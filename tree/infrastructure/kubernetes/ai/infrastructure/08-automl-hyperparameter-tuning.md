---
title: AutoML and Hyperparameter Tuning
description: '## one,AutoML Architecture Overview'
summary: 'from sklearn.gaussian_process import GaussianProcessRegressor'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- scheduler
- postgresql
- statefulset
- job
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is AutoML and Hyperparameter Tuning
- How to do AutoML and Hyperparameter Tuning
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AutoML and Hyperparameter Tuning
- ai
- infra
prerequisites:
- kubectl-basics
- gpu-scheduling-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
cross_refs:
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/08-automl-hyperparameter-tuning.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually can be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AutoML and Hyperparameter Tuning


## 1. AutoML Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        AutoML complete process                                      │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                  │
│  │ Data preprocessing   │───▶│ Feature engineering     │───▶│ Model selection     │                  │
│  │ AutoFE      │    │ AutoFeature │    │ NAS         │                  │
│  └─────────────┘    └─────────────┘    └─────────────┘                  │
│                                                │                          │
│                                                ▼                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                  │
│  │ Hyperparameter optimization   │◀───│ Model training     │◀───│ Architecture search     │                  │
│  │ HPO         │    │ Distributed │    │ DARTS/ENAS  │                  │
│  └─────────────┘    └─────────────┘    └─────────────┘                  │
│       │                    │                                              │
│       │                    ▼                                              │
│       │            ┌─────────────┐                                        │
│       └───────────▶│ Model evaluation     │                                        │
│                    │ Validation  │                                        │
│                    └─────────────┘                                        │
│                            │                                              │
│                            ▼                                              │
│                    ┌─────────────┐                                        │
│                    │ Model deployment     │                                        │
│                    │ Production  │                                        │
│                    └─────────────┘                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

---


## 2. Hyperparameter Optimization Algorithms

### 2.1 Algorithm Comparison

| Algorithm | Type | Advantage | Disadvantage | Scenario |
|-----|------|------|------|---------|
| **Grid Search** | Grid Search | Simple, reproducible | Exponential complexity | Small search space, discrete parameters |
| **Random Search** | Random Search | Efficient, easy to parallelize | No use of historical information | Moderate search space, initial exploration |
| **Bayesian Optimization** | Bayesian Optimization | Sample-efficient, intelligent | High computational cost | Expensive training, continuous parameters |
| **Hyperband/ASHA** | Early Stopping Strategy | Very fast, resource efficient | Depends on performance curve | Large-scale parallelism, quick screening |
| **Population Based Training** | Evolutionary Algorithms | Dynamic adjustment, online optimization | Requires multiple replicas | Long-term training, RL |
| **BOHB** | Hybrid Algorithm | Combines BO+HB advantages | Complex implementation | Recommended for production environments |

### 2.2 Principles of Bayesian Optimization

