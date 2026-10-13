# LaunchCodeAgenticEngineer
LaunchCode Agentic Engineer Course

Each module is a self-contained Docker development environment with its own
`Dockerfile`, `README.md`, and `CLAUDE.md`. See the module READMEs for build and
run instructions.

## Project Structure

```text
.
├── module_1/                 Base environment: Python 3.12, Claude Code CLI, Streamlit
│   ├── Dockerfile, docker-entrypoint.sh, requirements.txt
│   ├── settings.json, statusline.sh   Claude Code settings and status line
│   ├── module_x.py           Business-rule utilities (parallel-session exercise, Session A)
│   ├── module_y.py           Formatting/reporting utilities (parallel-session exercise, Session B)
│   └── agent_docker_check.md
├── module_2/                 Adds Slack and Gmail MCP servers, skills, and agents
│   ├── agents/               Sub-agent definitions (code-reviewer, email-summarize)
│   ├── skills/               Slash-command skills (check-gmail, send-email, ...)
│   ├── sample_docs/          PRD, rubric, and iteration log for exercises
│   └── sample_review.py      Script with deliberate issues for code-review practice
└── module_3/                 Multi-agent orchestration, evaluation, and retrieval
    ├── agents/               Planner, implementer, reviewer, project-manager, ...
    ├── skills/               Slash-command skills carried over from Module 2
    ├── mcp/                  Course MCP servers (coursetools, retrieval, storage)
    ├── eval/                 Orchestrator, regression/holdout runners, and tests
    ├── docs/                 PRD, orchestration diagrams, routing map, reports
    ├── scripts/              Helpers to start MCP servers and run retrieval comparisons
    ├── .eval-artifacts/      Baseline and recorded evaluation runs
    └── .memory/reference/    Reference notes served by the retrieval MCP server
```

## Modules

| Module | Image | Highlights |
| --- | --- | --- |
| [Module 1](module_1/README.md) | `agentic_engineer_1` | Python + Claude Code base environment, Gmail API setup |
| [Module 2](module_2/README.md) | `agentic_engineer_2` | Slack/Gmail MCP servers, pre-installed skills and agents |
| [Module 3](module_3/README.md) | `agentic_engineer_3` | Multi-agent orchestration, evals, retrieval and storage MCP servers |
