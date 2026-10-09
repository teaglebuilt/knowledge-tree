---
title: Agent Harness Verification and Gatekeeping (domain-14-ai-ml-infra)
description: 'description: '**Document Type**: Deep Dive Harness Engineering | **Last Updated**: 2026-04 | **Keywords**:'
  Verification,'
summary: 'summary: 'description: '**Document Type**: Deep Dive Harness Engineering | **Last Updated**: 2026-04 | **Keywords**: Verification,''
category: general
tags:
- ai
- ai-agent
- etcd
- helm
- docker
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 35min
intent_queries:
- What is Agent Harness Verification and Gatekeeping
- How to do Agent Harness Verification and Gatekeeping
- Best Practices for Agent Harness in Kubernetes 14 AI ML Infra
trigger_keywords:
- Agent
- Harness
- What is Verification and Gatekeeping
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- etcd-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/34-agent-harness-verification-quality.md
---

> **Production Environment Security Reminders**
>
> Commands contained herein are executable directly for operational purposes. Execute at your own risk: confirm that the target cluster and namespace are correct; ensure you have sufficient RBAC permissions; verify these commands in a non-production environment first. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but can usually be rolled back), 🟢 Low Risk/ReadOnly (information gathering with no side effects).




title: Agent Harness Validation and Quality Gate
description: '**Document Type**: Deep Dive into Harness Engineering | **Last Updated**: 2026-04 | **Keywords**: Verification,
  Quality Gate, Self-check Loop, LLM-as-Judge, RAGAS, Phantom Detection, Factuality Consistency, CI/CD, Regression Testing, Gray Release'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- [[Helm|helm]]
- docker
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is Agent Harness Validation and Quality Gate
- How to perform Agent Harness Validation and Quality Gate
trigger_keywords:
- Agent
- Harness
- Validation and Quality Gate
- ai
- agent
authors:
- name: Dillan Teagle
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# Agent Harness Validation and Quality Gates

> **Document Type**: Deep Dive into Harness Engineering | **Last Updated**: 2026-04 | **Keywords**: Verification, Quality Gate, Self-check Loop, LLM-as-Judge, RAGAS, Phantom Detection, Factuality Consistency, CI/CD, Regression Testing, Gray Release

---

## Overview

Verification (verification layer) is the fifth layer of the six-layer architecture of Agent Harness, also the key demarcation point that sets it apart from "bare Agent" in Harness. Experiments with LangChain show that adding a self-check loop alone increased the baseline score by 13.7%—this is the most efficient single change among all Harness improvements.

This document comprehensively explores multi-dimensional validation strategies for the verification layer, the LLM-as-Judge evaluation paradigm, the RAGAS evaluation framework integration, CI/CD quality gates, A/B testing and gray release, and the design of custom validators tailored for Kubernetes operational scenarios.

---

## 1. Core Theories of the Validation Layer

## 1.1 Why Validation is the Highest ROI Improvement for Harness

```
validate layer ROI empirical data:

LangChain encoding Agent (February 2026 experiment):
  no validation:      baseline score 52.8%
  add self-check loop: baseline score 66.5%  → +13.7% absolute improvement
  
  improvement breakdown:
    self-check loop:    +13.7% (highest single improvement)
    pre-environment scan: +5.2%
    drift detection:     +3.8%
    inference budget optimization: +2.5%

Anthropic long-running Agent:
  no validation:       task completion rate 71%
  with validation:     task completion rate 89%  → +18% absolute improvement
  
  types of validation intercept issues:
    - hallucination output: 40% of intercepted issues
    - format errors:        25% of intercepted issues
    - logical inconsistency: 20% of intercepted issues
    - security risks:       15% of intercepted issues
```

## 1.2 Classification System of Validations

```
Agent output verification classification:

1. factual verification (Factual Verification)
   are the facts in the output consistent with the context/evidence
   Tool: LLM-as-Judge, RAGAS Faithfulness

2. Format Verification
   Is the YAML/JSON/command output syntactically correct?
   Tool: Syntax parser, Schema validation

3. Safety Verification
   Is the command/operation safe?
   Tool: Regular expression matching, Command whitelist

4. Completeness Verification
   Is the output fully addressing all parts of the question?
   Tool: LLM-as-Judge, Checklist

5. Consistency Verification
   Are the parts of the output logically consistent?
   Tool: LLM-as-Judge, Rule engine

6. Executability Verification
   Is the proposed solution executable in the current environment?
   Tool: Dry-run, Environment check
```

---

## 2. Design of Multi-Dimensional Validator

## 2.1 Validator Framework

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Any
from enum import Enum

class VerificationSeverity(Enum):
    """validate severity of issues"""
    INFO = "info"           # 信息提示
    WARNING = "warning"     # 警告（不阻塞）
    ERROR = "error"         # 错误（阻塞输出）
    CRITICAL = "critical"   # 严重（立即终止）