```python
"""
贝叶斯优化核心思想：
1. 构建目标函数的概率模型（高斯过程）
2. 使用采集函数（Acquisition Function）决定下一个采样点
3. 评估目标函数，更新概率模型
4. 重复2-3直至收敛

数学表示：
- 目标：max f(x), x ∈ X
- 高斯过程：f(x) ~ GP(μ(x), k(x,x'))
- 采集函数：α(x) = EI(x) | UCB(x) | PI(x)
  - EI (Expected Improvement): 期望改进
  - UCB (Upper Confidence Bound): 上置信界
  - PI (Probability of Improvement): 改进概率
"""

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from scipy.stats import norm
import numpy as np

class BayesianOptimizer:
    def __init__(self, bounds, n_iter=50):
        self.bounds = bounds
        self.n_iter = n_iter
        self.X_observed = []
        self.y_observed = []
        
        # Gaussian Process
        kernel = Matern(nu=2.5)
        self.gp = GaussianProcessRegressor(
            kernel=kernel,
            alpha=1e-6,
            normalize_y=True,
            n_restarts_optimizer=10
        )
    
    def acquisition_function(self, X, xi=0.01):
        """Expected Improvement Acquisition Function"""
        mu, sigma = self.gp.predict(X, return_std=True)
        
        if len(self.y_observed) == 0:
            return mu
        
        mu_best = np.max(self.y_observed)
        
        with np.errstate(divide='warn'):
            improvement = mu - mu_best - xi
            Z = improvement / sigma
            ei = improvement * norm.cdf(Z) + sigma * norm.pdf(Z)
            ei[sigma == 0.0] = 0.0
        
        return ei
    
    def suggest(self):
        """Recommend next sample point"""
        if len(self.X_observed) == 0:
            # Random initialization
            return np.random.uniform(self.bounds[:, 0], self.bounds[:, 1])
        
        # Fit Gaussian Process
        self.gp.fit(self.X_observed, self.y_observed)
        
        # Maximize Acquisition Function
        X_candidates = np.random.uniform(
            self.bounds[:, 0],
            self.bounds[:, 1],
            size=(1000, len(self.bounds))
        )
        ei = self.acquisition_function(X_candidates)
        
        return X_candidates[np.argmax(ei)]
    
    def observe(self, X, y):
        """Record observation results"""
        self.X_observed.append(X)
        self.y_observed.append(y)

# Usage Example
def objective_function(params):
    """Objective function: train model and return validation accuracy"""
    lr, batch_size, dropout = params
    # Training code...
    accuracy = train_and_evaluate(lr, batch_size, dropout)
    return accuracy

# Define Search Space
bounds = np.array([
    [1e-5, 1e-2],  # learning_rate
    [16, 128],      # batch_size
    [0.1, 0.5]      # dropout
])

optimizer = BayesianOptimizer(bounds, n_iter=30)

for i in range(30):
    # Recommended parameters
    params = optimizer.suggest()
    
    # Evaluation
    score = objective_function(params)
    
    # Record result
    optimizer.observe(params, score)
    
    print(f"Iteration {i+1}: params={params}, score={score}")

# Best Parameters
best_idx = np.argmax(optimizer.y_observed)
best_params = optimizer.X_observed[best_idx]
best_score = optimizer.y_observed[best_idx]
print(f"Best params: {best_params}, Best score: {best_score}")
```

---


## 3. Deep Optuna Practice

### 3.1 Advanced Features of Optuna

