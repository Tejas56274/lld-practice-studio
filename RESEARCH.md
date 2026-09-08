# Research Note: LLD Practice Platform MVP

## 1. Learner Problem

Current coding platforms (LeetCode, HackerRank) focus on algorithmic efficiency (Time/Space complexity) and functional correctness. Real-world software engineering requires **Low-Level Design (LLD)**: clean class responsibilities, application of SOLID principles, extensibility, and proper design pattern selection. Learners struggle because design evaluation is qualitative, subjective, and rarely automated.

## 2. Existing Approaches & Gaps

- **Peer Code Reviews:** Slow, asynchronous, and dependent on mentor availability.
- **Static Analysis Tools (SonarQube/Checkstyle):** Too rigid; they measure code style metrics rather than domain modeling quality.
- **The Gap:** There is no lightweight loop allowing learners to submit domain models and instantly receive explainable architectural feedback on object relationships and extensibility trade-offs.

## 3. Product Direction

Our MVP introduces a frictionless practice loop: **Choose problem -> Code class structures -> Hybrid Evaluation (Deterministic AST checks + LLM architectural reasoning) -> Review feedback & track history.**