@dataclass
class VerificationResult:
    """single validation result"""
    verifier: str
    passed: bool
    severity: VerificationSeverity = VerificationSeverity.INFO
    message: str = ""
    details: list = field(default_factory=list)
    score: float = 1.0       # 0.0 - 1.0
    fix_suggestion: str = ""  # 修复建议

@dataclass
class VerificationReport:
    """complete validation report"""
    overall_passed: bool
    results: list[VerificationResult]
    total_score: float
    blocking_issues: list[VerificationResult]
    warnings: list[VerificationResult]

    @classmethod
    def from_results(cls, results: list[VerificationResult]) -> 'VerificationReport':
        blocking = [r for r in results if not r.passed
                    and r.severity in (VerificationSeverity.ERROR,
                                      VerificationSeverity.CRITICAL)]
        warnings = [r for r in results if not r.passed
                    and r.severity == VerificationSeverity.WARNING]
        scores = [r.score for r in results]
        avg_score = sum(scores) / len(scores) if scores else 0

        return cls(
            overall_passed=len(blocking) == 0,
            results=results,
            total_score=avg_score,
            blocking_issues=blocking,
            warnings=warnings,
        )


class BaseVerifier(ABC):
    """validation base class"""

    @abstractmethod
    def verify(self, task: str, output: str, context: dict) -> VerificationResult:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...


class VerificationPipeline:
    """validation pipeline: orchestrate multiple validators"""

    def __init__(self, verifiers: list[BaseVerifier] = None):
        self.verifiers = verifiers or []

    def add_verifier(self, verifier: BaseVerifier):
        self.verifiers.append(verifier)

    def verify_all(self, task: str, output: str, context: dict) -> VerificationReport:
        """run all validators"""
        results = []
        for verifier in self.verifiers:
            try:
                result = verifier.verify(task, output, context)
                results.append(result)

                # CRITICAL terminate the issue immediately
                if (not result.passed
                        and result.severity == VerificationSeverity.CRITICAL):
                    break
            except Exception as e:
                results.append(VerificationResult(
                    verifier=verifier.name,
                    passed=False,
                    severity=VerificationSeverity.WARNING,
                    message=f"Validation error: {e}",
                ))

        return VerificationReport.from_results(results)
```

## 2.2 Fact Consistency Validator

```python
class FactualConsistencyVerifier(BaseVerifier):
    """fact consistency validation: ensure output aligns with contextual evidence"""

    def __init__(self, judge_llm, threshold: float = 0.85):
        self.judge_llm = judge_llm
        self.threshold = threshold

    @property
    def name(self) -> str:
        return "factual_consistency"

    def verify(self, task: str, output: str, context: dict) -> VerificationResult:
        sources = context.get("sources", "")
        evidence = context.get("evidence", "")

        prompt = f"""
你是一个事实一致性审查员。请严格评估以下回答是否与给定的证据/上下文一致。

## task
{task}

## context/evidence
{sources[:3000]}
{evidence[:2000]}

## agent's response
{output[:3000]}

## evaluation requirements
1. 检查回答中的每一个事实性声明
2. 判断每个声明是否有上下文支撑
3. 识别任何幻觉（无依据的声明）

## output format (JSON)
{{
    "consistent": true/false,
    "score": 0.0-1.0,
    "unsupported_claims": ["unsupported claims1", "..."],
    "hallucinations": ["hallucinated content1", "..."],
    "missing_evidence": ["referenced evidence but not cited1", "..."],
}}
"""
        result = self.judge_llm.invoke(prompt)
        parsed = self._parse_json(result)

        score = parsed.get("score", 0)
        passed = score >= self.threshold

        return VerificationResult(
            verifier=self.name,
            passed=passed,
            severity=VerificationSeverity.ERROR if not passed
                     else VerificationSeverity.INFO,
            message=f"Fact consistency score: {score:.2f}",
            score=score,
            details=parsed.get("hallucinations", []),
            fix_suggestion="Please correct the following hallucinated content based on specific evidence within the context: "
                          + "; ".join(parsed.get("hallucinations", [])),
        )

    def _parse_json(self, text: str) -> dict:
        import json, re
        match = re.search(r'\{[\s\S]*\}', text)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return {"consistent": False, "score": 0.0}
```

## 2.3 Command Security Validator

```python
import re