```python
import optuna
from optuna.pruners import MedianPruner
from optuna.samplers import TPESampler
import mlflow
import torch
from transformers import Trainer, TrainingArguments

# 1. Define Objective Function
def objective(trial):
    """Optuna Objective Function"""
    
    # Hyperparameter Sampling
    params = {
        "learning_rate": trial.suggest_float("learning_rate", 1e-5, 1e-3, log=True),
        "per_device_train_batch_size": trial.suggest_categorical("batch_size", [16, 32, 64]),
        "num_train_epochs": trial.suggest_int("num_epochs", 2, 5),
        "warmup_ratio": trial.suggest_float("warmup_ratio", 0.0, 0.2),
        "weight_decay": trial.suggest_float("weight_decay", 0.0, 0.1),
        
        # Model architecture parameters
        "num_hidden_layers": trial.suggest_int("num_hidden_layers", 6, 12),
        "hidden_dropout_prob": trial.suggest_float("dropout", 0.1, 0.3),
        "attention_probs_dropout_prob": trial.suggest_float("attention_dropout", 0.1, 0.3)
    }
    
    # Evaluate MLflow Tracking
    with mlflow.start_run(nested=True):
        mlflow.log_params(params)
        
        # Build model
        model_config = AutoConfig.from_pretrained("bert-base-uncased")
        model_config.num_hidden_layers = params["num_hidden_layers"]
        model_config.hidden_dropout_prob = params["hidden_dropout_prob"]
        model_config.attention_probs_dropout_prob = params["attention_probs_dropout_prob"]
        
        model = AutoModelForSequenceClassification.from_config(model_config)
        
        # Training parameters
        training_args = TrainingArguments(
            output_dir="/tmp/optuna_trial",
            learning_rate=params["learning_rate"],
            per_device_train_batch_size=params["per_device_train_batch_size"],
            num_train_epochs=params["num_train_epochs"],
            warmup_ratio=params["warmup_ratio"],
            weight_decay=params["weight_decay"],
            evaluation_strategy="epoch",
            save_strategy="no",
            load_best_model_at_end=False
        )
        
        # Trainer callbacks: mid-level pruning
        class OptunaCallback:
            def __init__(self, trial):
                self.trial = trial
            
            def on_evaluate(self, args, state, control, metrics, **kwargs):
                # Report intermediate results
                accuracy = metrics.get("eval_accuracy")
                self.trial.report(accuracy, state.epoch)
                
                # Check if pruning should occur
                if self.trial.should_prune():
                    raise optuna.TrialPruned()
        
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            callbacks=[OptunaCallback(trial)]
        )
        
        # Train
        trainer.train()
        
        # Final evaluation
        eval_results = trainer.evaluate()
        accuracy = eval_results["eval_accuracy"]
        
        mlflow.log_metric("accuracy", accuracy)
        
        return accuracy

# 2. Create Study (supports distributed)
study = optuna.create_study(
    study_name="bert-classification-hpo",
    direction="maximize",
    storage="postgresql://optuna:password@postgres.ai-platform.svc.cluster.local:5432/optuna",
    load_if_exists=True,
    
    # TPE sampler
    sampler=TPESampler(
        n_startup_trials=10,  # 前10次随机采样
        n_ei_candidates=24,
        seed=42
    ),
    
    # Median pruner
    pruner=MedianPruner(
        n_startup_trials=5,
        n_warmup_steps=2,
        interval_steps=1
    )
)

# 3. Run optimization
study.optimize(
    objective,
    n_trials=100,
    timeout=7200,  # 2小时超时
    n_jobs=1,  # 单进程（Kubernetes并行）
    show_progress_bar=True
)

# 4. Result analysis
print(f"Best trial: {study.best_trial.number}")
print(f"Best value: {study.best_value}")
print(f"Best params: {study.best_params}")

# Statistics
print(f"Finished trials: {len(study.trials)}")
print(f"Pruned trials: {len(study.get_trials(states=[optuna.trial.TrialState.PRUNED]))}")
print(f"Complete trials: {len(study.get_trials(states=[optuna.trial.TrialState.COMPLETE]))}")

# Visualization
import optuna.visualization as vis

# Optimization history
fig = vis.plot_optimization_history(study)
fig.write_html("optuna_history.html")

# Parameter importance
fig = vis.plot_param_importances(study)
fig.write_html("optuna_importances.html")

# Parallel coordinate plot
fig = vis.plot_parallel_coordinate(study)
fig.write_html("optuna_parallel.html")

# Hyperparameter relationships
fig = vis.plot_contour(study, params=["learning_rate", "batch_size"])
fig.write_html("optuna_contour.html")
```

### 3.2 Distributed Optuna on Kubernetes

```yaml
# PostgreSQL storage
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: optuna-postgres
  namespace: ai-platform
spec:
  serviceName: optuna-postgres
  replicas: 1
  selector:
    matchLabels:
      app: optuna-postgres
  template:
    metadata:
      labels:
        app: optuna-postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_DB
          value: optuna
        - name: POSTGRES_USER
          value: optuna
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: optuna-postgres-secret
              key: password
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
          limits:
            cpu: "4"
            memory: "8Gi"
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 50Gi
---
# Optuna Worker Job
apiVersion: batch/v1
kind: Job
metadata:
  name: optuna-hpo-workers
  namespace: ai-platform
spec:
  parallelism: 20  # 20个并行worker
  completions: 100  # 总共100次trial
  template:
    metadata:
      labels:
        app: optuna-worker
    spec:
      restartPolicy: OnFailure
      containers:
      - name: worker
        image: myregistry/optuna-trainer:latest
        command:
        - python
        - optimize.py
        - --study-name=bert-classification-hpo
        - --n-trials=1
        
        env:
        - name: OPTUNA_STORAGE
          value: "postgresql://optuna:$(POSTGRES_PASSWORD)@optuna-postgres:5432/optuna"
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: optuna-postgres-secret
              key: password
        - name: MLFLOW_TRACKING_URI
          value: "http://mlflow-server:5000"
        
        resources:
          requests:
            cpu: "8"
            memory: "32Gi"
            nvidia.com/gpu: 1
          limits:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: 1
        
        volumeMounts:
        - name: code
          mountPath: /workspace
        - name: dshm
          mountPath: /dev/shm
      
      volumes:
      - name: code
        configMap:
          name: optuna-training-code
      - name: dshm
        emptyDir:
          medium: Memory
          sizeLimit: 16Gi
```

