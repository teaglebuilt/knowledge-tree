---
title: 33 - Model Explainability and Transparency
description: '### 1.1 Panoramic Architecture of Explainability'
summary: '### 1.1 Panoramic Architecture of Explainability'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- hpa
- job
- rag
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
- What is model explainability and transparency
- How is model explainability and transparency
- Kubernetes 11 ai infra best practices
trigger_keywords:
- Model Explainability and Transparency
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/33-model-explainability.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Please confirm before execution: that the target cluster and namespace are correct; that you have sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but can usually be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 33 - Model Explainability and Transparency

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Advanced | **References**: [SHAP](https://shap.readthedocs.io/) | [LIME](https://github.com/marcotcr/lime) | [InterpretML](https://interpret.ml/)


## 1. Model Explainability Framework

### 1.1 Explainability Panoramic Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                       Model Explainability Framework                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Global Interpretability                             │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │  │
│  │  │ Feature         │  │ Model           │  │ Partial         │               │  │
│  │  │ Importance      │  │ Summary         │  │ Dependence      │               │  │
│  │  │ (SHAP/LIME)     │  │ Plots           │  │ Plots           │               │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Local Interpretability                              │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │  │
│  │  │ Individual      │  │ Counterfactual  │  │ Adversarial     │               │  │
│  │  │ Prediction      │  │ Explanations    │  │ Examples        │               │  │
│  │  │ Explanations    │  │ (What-if)       │  │ (Robustness)    │               │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Operationalization                                  │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │  │
│  │  │ API Endpoint    │  │ Dashboard       │  │ Alert System    │               │  │
│  │  │ (/explain)      │  │ Visualization   │  │ (Bias/Fairness) │               │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Classification of Explainability Methods

| Method Category | Technical Name | Applicable Scenario | Advantage | Limitation |
|----------|----------|----------|------|--------|
| **Global Interpretation** | SHAP Values | Decision Trees, Neural Networks | Comprehensive, theoretically sound | High computational complexity |
| | Feature Importance | Linear Models, Decision Trees | Simple and intuitive | Ignores feature interactions |
| | Partial Dependence Plot | Any Model | Visualizes interaction effects | Curse of dimensionality |
| **Local Interpretation** | LIME | Black-box Models | Instance-level explanation | Instability |
| | Decision Boundary | Classification Models | Intuitive decision resolution | Visualization difficult in high-dimensional spaces |
| | Gradient Methods | Deep Learning | Efficient computation | Sensitive to input |
| **Comparison Interpretation** | Counterfactual | Any Model | Business-oriented | Difficult to generate |
| | Adversarial Samples | Security Detection | Robustness assessment | May mislead |

---


## 2. SHAP Explainability Implementation

### 2.1 Foundation Configuration of SHAP

```python
# shap_explainer.py
import shap
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import joblib

class ModelExplainer:
    def __init__(self, model_path, training_data_path):
        self.model = joblib.load(model_path)
        self.training_data = pd.read_csv(training_data_path)
        self.feature_names = [col for col in self.training_data.columns if col != 'target']
        self.X_train = self.training_data[self.feature_names]
        self.y_train = self.training_data['target']
        
    def calculate_shap_values(self, sample_size=1000):
        \"\"\"Calculate SHAP values\"\"\"
        # Sample to improve computational efficiency
        X_sample = shap.utils.sample(self.X_train, sample_size)
        
        # Create an interpreter
        if hasattr(self.model, 'predict_proba'):
            explainer = shap.TreeExplainer(self.model, X_sample)
            shap_values = explainer.shap_values(X_sample)
        else:
            explainer = shap.LinearExplainer(self.model, X_sample)
            shap_values = explainer.shap_values(X_sample)
        
        return explainer, shap_values, X_sample
    
    def global_explanations(self):
        \"\"\"Generate global explanation\"\"\"
        explainer, shap_values, X_sample = self.calculate_shap_values()
        
        # Feature importance ranking
        feature_importance = np.abs(shap_values).mean(0)
        importance_df = pd.DataFrame({
            'feature': self.feature_names,
            'importance': feature_importance
        }).sort_values('importance', ascending=False)
        
        # Save to MLflow
        with mlflow.start_run():
            mlflow.log_figure(
                self._plot_feature_importance(importance_df),
                'feature_importance.png'
            )
            
            # SHAP summary plot
            plt.figure(figsize=(10, 8))
            shap.summary_plot(shap_values, X_sample, show=False)
            plt.tight_layout()
            mlflow.log_figure(plt.gcf(), 'shap_summary.png')
            plt.close()
        
        return importance_df
    
    def local_explanations(self, instance_idx=0):
        \"\"\"Generate local explanation\"\"\"
        explainer, shap_values, X_sample = self.calculate_shap_values()
        
        # Single prediction explanation
        instance = X_sample.iloc[instance_idx:instance_idx+1]
        prediction = self.model.predict(instance)[0]
        probability = self.model.predict_proba(instance)[0][1] if hasattr(self.model, 'predict_proba') else None
        
        # SHAP influence
        plt.figure(figsize=(12, 6))
        shap.waterfall_plot(
            shap.Explanation(
                values=shap_values[instance_idx],
                base_values=explainer.expected_value,
                data=instance.iloc[0],
                feature_names=self.feature_names
            ),
            show=False
        )
        plt.tight_layout()
        
        # Save explanation results
        explanation_result = {
            'instance_index': instance_idx,
            'prediction': float(prediction),
            'probability': float(probability) if probability else None,
            'shap_values': shap_values[instance_idx].tolist(),
            'feature_values': instance.iloc[0].to_dict()
        }
        
        return explanation_result, plt.gcf()
    
    def _plot_feature_importance(self, importance_df):
        \"\"\"Draw feature importance plot\"\"\"
        plt.figure(figsize=(10, 8))
        sns.barplot(
            data=importance_df.head(15),
            x='importance',
            y='feature',
            palette='viridis'
        )
        plt.title('Top 15 Feature Importance (SHAP)')
        plt.xlabel('Mean |SHAP Value|')
        plt.ylabel('Features')
        plt.tight_layout()
        return plt.gcf()

# Usage Example
explainer = ModelExplainer(
    model_path='/models/churn_model.pkl',
    training_data_path='/data/training_data.csv'
)

# Global Explanation
global_importance = explainer.global_explanations()
print(global_importance.head(10))

# Local Explanation
local_explanation, plot = explainer.local_explanations(instance_idx=42)
plt.show(plot)
```

### 2.2 Explainability API Service

```python
# explainability_api.py
from flask import Flask, request, jsonify
import shap
import numpy as np
import pandas as pd
import joblib
from prometheus_client import Counter, Histogram, generate_latest
import logging

app = Flask(__name__)

# Metric Definition
explanation_requests = Counter('explanation_requests_total', 'Total explanation requests')
explanation_errors = Counter('explanation_errors_total', 'Explanation errors')
explanation_duration = Histogram('explanation_duration_seconds', 'Time spent processing explanations')

# Initialize model and interpreter
model = joblib.load('/models/production_model.pkl')
explainer = shap.TreeExplainer(model)

# Feature names (must be consistent with training)
FEATURE_NAMES = [
    'age', 'income', 'credit_score', 'account_balance',
    'transaction_frequency', 'product_usage', 'support_tickets',
    'days_since_last_login', 'num_products', 'is_active_member'
]

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/explain', methods=['POST'])
@explanation_duration.time()
def explain_prediction():
    \"\"\"Provide model prediction explanation\"\"\"
    explanation_requests.inc()
    
    try:
        # Parse request
        data = request.get_json()
        instance = np.array(data['features']).reshape(1, -1)
        instance_df = pd.DataFrame(instance, columns=FEATURE_NAMES)
        
        # Calculate SHAP values
        shap_values = explainer.shap_values(instance_df)
        
        # Generate explanation
        base_value = explainer.expected_value
        prediction = model.predict(instance)[0]
        probability = model.predict_proba(instance)[0][1] if hasattr(model, 'predict_proba') else None
        
        # Construct response
        explanation = {
            'prediction': int(prediction),
            'probability': float(probability) if probability else None,
            'base_value': float(base_value),
            'shap_values': shap_values.tolist()[0] if isinstance(shap_values, np.ndarray) else shap_values[1].tolist()[0],
            'feature_values': dict(zip(FEATURE_NAMES, instance[0])),
            'feature_contributions': sorted([
                {
                    'feature': FEATURE_NAMES[i],
                    'value': float(instance[0][i]),
                    'contribution': float(shap_values[0][i]) if isinstance(shap_values, np.ndarray) else float(shap_values[1][0][i]),
                    'abs_contribution': abs(float(shap_values[0][i]) if isinstance(shap_values, np.ndarray) else float(shap_values[1][0][i]))
                }
                for i in range(len(FEATURE_NAMES))
            ], key=lambda x: x['abs_contribution'], reverse=True)
        }
        
        return jsonify(explanation)
        
    except Exception as e:
        explanation_errors.inc()
        logging.error(f\"Explanation error: {str(e)}\")
        return jsonify({'error': str(e)}), 500

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/feature-importance')
def feature_importance():
    \"\"\"Get global feature importance\"\"\"
    try:
        # Calculate global importance using training data
        training_data = pd.read_csv('/data/training_sample.csv')
        X_sample = shap.utils.sample(training_data[FEATURE_NAMES], 1000)
        shap_values = explainer.shap_values(X_sample)
        
        # Calculate average absolute SHAP value
        importance = np.abs(shap_values).mean(0)
        importance_dict = dict(zip(FEATURE_NAMES, importance.tolist()))
        
        return jsonify({
            'feature_importance': importance_dict,
            'top_features': sorted(
                [{'feature': k, 'importance': v} for k, v in importance_dict.items()],
                key=lambda x: x['importance'],
                reverse=True
            )[:10]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2.3 Kubernetes Deployment Configuration

```yaml
# explainability-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-explainability-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: explainability-api
  template:
    metadata:
      labels:
        app: explainability-api
    spec:
      containers:
      - name: explainability-api
        image: company/explainability-api:v1.0
        ports:
        - containerPort: 5000
        env:
        - name: MODEL_PATH
          value: \"/models/production_model.pkl\"
        - name: TRAINING_DATA_PATH
          value: \"/data/training_sample.csv\"
        - name: FLASK_ENV
          value: \"production\"
        resources:
          requests:
            cpu: \"500m\"
            memory: \"1Gi\"
          limits:
            cpu: \"1\"
            memory: \"2Gi\"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: model-storage
          mountPath: /models
        - name: data-storage
          mountPath: /data
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-pvc
      - name: data-storage
        persistentVolumeClaim:
          claimName: data-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: explainability-api-service
spec:
  selector:
    app: explainability-api
  ports:
  - port: 80
    targetPort: 5000
  type: ClusterIP

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: explainability-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-explainability-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---


## 3. Fairness and Bias Detection

### 3.1 Fairness Evaluation Framework

```python
# fairness_analyzer.py
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
import mlflow

class FairnessAnalyzer:
    def __init__(self, predictions_df, protected_attributes):
        self.df = predictions_df
        self.protected_attrs = protected_attributes
        
    def calculate_disparate_impact(self, group1_condition, group2_condition):
        \"\"\"Calculate difference impact ratio\"\"\"
        group1_positive = self.df[group1_condition]['prediction'].mean()
        group2_positive = self.df[group2_condition]['prediction'].mean()
        
        if group2_positive == 0:
            return float('inf')
        
        disparate_impact = group1_positive / group2_positive
        return disparate_impact
    
    def demographic_parity_difference(self, group1_condition, group2_condition):
        \"\"\"Calculate population parity difference\"\"\"
        group1_positive_rate = self.df[group1_condition]['prediction'].mean()
        group2_positive_rate = self.df[group2_condition]['prediction'].mean()
        
        return abs(group1_positive_rate - group2_positive_rate)
    
    def equal_opportunity_difference(self, group1_condition, group2_condition):
        \"\"\"Calculate opportunity equality difference\"\"\"
        # Consider only positive class samples
        positive_samples = self.df[self.df['true_label'] == 1]
        
        group1_tpr = positive_samples[group1_condition]['prediction'].mean()
        group2_tpr = positive_samples[group2_condition]['prediction'].mean()
        
        return abs(group1_tpr - group2_tpr)
    
    def analyze_bias(self):
        \"\"\"Comprehensive bias analysis\"\"\"
        bias_metrics = {}
        
        for attr in self.protected_attrs:
            if attr not in self.df.columns:
                continue
                
            # For binary attributes
            if self.df[attr].nunique() == 2:
                values = self.df[attr].unique()
                group1_cond = self.df[attr] == values[0]
                group2_cond = self.df[attr] == values[1]
                
                bias_metrics[f'{attr}_disparate_impact'] = self.calculate_disparate_impact(
                    group1_cond, group2_cond
                )
                bias_metrics[f'{attr}_demographic_parity'] = self.demographic_parity_difference(
                    group1_cond, group2_cond
                )
                bias_metrics[f'{attr}_equal_opportunity'] = self.equal_opportunity_difference(
                    group1_cond, group2_cond
                )
        
        return bias_metrics
    
    def plot_bias_analysis(self):
        \"\"\"Visualize bias analysis results\"\"\"
        bias_results = self.analyze_bias()
        
        # Create visualization
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Difference impact ratio
        di_metrics = {k: v for k, v in bias_results.items() if 'disparate_impact' in k}
        axes[0].bar(di_metrics.keys(), di_metrics.values())
        axes[0].axhline(y=0.8, color='r', linestyle='--', label='Fairness threshold (0.8)')
        axes[0].axhline(y=1.2, color='r', linestyle='--', label='Fairness threshold (1.2)')
        axes[0].set_title('Disparate Impact Ratio')
        axes[0].set_ylabel('Ratio')
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].legend()
        
        # Population parity
        dp_metrics = {k: v for k, v in bias_results.items() if 'demographic_parity' in k}
        axes[1].bar(dp_metrics.keys(), dp_metrics.values())
        axes[1].axhline(y=0.1, color='r', linestyle='--', label='Fairness threshold (0.1)')
        axes[1].set_title('Demographic Parity Difference')
        axes[1].set_ylabel('Difference')
        axes[1].tick_params(axis='x', rotation=45)
        axes[1].legend()
        
        # Equal opportunity
        eo_metrics = {k: v for k, v in bias_results.items() if 'equal_opportunity' in k}
        axes[2].bar(eo_metrics.keys(), eo_metrics.values())
        axes[2].axhline(y=0.1, color='r', linestyle='--', label='Fairness threshold (0.1)')
        axes[2].set_title('Equal Opportunity Difference')
        axes[2].set_ylabel('Difference')
        axes[2].tick_params(axis='x', rotation=45)
        axes[2].legend()
        
        plt.tight_layout()
        
        # Record to MLflow
        with mlflow.start_run():
            mlflow.log_figure(fig, 'bias_analysis.png')
        
        return fig, bias_results

# Usage example
predictions_df = pd.read_csv('/data/model_predictions.csv')
analyzer = FairnessAnalyzer(
    predictions_df=predictions_df,
    protected_attributes=['gender', 'race', 'age_group']
)

fig, bias_metrics = analyzer.plot_bias_analysis()
print(\"Bias analysis results:\")
for metric, value in bias_metrics.items():
    print(f\"{metric}: {value:.4f}\")
```

### 3.2 Bias Mitigation Strategies

```python
# bias_mitigation.py
from aif360.algorithms.preprocessing import Reweighing, DisparateImpactRemover
from aif360.algorithms.inprocessing import PrejudiceRemover
from aif360.algorithms.postprocessing import CalibratedEqOddsPostprocessing, RejectOptionClassification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class BiasMitigationPipeline:
    def __init__(self, dataset, target_column, protected_attribute):
        self.dataset = dataset
        self.target_col = target_column
        self.protected_attr = protected_attribute
        
        # Convert to AIF360 format
        self.aif_dataset = BinaryLabelDataset(
            df=dataset,
            label_names=[target_column],
            protected_attribute_names=[protected_attribute]
        )
        
    def reweighing_preprocessing(self):
        \"\"\"Re-weight preprocessing\"\"\"
        rw = Reweighing(
            unprivileged_groups=[{self.protected_attr: 0}],
            privileged_groups=[{self.protected_attr: 1}]
        )
        
        transf_dataset = rw.fit_transform(self.aif_dataset)
        return transf_dataset
    
    def disparate_impact_remover(self, repair_level=1.0):
        \"\"\"Difference impact elimination\"\"\"
        dir = DisparateImpactRemover(
            repair_level=repair_level,
            sensitive_attribute=self.protected_attr
        )
        
        transf_dataset = dir.fit_transform(self.aif_dataset)
        return transf_dataset
    
    def prejudice_remover_inprocessing(self, eta=25.0):
        \"\"\"Process-level bias elimination\"\"\"
        # Split data
        train_data, test_data = self.aif_dataset.split([0.7], shuffle=True)
        
        # Train bias mitigation model
        pr = PrejudiceRemover(
            sensitive_attr=self.protected_attr,
            eta=eta
        )
        
        pr.fit(train_data)
        predictions = pr.predict(test_data)
        
        return predictions
    
    def calibrated_equalized_odds_postprocessing(self, model_predictions):
        \"\"\"Calibration equalized odds post-processing\"\"\"
        # Create prediction dataset
        pred_dataset = self.aif_dataset.copy()
        pred_dataset.labels = model_predictions.reshape(-1, 1)
        
        # Split data
        dataset_orig_train, dataset_orig_test = self.aif_dataset.split([0.7], shuffle=True)
        dataset_pred_train, dataset_pred_test = pred_dataset.split([0.7], shuffle=True)
        
        # Train post-processor
        cpp = CalibratedEqOddsPostprocessing(
            privileged_groups=[{self.protected_attr: 1}],
            unprivileged_groups=[{self.protected_attr: 0}],
            cost_constraint='fnr'  # 可选: 'fpr', 'weighted'
        )
        
        cpp = cpp.fit(dataset_orig_train, dataset_pred_train)
        transf_predictions = cpp.predict(dataset_pred_test)
        
        return transf_predictions
    
    def evaluate_fairness(self, predictions, original_labels):
        \"\"\"Evaluate fairness metrics\"\"\"
        # Create metric object
        metric = ClassificationMetric(
            self.aif_dataset,
            predictions,
            unprivileged_groups=[{self.protected_attr: 0}],
            privileged_groups=[{self.protected_attr: 1}]
        )
        
        fairness_metrics = {
            'disparate_impact': metric.disparate_impact(),
            'statistical_parity_difference': metric.statistical_parity_difference(),
            'equal_opportunity_difference': metric.equal_opportunity_difference(),
            'average_odds_difference': metric.average_odds_difference(),
            'theil_index': metric.theil_index()
        }
        
        return fairness_metrics

# Usage example
mitigation = BiasMitigationPipeline(
    dataset=pd.read_csv('/data/training_data.csv'),
    target_column='loan_approved',
    protected_attribute='race'
)

# Apply different mitigation strategies
reweighed_data = mitigation.reweighing_preprocessing()
di_removed_data = mitigation.disparate_impact_remover(repair_level=0.8)
pr_predictions = mitigation.prejudice_remover_inprocessing(eta=50.0)

# Evaluate fairness
fairness_scores = mitigation.evaluate_fairness(pr_predictions, di_removed_data.labels)
print(\"Fairness evaluation results:\", fairness_scores)
```

---


## 4. Explainable Monitoring and Alerts

### 4.1 Explainability Monitoring System

```yaml
# explainability-monitoring.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: explainability-alerts
  namespace: monitoring
spec:
  groups:
  - name: explainability.rules
    rules:
    # Feature importance change alert
    - alert: FeatureImportanceDrift
      expr: |
        abs(
          rate(feature_importance_shap[1h]) - 
          rate(feature_importance_baseline[1h])
        ) > 0.1
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: \"Feature importance drift detected\"
        description: \"SHAP feature importance has drifted significantly in the last hour\"
    
    # Prediction distribution change alert
    - alert: PredictionDistributionShift
      expr: |
        histogram_quantile(0.95, sum(rate(prediction_confidence_bucket[1h])) by (le))
        - 
        histogram_quantile(0.95, sum(rate(baseline_prediction_confidence_bucket[1h])) by (le))
        > 0.2
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: \"Prediction distribution shift detected\"
        description: \"Model prediction confidence distribution has shifted significantly\"
    
    # Fairness violation alarm
    - alert: FairnessViolation
      expr: |
        disparate_impact_ratio < 0.8 or disparate_impact_ratio > 1.2
      for: 30m
      labels:
        severity: critical
      annotations:
        summary: \"Fairness constraint violation\"
        description: \"Model disparate impact ratio {{ $value }} violates fairness constraints\"
    
    # Explanation of availability alert
    - alert: ExplainabilityServiceDown
      expr: |
        up{job=\"explainability-api\"} == 0
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: \"Explainability service is down\"
        description: \"Model explanation API service is not responding\"

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: explainability-dashboard
  namespace: monitoring
data:
  dashboard.json: |
    {
      \"dashboard\": {
        \"title\": \"Model Explainability Monitoring\",
        \"panels\": [
          {
            \"title\": \"Top Feature Importance\",
            \"type\": \"barchart\",
            \"targets\": [
              {
                \"expr\": \"topk(10, feature_importance_shap)\",
                \"legendFormat\": \"{{feature}}\"
              }
            ]
          },
          {
            \"title\": \"SHAP Value Distribution\",
            \"type\": \"heatmap\",
            \"targets\": [
              {
                \"expr\": \"shap_values_histogram\",
                \"legendFormat\": \"SHAP Values\"
              }
            ]
          },
          {
            \"title\": \"Disparate Impact Ratio\",
            \"type\": \"graph\",
            \"targets\": [
              {
                \"expr\": \"disparate_impact_ratio\",
                \"legendFormat\": \"Current\"
              },
              {
                \"expr\": \"1\",
                \"legendFormat\": \"Ideal (1.0)\"
              },
              {
                \"expr\": \"0.8\",
                \"legendFormat\": \"Lower Threshold\"
              },
              {
                \"expr\": \"1.2\",
                \"legendFormat\": \"Upper Threshold\"
              }
            ]
          },
          {
            \"title\": \"Explanation Response Time\",
            \"type\": \"graph\",
            \"targets\": [
              {
                \"expr\": \"histogram_quantile(0.95, sum(rate(explanation_duration_seconds_bucket[5m])) by (le))\",
                \"legendFormat\": \"95th Percentile\"
              },
              {
                \"expr\": \"histogram_quantile(0.50, sum(rate(explanation_duration_seconds_bucket[5m])) by (le))\",
                \"legendFormat\": \"Median\"
              }
            ]
          }
        ]
      }
    }
```

### 4.2 Automated Explainability Reports

```python
# automated_explainability_report.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import jinja2
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class ExplainabilityReporter:
    def __init__(self, model_name, data_source):
        self.model_name = model_name
        self.data_source = data_source
        self.report_date = datetime.now()
        
    def generate_weekly_report(self):
        \"\"\"Generate weekly explainability report\"\"\"
        # Collect data
        weekly_data = self._collect_weekly_data()
        
        # Generate analysis results
        analysis_results = self._perform_analysis(weekly_data)
        
        # Create report
        report_html = self._create_report_template(analysis_results)
        
        # Generate PDF
        pdf_path = f'/reports/{self.model_name}_explainability_report_{self.report_date.strftime(\"%Y%m%d\")}.pdf'
        pdfkit.from_string(report_html, pdf_path)
        
        # Send report
        self._send_report(pdf_path)
        
        return pdf_path
    
    def _collect_weekly_data(self):
        \"\"\"Collect data for a week\"\"\"
        # Retrieve data from monitoring system (simplified to simulated data)
        # Here simplified to simulated data
        data = {
            'feature_importance': self._get_feature_importance_data(),
            'prediction_distribution': self._get_prediction_distribution(),
            'fairness_metrics': self._get_fairness_metrics(),
            'explanation_requests': self._get_explanation_stats()
        }
        return data
    
    def _perform_analysis(self, data):
        "\"\"\"Perform analysis\"\"\""
        analysis = {}
        
        # Feature importance analysis
        importance_df = pd.DataFrame(data['feature_importance'])
        analysis['top_features'] = importance_df.head(10).to_dict('records')
        analysis['importance_changes'] = self._calculate_importance_changes(importance_df)
        
        # Fairness analysis
        fairness_df = pd.DataFrame(data['fairness_metrics'])
        analysis['fairness_summary'] = fairness_df.describe().to_dict()
        analysis['fairness_alerts'] = self._detect_fairness_issues(fairness_df)
        
        # Performance analysis
        analysis['explanation_performance'] = data['explanation_requests']
        
        return analysis
    
    def _create_report_template(self, analysis_results):
        "\"\"\"Create report template\"\"\""
        template_str = \"\"\"
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ model_name }} Explainability Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .header { background-color: #f0f0f0; padding: 20px; border-radius: 5px; }
                .section { margin: 20px 0; }
                .chart { margin: 10px 0; }
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <div class=\"header\">
                <h1>{{ model_name }} Explainability Report</h1>
                <p>Generated on: {{ report_date }}</p>
            </div>
            
            <div class=\"section\">
                <h2>Executive Summary</h2>
                <ul>
                    <li>Total explanation requests: {{ analysis.explanation_performance.total_requests }}</li>
                    <li>Average response time: {{ analysis.explanation_performance.avg_response_time }}ms</li>
                    <li>Fairness violations detected: {{ analysis.fairness_alerts|length }}</li>
                </ul>
            </div>
            
            <div class=\"section\">
                <h2>Top Feature Importance</h2>
                <table>
                    <tr><th>Feature</th><th>Importance</th><th>Change</th></tr>
                    {% for feature in analysis.top_features %}
                    <tr>
                        <td>{{ feature.feature }}</td>
                        <td>{{ \"%.4f\"|format(feature.importance) }}</td>
                        <td>{{ \"%.4f\"|format(feature.change) }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
            
            <div class=\"section\">
                <h2>Fairness Analysis</h2>
                {% if analysis.fairness_alerts %}
                <div style=\"color: red;\">
                    <h3>⚠️ Fairness Issues Detected</h3>
                    <ul>
                    {% for alert in analysis.fairness_alerts %}
                        <li>{{ alert }}</li>
                    {% endfor %}
                    </ul>
                </div>
                {% else %}
                <p style=\"color: green;\">✅ No fairness violations detected</p>
                {% endif %}
            </div>
        </body>
        </html>
        \"\"\"
        
        template = jinja2.Template(template_str)
        return template.render(
            model_name=self.model_name,
            report_date=self.report_date.strftime('%Y-%m-%d'),
            analysis=analysis_results
        )
    
    def _send_report(self, pdf_path):
        "\"\"\"Send report\"\"\""
        # Email configuration
        msg = MIMEMultipart()
        msg['From'] = 'ml-governance@company.com'
        msg['To'] = 'stakeholders@company.com'
        msg['Subject'] = f'{self.model_name} Explainability Report - {self.report_date.strftime(\"%Y-%m-%d\")}'
        
        # Email body
        body = f\"\"\"Dear Stakeholders,

Please find attached the weekly explainability report for {self.model_name}.

Key highlights:
- Feature importance analysis completed
- Fairness metrics reviewed
- Performance benchmarks assessed

Best regards,
ML Governance Team
        \"\"\"
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach PDF report
        with open(pdf_path, \"rb\") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {pdf_path.split(\"/\")[-1]}'
        )
        msg.attach(part)
        
        # Send email (SMTP configuration required for actual use)
        # server = smtplib.SMTP('smtp.company.com', 587)
        # server.starttls()
        # server.login('ml-governance@company.com', 'password')
        # server.send_message(msg)
        # server.quit()

# Usage Example
reporter = ExplainabilityReporter(
    model_name='customer_churn_model',
    data_source='production_logs'
)

report_path = reporter.generate_weekly_report()
print(f\"Report generated: {report_path}\")
```

---

**Maintainer**: AI Ethics Team | **Last Updated**: 2026-02 | **Version**: v1.0

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Framework
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 31-ai-platform-governance
- 32-mlops-pipeline
- 34-federated-learning
- 35-model-drift-monitoring


<!-- risk-assessed -->