class CommandSafetyVerifier(BaseVerifier):
    """command security validation: intercept dangerous commands"""

    DANGER_LEVELS = {
        "critical": [
            r"kubectl\s+delete\s+(?:namespace|ns|node)",
            r"kubectl\s+delete\s+--all",
            r"rm\s+-rf\s+/",
            r"DROP\s+(?:TABLE|DATABASE)",
            r"kubectl\s+drain\s+.*--force.*--delete-emptydir-data",
            r"etcdctl\s+del",
        ],
        "high": [
            r"kubectl\s+delete\s+(?:deploy|sts|ds|svc)",
            r"kubectl\s+drain",
            r"kubectl\s+cordon",
            r"helm\s+(?:uninstall|delete)",
            r"kubectl\s+scale.*replicas=0",
        ],
        "medium": [
            r"kubectl\s+(?:apply|patch|edit)",
            r"kubectl\s+rollout\s+undo",
            r"helm\s+(?:upgrade|install)",
            r"kubectl\s+label.*--overwrite",
        ],
    }

    @property
    def name(self) -> str:
        return "command_safety"

    def verify(self, task: str, output: str, context: dict) -> VerificationResult:
        commands = self._extract_commands(output)
        if not commands:
            return VerificationResult(
                verifier=self.name, passed=True,
                message="No command detected", score=1.0,
            )

        issues = []
        max_severity = VerificationSeverity.INFO

        for cmd in commands:
            for level, patterns in self.DANGER_LEVELS.items():
                for pattern in patterns:
                    if re.search(pattern, cmd, re.IGNORECASE):
                        severity = {
                            "critical": VerificationSeverity.CRITICAL,
                            "high": VerificationSeverity.ERROR,
                            "medium": VerificationSeverity.WARNING,
                        }[level]

                        issues.append({
                            "command": cmd,
                            "danger_level": level,
                            "pattern": pattern,
                        })

                        if severity.value > max_severity.value:
                            max_severity = severity

        passed = max_severity in (VerificationSeverity.INFO,
                                   VerificationSeverity.WARNING)

        return VerificationResult(
            verifier=self.name,
            passed=passed,
            severity=max_severity,
            message=f"Detected {len(issues)} security issues" if issues else "Command security check passed",
            details=issues,
            score=1.0 - len(issues) * 0.2,
            fix_suggestion="Replace dangerous commands with read-only commands or add the --dry-run flag",
        )

    def _extract_commands(self, text: str) -> list:
        """extract commands from text"""
        commands = []
        # extract commands from code blocks
        code_blocks = re.findall(r'```(?:bash|shell|sh)?\n(.*?)```',
                                 text, re.DOTALL)
        for block in code_blocks:
            for line in block.strip().split("\n"):
                line = line.strip()
                if line and not line.startswith("#"):
                    commands.append(line)

        # extract inline commands
        inline_cmds = re.findall(r'`((?:kubectl|helm|etcdctl|docker)\s+[^`]+)`',
                                 text)
        commands.extend(inline_cmds)

        return commands
```

## 2.4 Output Format Validator

```python
import yaml
import json as json_module

class OutputFormatVerifier(BaseVerifier):
    """output format validation: ensure YAML/JSON syntax is correct"""

    @property
    def name(self) -> str:
        return "output_format"

    def verify(self, task: str, output: str, context: dict) -> VerificationResult:
        issues = []

        # validate YAML block
        yaml_blocks = re.findall(r'```yaml\n(.*?)```', output, re.DOTALL)
        for i, block in enumerate(yaml_blocks):
            try:
                parsed = yaml.safe_load(block)
                if parsed is None:
                    issues.append({
                        "type": "yaml", "block": i,
                        "error": "YAML parsing result is empty",
                    })
            except yaml.YAMLError as e:
                issues.append({
                    "type": "yaml", "block": i,
                    "error": str(e)[:200],
                    "content_preview": block[:100],
                })

        # validate JSON block
        json_blocks = re.findall(r'```json\n(.*?)```', output, re.DOTALL)
        for i, block in enumerate(json_blocks):
            try:
                json_module.loads(block)
            except json_module.JSONDecodeError as e:
                issues.append({
                    "type": "json", "block": i,
                    "error": str(e)[:200],
                })

        # Validate kubectl command syntax
        kubectl_cmds = re.findall(r'`(kubectl\s+[^`]+)`', output)
        for cmd in kubectl_cmds:
            cmd_issues = self._validate_kubectl_syntax(cmd)
            issues.extend(cmd_issues)

        passed = len(issues) == 0
        return VerificationResult(
            verifier=self.name,
            passed=passed,
            severity=VerificationSeverity.ERROR if not passed
                     else VerificationSeverity.INFO,
            message=f"Found {len(issues)} format issues" if issues else "Format check passed",
            details=issues,
            score=max(0, 1.0 - len(issues) * 0.15),
            fix_suggestion="Fix YAML/JSON syntax errors",
        )

    def _validate_kubectl_syntax(self, cmd: str) -> list:
        """Basic kubectl command syntax check"""
        issues = []
        parts = cmd.split()
        if len(parts) < 2:
            issues.append({"type": "kubectl", "error": "command incomplete",
                          "command": cmd})
            return issues

        valid_verbs = {"get", "describe", "logs", "top", "apply", "delete",
                       "patch", "scale", "rollout", "exec", "explain",
                       "create", "edit", "label", "annotate", "drain",
                       "cordon", "uncordon", "taint", "events"}
        verb = parts[1]
        if verb not in valid_verbs:
            issues.append({"type": "kubectl", "error": f"Unknown subcommand: {verb}",
                          "command": cmd})

        return issues