---


## 4. Ray Tune Large-scale Parallelism

### 4.1 Ray Tune Architecture

```python
from ray import tune
from ray.tune import CLIReporter
from ray.tune.schedulers import ASHAScheduler, PopulationBasedTraining
from ray.tune.integration.mlflow import MLflowLoggerCallback
import torch
from functools import partial

def train_model(config, checkpoint_dir=None, data_dir=None):
    """Training function"""
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
    from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
    
    # Build model
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )
    
    # Training parameters
    training_args = TrainingArguments(
        output_dir="/tmp/ray_tune",
        learning_rate=config["learning_rate"],
        per_device_train_batch_size=config["batch_size"],
        num_train_epochs=config["num_epochs"],
        evaluation_strategy="epoch",
        save_strategy="no"
    )
    
    # Data loading
    train_dataset = load_dataset(data_dir, "train")
    eval_dataset = load_dataset(data_dir, "eval")
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset
    )
    
    # Training loop (supports checkpointing)
    for epoch in range(config["num_epochs"]):
        trainer.train()
        eval_results = trainer.evaluate()
        
        # Report metrics to Ray Tune
        tune.report(
            accuracy=eval_results["eval_accuracy"],
            loss=eval_results["eval_loss"]
        )

# Search space
search_space = {
    "learning_rate": tune.loguniform(1e-5, 1e-3),
    "batch_size": tune.choice([16, 32, 64]),
    "num_epochs": tune.choice([3, 5, 7]),
    "weight_decay": tune.uniform(0.0, 0.1)
}

# ASHA scheduler (asynchronous continuous halving)
scheduler = ASHAScheduler(
    metric="accuracy",
    mode="max",
    max_t=10,  # 最大epoch数
    grace_period=1,  # 至少运行1个epoch
    reduction_factor=2  # 每轮淘汰50%
)

# CLIReporter beautify output
reporter = CLIReporter(
    metric_columns=["accuracy", "loss", "training_iteration"],
    max_progress_rows=20
)

# Run hyperparameter search
analysis = tune.run(
    partial(train_model, data_dir="/data"),
    resources_per_trial={"cpu": 8, "gpu": 1},
    config=search_space,
    num_samples=50,  # 50次trial
    scheduler=scheduler,
    progress_reporter=reporter,
    local_dir="/tmp/ray_results",
    
    # MLflow integration
    callbacks=[
        MLflowLoggerCallback(
            tracking_uri="http://mlflow-server:5000",
            experiment_name="ray-tune-hpo",
            save_artifact=True
        )
    ],
    
    # Fault tolerance
    max_failures=3,
    raise_on_failed_trial=False
)

# Best configuration
best_trial = analysis.best_trial
print(f"Best trial config: {best_trial.config}")
print(f"Best trial final validation accuracy: {best_trial.last_result['accuracy']}")

# Get best model checkpoint
best_checkpoint = analysis.best_checkpoint
```

### 4.2 Population Based Training (PBT)

```python
from ray.tune.schedulers import PopulationBasedTraining

# PBT scheduler
pbt_scheduler = PopulationBasedTraining(
    time_attr="training_iteration",
    metric="accuracy",
    mode="max",
    
    # Perturb hyperparameters
    perturbation_interval=2,  # 每2个epoch扰动一次
    hyperparam_mutations={
        "learning_rate": lambda: tune.loguniform(1e-5, 1e-3).sample(),
        "weight_decay": lambda: tune.uniform(0.0, 0.1).sample()
    },
    
    # Exploration strategy
    resample_probability=0.25,  # 25%概率重新采样
    
    # Population size
    quantile_fraction=0.25,  # 淘汰底部25%
    
    # Resource configuration
    log_config=True
)

analysis = tune.run(
    train_model,
    name="pbt_experiment",
    scheduler=pbt_scheduler,
    num_samples=16,  # 种群大小16
    config={
        "learning_rate": tune.loguniform(1e-5, 1e-3),
        "weight_decay": tune.uniform(0.0, 0.1),
        "batch_size": 32,  # 固定
        "num_epochs": 20
    },
    resources_per_trial={"cpu": 4, "gpu": 1},
    stop={"training_iteration": 20}
)
```

