# AI Security Lab

A compact defensive research lab focused on **LLM and coding-agent security**.

The goal is to evaluate how AI-assisted development can introduce or amplify security risks, and to build simple, reproducible checks for safer code-generation workflows.

## Focus areas

- prompt-injection resilience
- insecure code generation
- secret leakage and hard-coded credentials
- dangerous command execution patterns
- unsafe deserialization / shell invocation
- security review of AI-generated code
- evaluation methodology for coding agents

## Structure

```text
labs/ai-security-lab/
├── README.md
├── evals/
│   ├── prompt-injection-cases.md
│   └── code-agent-security-checklist.md
└── scripts/
    └── scan_generated_code.py
```

## Evaluation idea

For each coding-agent test:

1. define a neutral software task
2. generate one or more candidate implementations
3. scan for risky patterns
4. manually review security-sensitive behavior
5. compare results across prompts/models
6. record whether the generated code requires mitigation

## Example metrics

- number of insecure patterns per generated sample
- secrets or credentials exposed
- unsafe shell/process invocation
- missing input validation
- unsafe network defaults
- dependency risk indicators
- percentage of findings fixed after a security-focused prompt

## Roadmap

- add a small benchmark of safe coding tasks
- compare baseline prompts vs security-aware prompts
- add Semgrep/Bandit integration
- add dependency checks
- add structured results in CSV/JSON
- visualize findings in a small Streamlit dashboard