```

## 2.5 Integrity Validator

```python
class CompletenessVerifier(BaseVerifier):
    """Completeness verification: Ensure the response covers all aspects of the question"""

    def __init__(self, judge_llm):
        self.judge_llm = judge_llm

    @property
    def name(self) -> str:
        return "completeness"

    def verify(self, task: str, output: str, context: dict) -> VerificationResult:
        prompt = f"""
评估以下回答是否完整地回应了任务要求。

## Task
{task}

## Answer
{output[:3000]}

## Evaluation Criteria
1. 是否直接回答了核心问题
2. 是否提供了具体的操作步骤
3. 是否包含必要的前置条件和注意事项
4. 是否遗漏了关键信息

## Output Format (JSON)
{{
    "complete": true/false,
    "score": 0.0-1.0,
    "covered_aspects": ["covered aspects1", "..."],
    "missing_aspects": ["missing aspects1", "..."],
    "improvement_suggestions": ["improvement suggestions1", "..."],
}}
"""
        result = self.judge_llm.invoke(prompt)
        parsed = self._parse_json(result)

        score = parsed.get("score", 0)
        passed = score >= 0.7

        return VerificationResult(
            verifier=self.name,
            passed=passed,
            severity=VerificationSeverity.WARNING if not passed
                     else VerificationSeverity.INFO,
            message=f"Integrity score: {score:.2f}",
            score=score,
            details=parsed.get("missing_aspects", []),
            fix_suggestion="Add the following missing content: "
                          + "; ".join(parsed.get("missing_aspects", [])),
        )

    def _parse_json(self, text: str) -> dict:
        import json
        match = re.search(r'\{[\s\S]*\}', text)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return {"complete": False, "score": 0.0}
```

---

## 3. Self-Inspection Loop Pattern

## 3.1 Implementation of Self-Inspection Loop

```python
class SelfCheckLoop:
    """Self-check loop: Agent runs the checklist automatically after completion"""

    def __init__(
        self,
        verification_pipeline: VerificationPipeline,
        max_correction_rounds: int = 2,
        llm=None,
    ):
        self.pipeline = verification_pipeline
        self.max_rounds = max_correction_rounds
        self.llm = llm

    def verify_and_correct(
        self,
        task: str,
        output: str,
        context: dict,
    ) -> dict:
        """Validate and self-correct"""
        correction_history = []

        for round_num in range(self.max_rounds + 1):
            # Run validation
            report = self.pipeline.verify_all(task, output, context)

            correction_history.append({
                "round": round_num,
                "output_preview": output[:200],
                "passed": report.overall_passed,
                "score": report.total_score,
                "issues": len(report.blocking_issues),
            })

            # Validation passed
            if report.overall_passed:
                return {
                    "status": "passed",
                    "output": output,
                    "report": report,
                    "correction_rounds": round_num,
                    "history": correction_history,
                }

            # Reached maximum correction rounds
            if round_num >= self.max_rounds:
                return {
                    "status": "failed_after_corrections",
                    "output": output,
                    "report": report,
                    "correction_rounds": round_num,
                    "history": correction_history,
                    "unresolved_issues": [
                        {"verifier": r.verifier, "message": r.message}
                        for r in report.blocking_issues
                    ],
                }

            # Self-correct
            output = self._self_correct(task, output, report, context)

        return {"status": "max_rounds_exceeded", "output": output,
                "history": correction_history}

    def _self_correct(
        self,
        task: str,
        output: str,
        report: VerificationReport,
        context: dict,
    ) -> str:
        """Make the LLM self-correct based on validation feedback"""
        issues_text = "\n".join([
            f"- [{r.verifier}] {r.message}\n  Fix suggestion: {r.fix_suggestion}"
            for r in report.blocking_issues + report.warnings
        ])

        correction_prompt = f"""
你之前的回答存在以下问题，请修正后重新输出。

## Original Task
{task}

## Your Previous Answer
{output[:3000]}

## Issues Found During Verification
{issues_text}

## Requirements
1. 保留正确的部分
2. 修正上述问题
3. 确保 YAML/JSON 语法正确
4. 确保命令安全可执行
5. 确保事实有证据支撑

请直接输出修正后的完整回答，不要包含任何解释。
"""
        corrected = self.llm.invoke(correction_prompt)
        return corrected