---


## 5. Neural Architecture Search (NAS)

### 5.1 Differentiable Architecture Search (DARTS)

```python
import torch
import torch.nn as nn

class DARTSCell(nn.Module):
    """DARTS search unit"""
    def __init__(self, C_in, C_out, stride=1):
        super().__init__()
        self.stride = stride
        
        # Candidate operations
        self.ops = nn.ModuleList([
            nn.Identity(),
            nn.MaxPool2d(3, stride=stride, padding=1),
            nn.AvgPool2d(3, stride=stride, padding=1),
            SepConv(C_in, C_out, 3, stride),
            SepConv(C_in, C_out, 5, stride),
            DilConv(C_in, C_out, 3, stride, dilation=2),
            DilConv(C_in, C_out, 5, stride, dilation=2),
            nn.Sequential()  # zero operation
        ])
        
        # Architecture parameters (learnable)
        self.alpha = nn.Parameter(torch.randn(len(self.ops)))
    
    def forward(self, x):
        # Weighted sum of all operations
        weights = torch.softmax(self.alpha, dim=0)
        return sum(w * op(x) for w, op in zip(weights, self.ops))

class DARTSNetwork(nn.Module):
    def __init__(self, C=16, num_cells=8, num_classes=10):
        super().__init__()
        self.stem = nn.Conv2d(3, C, 3, padding=1)
        
        # Stack DARTS units
        self.cells = nn.ModuleList([
            DARTSCell(C, C) for _ in range(num_cells)
        ])
        
        self.classifier = nn.Linear(C, num_classes)
    
    def forward(self, x):
        x = self.stem(x)
        for cell in self.cells:
            x = cell(x)
        x = x.mean([2, 3])  # Global average pooling
        return self.classifier(x)
    
    def arch_parameters(self):
        """Return architecture parameters"""
        return [cell.alpha for cell in self.cells]
    
    def model_parameters(self):
        """Return model weight parameters"""
        params = []
        for name, param in self.named_parameters():
            if 'alpha' not in name:
                params.append(param)
        return params

# DARTS training process
def train_darts(model, train_loader, val_loader, epochs=50):
    # Two optimizers
    w_optimizer = torch.optim.SGD(
        model.model_parameters(),
        lr=0.025,
        momentum=0.9,
        weight_decay=3e-4
    )
    
    alpha_optimizer = torch.optim.Adam(
        model.arch_parameters(),
        lr=3e-4,
        betas=(0.5, 0.999),
        weight_decay=1e-3
    )
    
    for epoch in range(epochs):
        # 1. Update architecture parameters α (on validation set)
        for batch in val_loader:
            images, labels = batch
            
            alpha_optimizer.zero_grad()
            logits = model(images)
            loss = nn.CrossEntropyLoss()(logits, labels)
            loss.backward()
            alpha_optimizer.step()
        
        # 2. Update model weights w (on training set)
        for batch in train_loader:
            images, labels = batch
            
            w_optimizer.zero_grad()
            logits = model(images)
            loss = nn.CrossEntropyLoss()(logits, labels)
            loss.backward()
            w_optimizer.step()
        
        print(f"Epoch {epoch+1}: Architecture weights updated")
    
    # Export final architecture
    for i, cell in enumerate(model.cells):
        best_op_idx = torch.argmax(cell.alpha).item()
        print(f"Cell {i}: Best operation index = {best_op_idx}")
```

### 5.2 Once-for-All (OFA) Network

```python
"""
Once-for-All思想：
训练一个超网络，支持多种架构配置（深度、宽度、kernel size）
部署时根据硬件约束选择子网络，无需重新训练

优势：
- 一次训练，多次部署
- 支持边缘设备（移动端、IoT）
- 延迟-精度权衡
"""

from ofa.model_zoo import ofa_net
from ofa.nas.accuracy_predictor import AccuracyPredictor
from ofa.nas.efficiency_predictor import LatencyPredictor

# Load pre-trained OFA network
ofa_network = ofa_net('ofa_mbv3_d234_e346_k357_w1.2', pretrained=True)

# Search for optimal subnetwork
accuracy_predictor = AccuracyPredictor(ofa_network)
latency_predictor = LatencyPredictor(device='note10')  # Samsung Note10

# Constraints
latency_constraint = 20  # 20ms延迟

# Evolutionary search
best_config = evolutionary_search(
    ofa_network,
    accuracy_predictor,
    latency_predictor,
    latency_constraint=latency_constraint,
    population_size=100,
    num_generations=30
)

print(f"Best config: {best_config}")
print(f"Estimated accuracy: {accuracy_predictor(best_config)}")
print(f"Estimated latency: {latency_predictor(best_config)}ms")

# Export subnetwork
subnet = ofa_network.get_active_subnet(best_config)
torch.save(subnet.state_dict(), "optimized_subnet.pth")
```