```

## 3.2 Self-Inspection Checklist Template

```python
class DiagnosisChecklist:
    """K8S diagnostic output self-checklist"""

    CHECKLIST = [
        {"id": "root_cause", "question": "Is the root cause analysis clearly specified?",
         "required": True},
        {"id": "evidence", "question": "Is the root cause conclusion supported by specific Event/log evidence?",
         "required": True},
        {"id": "commands_safe", "question": "Are the commands safe to execute?",
         "required": True},
        {"id": "yaml_valid", "question": "Is the YAML/JSON syntax correct?",
         "required": True},
        {"id": "steps_complete", "question": "Are the operation steps complete and executable?",
         "required": True},
        {"id": "risk_assessed", "question": "Has the operation risk level been assessed?",
         "required": False},
        {"id": "rollback_plan", "question": "Is there a rollback plan provided?",
         "required": False},
        {"id": "confidence", "question": "Is the diagnostic confidence marked?",
         "required": False},
    ]

    def evaluate(self, output: str, context: dict) -> dict:
        """Evaluate the output according to the checklist"""
        results = []
        for item in self.CHECKLIST:
            met = self._check_item(item, output)
            results.append({
                "id": item["id"],
                "question": item["question"],
                "met": met,
                "required": item["required"],
            })

        required_met = all(r["met"] for r in results if r["required"])
        total_met = sum(1 for r in results if r["met"])
        score = total_met / len(results)

        return {
            "passed": required_met,
            "score": score,
            "checklist_results": results,
            "missing_required": [
                r["question"] for r in results
                if r["required"] and not r["met"]
            ],
        }

    def _check_item(self, item: dict, output: str) -> bool:
        """Check Single (Quick Check Based on Keywords)"""
        checks = {
            "root_cause": lambda o: any(kw in o for kw in ["root cause", "cause", "reason"]),
            "evidence": lambda o: any(kw in o for kw in ["Event", "log", "evidence", "proof"]),
            "commands_safe": lambda o: "delete" not in o.lower() or "--dry-run" in o,
            "yaml_valid": lambda o: self._check_yaml_blocks(o),
            "steps_complete": lambda o: any(kw in o for kw in ["operation", "step", "procedure"]),
            "risk_assessed": lambda o: any(kw in o for kw in ["risk", "risk assessment", "impact"]),
            "rollback_plan": lambda o: any(kw in o for kw in ["rollback", "recovery", "restoration"]),
            "confidence": lambda o: any(kw in o for kw in ["confidence", "certainty", "assurance", "%"]),
        }
        checker = checks.get(item["id"], lambda o: True)
        return checker(output)

    def _check_yaml_blocks(self, output: str) -> bool:
        yaml_blocks = re.findall(r'```yaml\n(.*?)```', output, re.DOTALL)
        for block in yaml_blocks:
            try:
                yaml.safe_load(block)
            except yaml.YAMLError:
                return False
        return True
```

---

## 4. LLM-as-Judge Evaluation Paradigm

## 4.1 Strategy for Selecting Judge Models

```
LLM-as-Judge model selection:

Principle: The Judge model must be different from the generation model (to avoid homogenization bias)

Recommended configuration:
  Generation model         Judge model          Applicable scenarios
  GPT-4o           Claude Sonnet 4     General judgment
  Claude Sonnet 4  GPT-4o              General judgment
  GPT-4o-mini      GPT-4o              cost-sensitive scenarios
  Gemini 2.5       Claude Sonnet 4     Cross-vendor assessment
  any open-source model     GPT-4o              Open-source model evaluation

Assessment dimensions and weights:
  Faithfulness (faithfulness):     weight 30%
  Relevancy (relevance):       weight 25%
  Completeness (completeness):    weight 20%
  Safety (safety):          weight 15%
  Format (format correctness):      weight 10%
```

## 4.2 Implementation of Judge Evaluators

```python
class LLMJudge:
    """LLM-as-Judge Evaluator"""

    def __init__(self, judge_llm, dimensions: dict = None):
        self.judge = judge_llm
        self.dimensions = dimensions or {
            "faithfulness": 0.30,
            "relevancy": 0.25,
            "completeness": 0.20,
            "safety": 0.15,
            "format": 0.10,
        }

    def evaluate(self, task: str, output: str, context: dict) -> dict:
        """Multi-dimensional Evaluation"""
        prompt = f"""
你是一个专业的 AI 输出质量评估员。请严格按照以下维度评估 Agent 的回答。

## Task
{task}

## Context/Evidence
{context.get('sources', '')[:3000]}

## Agent's Response
{output[:4000]}

## Evaluation Dimensions

## 1. Faithfulness (Faithfulness) 0-10 Points
回答中的每个事实是否都有上下文支撑？是否存在幻觉？

## 2. Relevancy (Relevancy) 0-10 Points
回答是否直接针对了提出的问题？是否偏离主题？

## 3. Completeness (Completeness) 0-10 Points
回答是否覆盖了问题的所有方面？是否有遗漏？

## 4. Safety (Safety) 0-10 Points
给出的命令/操作是否安全？是否存在风险操作未被标注？

## 5. Format (Format Correctness) 0-10 Points
YAML/JSON 语法是否正确？命令格式是否规范？

## Output Format (JSON)
{{
    "faithfulness": {{"score": 0-10, "reasoning": "..."}},
    "relevancy": {{"score": 0-10, "reasoning": "..."}},
    "completeness": {{"score": 0-10, "reasoning": "..."}},
    "safety": {{"score": 0-10, "reasoning": "..."}},
    "format": {{"score": 0-10, "reasoning": "..."}},
    "overall_assessment": "Overall assessment",
    "key_issues": ["Key issue 1", "..."]
}}
"""
        result = self.judge.invoke(prompt)
        parsed = self._parse_json(result)

        # Calculate Weighted Total Score
        weighted_score = 0
        for dim, weight in self.dimensions.items():
            dim_score = parsed.get(dim, {}).get("score", 0) / 10.0
            weighted_score += dim_score * weight

        return {
            "dimensions": parsed,
            "weighted_score": weighted_score,
            "passed": weighted_score >= 0.7,
            "key_issues": parsed.get("key_issues", []),
        }

    def _parse_json(self, text: str) -> dict:
        import json
        match = re.search(r'\{[\s\S]*\}', text)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return {}
```

---

## 5. Integration of RAGAS Evaluation Framework

## 5.1 RAGAS Indicator System

```
RAGAS Core Indicators:

1. Faithfulness(faithfulness)
   Measure:  Whether the generated answer is consistent with the retrieved context
   Calculation: Each statement in the answer → Check if there is supporting content in the context
   Threshold: > 0.85

2. Answer Relevancy(answer relevance)
   Measure:  Whether the answer directly responds to the question
   Calculation: Generate a question from the answer → Calculate similarity with the original question
   Threshold: > 0.80

3. Context Precision(Context Precision)
   Measured: Are all retrieved contexts relevant?
   Calculate: relevant context / total search context
   Threshold: > 0.70

4. Context Recall(Context Recall)
   Measure: Did we retrieve all the contextual information needed to answer the question?
   Calculate: The context required for the answer / The actual context to be retrieved
   Threshold: > 0.75
```

## 5.2 Implementation of RAGAS Integration

```python
class RAGASEvaluator:
    """RAGAS Integration Evaluation"""

    def __init__(self, llm, embeddings):
        self.llm = llm
        self.embeddings = embeddings

    def evaluate(
        self,
        question: str,
        answer: str,
        contexts: list[str],
        ground_truth: str = None,
    ) -> dict:
        """Run RAGAS Evaluation"""
        results = {}

        # Faithfulness
        results["faithfulness"] = self._evaluate_faithfulness(
            answer, contexts
        )

        # Answer Relevancy
        results["answer_relevancy"] = self._evaluate_relevancy(
            question, answer
        )

        # Context Precision
        results["context_precision"] = self._evaluate_context_precision(
            question, contexts
        )

        # Context Recall (needs ground truth)
        if ground_truth:
            results["context_recall"] = self._evaluate_context_recall(
                ground_truth, contexts
            )

        # Overall Score
        scores = [v["score"] for v in results.values()]
        results["overall"] = sum(scores) / len(scores)

        return results

    def _evaluate_faithfulness(self, answer: str, contexts: list) -> dict:
        """Evaluate Faithfulness"""
        # Step 1: Extract Statements from the Answer
        claims = self._extract_claims(answer)

        # Step 2: Verify support for each declaration
        supported = 0
        details = []
        context_text = "\n".join(contexts)

        for claim in claims:
            is_supported = self._check_claim_support(claim, context_text)
            if is_supported:
                supported += 1
            details.append({"claim": claim, "supported": is_supported})

        score = supported / len(claims) if claims else 1.0
        return {"score": score, "total_claims": len(claims),
                "supported_claims": supported, "details": details}

    def _evaluate_relevancy(self, question: str, answer: str) -> dict:
        """Evaluate relevance of answers"""
        # Generate questions from answers and compare similarity to original
        generated_questions = self._generate_questions_from_answer(answer, n=3)
        similarities = []
        q_embedding = self.embeddings.encode(question)

        for gq in generated_questions:
            gq_embedding = self.embeddings.encode(gq)
            sim = self._cosine_similarity(q_embedding, gq_embedding)
            similarities.append(sim)

        score = sum(similarities) / len(similarities) if similarities else 0
        return {"score": score, "generated_questions": generated_questions}

    def _evaluate_context_precision(self, question: str,
                                     contexts: list) -> dict:
        """Evaluate context accuracy"""
        relevant_count = 0
        for ctx in contexts:
            if self._is_context_relevant(question, ctx):
                relevant_count += 1
        score = relevant_count / len(contexts) if contexts else 0
        return {"score": score, "relevant": relevant_count,
                "total": len(contexts)}

    def _extract_claims(self, answer: str) -> list:
        prompt = f"Decompose the following text into independent fact-based statements list:\n\n{answer[:2000]}\n\nOutput JSON array: [\"Statement1\", \"Statement2\", ...]"
        result = self.llm.invoke(prompt)
        try:
            return json.loads(result)
        except:
            return [answer[:200]]

    def _check_claim_support(self, claim: str, context: str) -> bool:
        prompt = f"Does the following statement have contextual support? Only answer yes or no.\nStatement: {claim}\nContext: {context[:2000]}"
        result = self.llm.invoke(prompt).strip().lower()
        return "yes" in result

    def _cosine_similarity(self, a, b) -> float:
        import numpy as np
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
```

---

## 6. CI/CD Quality Gates

## 6.1 Quality Gate Configuration

```yaml
# harness-quality-gate.yaml
quality_gate:
  # Hard gating (block merge if fails)
  hard_gates:
    faithfulness:
      min: 0.85
      description: "Minimum threshold for fact consistency"
    command_safety:
      min: 1.0
      description: "Command safety must be 100%"
    hallucination_rate:
      max: 0.05
      description: "Maximum hallucination rate 5%"
    task_completion_rate:
      min: 0.90
      description: "Minimum task completion rate 90%"

  # Soft gating (warn if fails)
  soft_gates:
    answer_relevancy:
      min: 0.80
      description: "Suggested threshold for relevance of answers"
    completeness:
      min: 0.75
      description: "Suggested threshold for completeness"
    avg_steps_ratio:
      max: 1.5
      description: "Efficiency ratio (relative optimal path)"

  # Regression detection
  regression:
    enabled: true
    tolerance: 0.02        # 允许 2% 波动
    baseline_path: "reports/baseline.json"
    metrics:
      - faithfulness
      - task_completion_rate
      - answer_relevancy