---


## 6. AutoML Platform Comparison

| Platform | Algorithm Support | Distributed | NAS Support | Usability | Open Source |
|-----|---------|--------|---------|--------|------|
| **Optuna** | BO, TPE, CMA-ES | ✅ | ❌ | ★★★★★ | ✅ |
| **Ray Tune** | Grid, Random, BO, ASHA, PBT | ✅ | ✅ | ★★★★☆ | ✅ |
| **Hyperopt** | TPE, Random | ❌ | ❌ | ★★★☆☆ | ✅ |
| **Keras Tuner** | Random, Hyperband, BO | ❌ | ✅ | ★★★★☆ | ✅ |
| **Auto-sklearn** | SMAC, meta-learning | ❌ | ❌ | ★★★★★ | ✅ |
| **Google Vertex AI** | BO, Grid | ✅ | ❌ | ★★★★☆ | ❌ |
| **Azure AutoML** | Multiple | ✅ | ✅ | ★★★★☆ | ❌ |

**Recommended Choice:**
- Deep Learning: Ray Tune (massive parallelism) + Optuna (fine-tuning optimization)
- Traditional ML: Auto-sklearn (fast baseline)
- Production Environment: Ray Tune + [[Kubernetes|Kubernetes]] (elastic scaling)
- Academic Research: Optuna (flexible, scalable)

---


## 7. Multi-objective Optimization

### 7.1 Pareto Frontier Search

```python
import optuna

def multi_objective(trial):
    """Multi-objective optimization: precision vs latency"""
    # Hyperparameters
    num_layers = trial.suggest_int("num_layers", 6, 24)
    hidden_size = trial.suggest_categorical("hidden_size", [256, 512, 768, 1024])
    
    # Train model
    model = build_model(num_layers, hidden_size)
    accuracy = train_and_evaluate(model)
    
    # Inference latency (ms)
    latency = benchmark_latency(model)
    
    return accuracy, latency

# Create multi-objective Study
study = optuna.create_study(
    directions=["maximize", "minimize"],  # 最大化精度，最小化延迟
    study_name="multi-objective-hpo"
)

study.optimize(multi_objective, n_trials=100)

# Get Pareto frontier
pareto_trials = study.best_trials

print(f"Number of Pareto optimal trials: {len(pareto_trials)}")

for trial in pareto_trials:
    print(f"Trial {trial.number}:")
    print(f"  Accuracy: {trial.values[0]:.4f}")
    print(f"  Latency: {trial.values[1]:.2f}ms")
    print(f"  Params: {trial.params}")

# Visualize Pareto frontier
import optuna.visualization as vis
fig = vis.plot_pareto_front(study, target_names=["Accuracy", "Latency"])
fig.write_html("pareto_front.html")
```

---


## 8. AutoML Pipeline

### 8.1 Complete AutoML Workflow

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from auto_sklearn.classification import AutoSklearnClassifier
import pandas as pd

# Load data
df = pd.read_csv("data.csv")
X = df.drop("target", axis=1)
y = df["target"]

# Automatic feature engineering
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Auto-sklearn automatic model selection + hyperparameter optimization
automl = AutoSklearnClassifier(
    time_left_for_this_task=3600,  # 1小时
    per_run_time_limit=300,  # 每次trial 5分钟
    n_jobs=8,
    ensemble_size=50,
    ensemble_nbest=200,
    initial_configurations_via_metalearning=25,
    metric=autosklearn.metrics.accuracy
)

# Complete Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', automl)
])

# Train (automatic search)
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}")

# View the best model found by Auto-sklearn
print(automl.show_models())

# Output example:
# [(0.52, SimpleClassificationPipeline(...RandomForest...)),
#  (0.28, SimpleClassificationPipeline(...GradientBoosting...)),
#  (0.20, SimpleClassificationPipeline(...SVM...))]
```

---


## 9. Production Environment Deployment

### 9.1 Template for Hyperparameter Optimization Jobs

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hpo-bert-classification
  namespace: ai-platform
  labels:
    app: hpo
    model: bert
spec:
  parallelism: 10
  completions: 50
  template:
    metadata:
      labels:
        app: hpo-worker
    spec:
      restartPolicy: OnFailure
      
      # Initialization Container: waits for Optuna DB to be ready
      initContainers:
      - name: wait-for-db
        image: busybox:latest
        command:
        - sh
        - -c
        - |
          until nc -z optuna-postgres 5432; do
            echo "Waiting for PostgreSQL..."
            sleep 2
          done
      
      containers:
      - name: hpo-worker
        image: myregistry/optuna-bert-trainer:v1.0
        command:
        - python
        - /workspace/optimize.py
        - --study-name=bert-classification-hpo
        - --n-trials=1
        
        env:
        - name: OPTUNA_STORAGE
          value: "postgresql://optuna:$(POSTGRES_PASSWORD)@optuna-postgres:5432/optuna"
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: optuna-postgres-secret
              key: password
        - name: MLFLOW_TRACKING_URI
          value: "http://mlflow-server:5000"
        - name: MLFLOW_EXPERIMENT_NAME
          value: "hpo-bert-classification"
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: access-key-id
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: secret-access-key
        
        resources:
          requests:
            cpu: "8"
            memory: "32Gi"
            nvidia.com/gpu: 1
          limits:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: 1
        
        volumeMounts:
        - name: workspace
          mountPath: /workspace
        - name: cache
          mountPath: /root/.cache
        - name: dshm
          mountPath: /dev/shm
      
      volumes:
      - name: workspace
        configMap:
          name: hpo-training-code
      - name: cache
        emptyDir: {}
      - name: dshm
        emptyDir:
          medium: Memory
          sizeLimit: 16Gi
      
      # Init container: wait for Optuna DB to be ready
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            preference:
              matchExpressions:
              - key: karpenter.sh/capacity-type
                operator: In
                values: ["spot"]
```

### 9.2 Cost Optimization Strategies

**Spot Instances Savings:**
```yaml
# Karpenter Provisioner for HPO
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: hpo-spot-provisioner
spec:
  requirements:
  - key: karpenter.sh/capacity-type
    operator: In
    values: ["spot"]
  - key: node.kubernetes.io/instance-type
    operator: In
    values: ["g5.xlarge", "g5.2xlarge", "g4dn.xlarge"]
  - key: nvidia.com/gpu
    operator: Exists
  
  # Spot interruption handling
  ttlSecondsAfterEmpty: 30
  ttlSecondsUntilExpired: 3600  # 1小时
  
  limits:
    resources:
      nvidia.com/gpu: 50

# Cost savings:
# - On-Demand g5.xlarge: $1.006/hour
# - Spot g5.xlarge: ~$0.30/hour (70% off)
# - 50 trials × 30 minutes = 25 GPU hours
# - On-Demand cost: $25.15
# - Spot cost: $7.50
# - Savings: $17.65 (70%)
```

---


## 10. Best Practices

### 10.1 Hyperparameter Search Strategies

**1. Broad Search + Narrow Search:**
```python
# Stage 1: Coarse Search (Broad Scope, Few Samples)
coarse_search_space = {
    "learning_rate": tune.loguniform(1e-6, 1e-2),  # 4个数量级
    "batch_size": tune.choice([8, 16, 32, 64, 128]),
    "num_layers": tune.randint(6, 24)
}

coarse_analysis = tune.run(
    train_model,
    config=coarse_search_space,
    num_samples=20,  # 少量样本
    resources_per_trial={"gpu": 1}
)

best_coarse_lr = coarse_analysis.best_config["learning_rate"]

# Stage 2: Fine Search (Narrow Scope, Diverse Samples)
fine_search_space = {
    "learning_rate": tune.uniform(
        best_coarse_lr * 0.5,
        best_coarse_lr * 2.0
    ),  # 围绕最佳值
    "batch_size": tune.choice([32, 64]),  # 固定两个候选
    "num_layers": 12  # 固定
}

fine_analysis = tune.run(
    train_model,
    config=fine_search_space,
    num_samples=50,  # 更多样本
    resources_per_trial={"gpu": 1}
)
```