```

## 6.2 Quality Gate Inspector

```python
import json
import sys
from dataclasses import dataclass

@dataclass
class GateResult:
    metric: str
    threshold: float
    actual: float
    passed: bool
    is_hard: bool
    is_regression: bool = False

class QualityGateChecker:
    """Harness Quality Gate Checker"""

    def __init__(self, config_path: str):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)["quality_gate"]

    def check(self, report_path: str, baseline_path: str = None) -> dict:
        """Run Quality Gate Checker"""
        with open(report_path) as f:
            report = json.load(f)

        results: list[GateResult] = []

        # Check hard gating
        for metric, gate in self.config.get("hard_gates", {}).items():
            if metric not in report:
                continue
            actual = report[metric]
            if "min" in gate:
                passed = actual >= gate["min"]
                threshold = gate["min"]
            else:
                passed = actual <= gate["max"]
                threshold = gate["max"]
            results.append(GateResult(
                metric=metric, threshold=threshold,
                actual=actual, passed=passed, is_hard=True,
            ))

        # Check soft gating
        for metric, gate in self.config.get("soft_gates", {}).items():
            if metric not in report:
                continue
            actual = report[metric]
            if "min" in gate:
                passed = actual >= gate["min"]
                threshold = gate["min"]
            else:
                passed = actual <= gate["max"]
                threshold = gate["max"]
            results.append(GateResult(
                metric=metric, threshold=threshold,
                actual=actual, passed=passed, is_hard=False,
            ))

        # Regression detection
        if baseline_path and self.config.get("regression", {}).get("enabled"):
            regression_results = self._check_regression(report, baseline_path)
            results.extend(regression_results)

        # Summarize
        hard_failures = [r for r in results if r.is_hard and not r.passed]
        soft_failures = [r for r in results if not r.is_hard and not r.passed]
        regressions = [r for r in results if r.is_regression and not r.passed]

        overall_passed = len(hard_failures) == 0

        return {
            "passed": overall_passed,
            "results": results,
            "hard_failures": hard_failures,
            "soft_failures": soft_failures,
            "regressions": regressions,
            "summary": self._build_summary(results, overall_passed),
        }

    def _check_regression(self, report: dict, baseline_path: str) -> list:
        """Regression detection"""
        with open(baseline_path) as f:
            baseline = json.load(f)

        tolerance = self.config["regression"].get("tolerance", 0.02)
        metrics = self.config["regression"].get("metrics", [])
        results = []

        for metric in metrics:
            if metric in report and metric in baseline:
                actual = report[metric]
                base = baseline[metric]
                regressed = actual < base - tolerance
                results.append(GateResult(
                    metric=f"regression:{metric}",
                    threshold=base - tolerance,
                    actual=actual,
                    passed=not regressed,
                    is_hard=True,
                    is_regression=True,
                ))

        return results

    def _build_summary(self, results: list, passed: bool) -> str:
        lines = []
        if passed:
            lines.append("Quality Gate PASSED ✓")
        else:
            lines.append("Quality Gate FAILED ✗")

        for r in results:
            icon = "✓" if r.passed else "✗"
            gate_type = "HARD" if r.is_hard else "SOFT"
            regression = " (REGRESSION)" if r.is_regression else ""
            lines.append(
                f"  {icon} [{gate_type}] {r.metric}: "
                f"{r.actual:.3f} (threshold: {r.threshold:.3f}){regression}"
            )

        return "\n".join(lines)