**2. Optimize the learning rate first, then optimize other parameters:**
```python
# Learning rate has the greatest impact on model performance, prioritize optimization
# Step 1: Optimize only LR
lr_search = {
    "learning_rate": tune.loguniform(1e-5, 1e-3),
    "batch_size": 32,  # 固定
    "num_epochs": 3
}

# Step 2: Fix the best LR and optimize other parameters
best_lr = lr_analysis.best_config["learning_rate"]

other_search = {
    "learning_rate": best_lr,  # 固定
    "batch_size": tune.choice([16, 32, 64]),
    "weight_decay": tune.uniform(0.0, 0.1),
    "warmup_ratio": tune.uniform(0.0, 0.2)
}
```

### 10.2 Avoid Overfitting Search Space

```python
"""
常见错误：在测试集上评估超参数，导致信息泄露

正确做法：
1. 训练集：训练模型
2. 验证集：超参数优化
3. 测试集：最终评估（仅一次）
"""

# ❌ Error Example
def objective_wrong(trial):
    model = train(config)
    accuracy = evaluate(model, test_dataset)  # 泄露测试集信息！
    return accuracy

# ✅ Correct Example
def objective_correct(trial):
    model = train(config, train_dataset)
    accuracy = evaluate(model, val_dataset)  # 使用验证集
    return accuracy

# Final Evaluation (Once Only)
best_model = load_model(best_trial)
final_accuracy = evaluate(best_model, test_dataset)
```

### 10.3 Early Stopping Strategy

```python
# Optuna MedianPruner
pruner = MedianPruner(
    n_startup_trials=10,  # 前10次trial不剪枝
    n_warmup_steps=2,  # 前2个epoch不剪枝
    interval_steps=1  # 每个epoch检查一次
)

# Report intermediate results within the training loop
for epoch in range(num_epochs):
    train_loss = train_one_epoch()
    val_accuracy = validate()
    
    # Report to Optuna
    trial.report(val_accuracy, epoch)
    
    # Check if pruning should be performed
    if trial.should_prune():
        raise optuna.TrialPruned()

# Effect: Save 50-70% computational resources
```

---


## 11. Monitoring and Visualization

### 11.1 Real-time Monitoring Dashboard

```python
import optuna
from optuna.visualization import plot_optimization_history, plot_param_importances
import streamlit as st

# Streamlit Real-time Dashboard
st.title("Hyperparameter Optimization Dashboard")

# Connect Optuna Study
study = optuna.load_study(
    study_name="bert-classification-hpo",
    storage="postgresql://optuna:password@postgres:5432/optuna"
)

# Real-time Refresh
while True:
    # Optimize History
    st.subheader("Optimization History")
    fig1 = plot_optimization_history(study)
    st.plotly_chart(fig1)
    
    # Parameter Importance
    st.subheader("Hyperparameter Importances")
    fig2 = plot_param_importances(study)
    st.plotly_chart(fig2)
    
    # Statistical Information
    st.subheader("Statistics")
    st.metric("Total Trials", len(study.trials))
    st.metric("Best Value", f"{study.best_value:.4f}")
    st.metric("Best Trial", study.best_trial.number)
    
    # Best Parameters
    st.subheader("Best Parameters")
    st.json(study.best_params)
    
    time.sleep(10)  # 每10秒刷新
```

---

**Related tables:**
- [111-AI Infrastructure Architecture](./01-ai-infrastructure.md)
- [112-Distributed Training Frameworks](./05-distributed-training-frameworks.md)
- [117-AI Experiment Management](./07-ai-experiment-management.md)

**Version Information:**
- Optuna: v3.5.0+
- Ray Tune: v2.9.0+
- Auto-sklearn: v0.15.0+
- Kubernetes: v1.27+

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure - Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AI Model Registry and Version Management
- AI Model Deployment and Lifecycle Management

## See Also

- 06-ai-data-pipeline
- 07-ai-experiment-management
- 09-model-registry
- 10-model-deployment-management

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