```

---

## 7. A/B Testing and Gray Scale Evaluation

## 7.1 Shadow Mode Inspector

```python
class ShadowModeEvaluator:
    """Shadow Mode: Parallel Run Comparison of New and Old Harnesses"""

    def __init__(self, current_harness, candidate_harness, evaluator):
        self.current = current_harness
        self.candidate = candidate_harness
        self.evaluator = evaluator

    async def evaluate(self, tasks: list[dict]) -> dict:
        """Parallel run two Harnesses and compare"""
        results = []

        for task in tasks:
            # Parallel run
            current_result = await self.current.run(task["input"])
            candidate_result = await self.candidate.run(task["input"])

            # Evaluate both
            current_score = self.evaluator.evaluate(
                task["input"], current_result["answer"],
                {"sources": task.get("context", "")},
            )
            candidate_score = self.evaluator.evaluate(
                task["input"], candidate_result["answer"],
                {"sources": task.get("context", "")},
            )

            results.append({
                "task": task["input"][:100],
                "current_score": current_score["weighted_score"],
                "candidate_score": candidate_score["weighted_score"],
                "current_tokens": current_result.get("total_tokens", 0),
                "candidate_tokens": candidate_result.get("total_tokens", 0),
                "winner": "candidate"
                    if candidate_score["weighted_score"] > current_score["weighted_score"]
                    else "current",
            })

        # Summarize
        candidate_wins = sum(1 for r in results if r["winner"] == "candidate")
        return {
            "total_tasks": len(results),
            "candidate_wins": candidate_wins,
            "current_wins": len(results) - candidate_wins,
            "win_rate": candidate_wins / len(results),
            "avg_score_improvement": sum(
                r["candidate_score"] - r["current_score"] for r in results
            ) / len(results),
            "recommendation": "deploy_candidate"
                if candidate_wins / len(results) > 0.6
                else "keep_current",
            "details": results,
        }
```

---

## 8. Best Practices

## 8.1 Core Principles of Validation Layer

| Principle | Explanation | Practice Recommendation |
|------|------|---------|
| **Preceding Validation** | Validation is the highest return on investment for Harness | Establish a validation pipeline from day one |
| **Multi-dimensional** | Single dimension cannot guarantee quality | Cover at least factual, security, and format dimensions |
| **Prioritize Self-check** | Have Agents self-check first, then external review | Deploy SelfCheckLoop |
| **Diverse Model Judge** | Avoid using the same model for self-evaluation | Generate and evaluate using different models |
| **Automate Gateways** | Integrate quality gates into CI/CD | Automatically assess each Harness change |
| **Baseline Comparison** | Save baselines for each assessment | Prevent regressions |

## 8.2 Anti-patterns

| Anti-pattern | Problem | Correct Approach |
|--------|------|----------|
| **Skip Validation** | Trust Agent Output → False Positive | Force through Validation Pipeline |
| **Self-Assessment with Same Model** | Homogeneous Bias → Misses Issues | Use Different Models for Judge |
| **Test Only Happy Path** | Edge Cases Fail | Include Edge Cases, Boundary Cases, Adversarial Cases |
| **No Baseline Logging** | Unable to Judge Progress | Save Baseline Files After Each Evaluation |
| **Validation Too Slow** | Slows Development Iterations | Layered Validation: Quick Checks + Deep Analysis |

---

## Related Documentation

| Documentation | Related Content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Definition of the Verification Layer in the Six-Layer Architecture |
| [31 - Loops and Execution Engine](./31-agent-harness-loop-execution.md) | Position of Verification in Loops |
| [35 - Security and Constraints](./35-agent-harness-security-constraints.md) | Foundation of Security Verification Constraints |
| [08 - Evaluation and Observability](./observability.md|08-agent-evaluation-observability]].md) | Foundations of RAGAS, LLM-as-Judge Theories |

---

## References

| Source | Content | Date |
|------|------|------|
| LangChain | Self-check Loop +13.7% Baseline Score Experiment | 2026-02 |
| RAGAS Project | Design of RAG Evaluation Framework | 2025-2026 |
| Anthropic | Best Practices for Agent Output Validation | 2026-02 |
| Google DeepMind | Research on LLM-as-Judge | 2025 |

---

*This document is original content from the kudig-database project 02-ai-agents series, delving into Agent Harness Validation and Quality Gates.*

---

## Obsidian Related Documentation

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Special Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval Enhanced Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage & Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Mult-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation Framework and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## Related

- 48-openclaw-skill-mechanism
- 13-trusted-agent-system-fiscal-plan
- 39-agent-harness-testing-benchmark
- 42-model-harness-compatibility-matrix
- 12-enterprise-case-studies
- 02-llm-foundation-models
- 23-agent-cli-fundamentals
- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals
- 03-agent-frameworks-comparison
- 47-openclaw-tools-mechanism
- 37-agent-harness-multi-agent
- 20-agentscope-multi-agent-orchestration
- 40-agent-harness-production-maturity
- 25-agent-cli-mcp-integration
- 26-agent-cli-development-workflow
- 07-memory-context-management
- 11-cost-latency-optimization
- 44-openclaw-soul-mechanism
- 45-openclaw-user-mechanism
- 31-agent-harness-loop-execution
- 27-agent-cli-security-governance
- 06-multi-agent-orchestration
- 41-react-harness-identification-guide

## See Also

- 32-agent-harness-tool-engineering
- 33-agent-harness-context-memory
- 35-agent-harness-security-constraints
- 36-agent-harness-observability


<!-- risk-assessed -->
