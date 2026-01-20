# 🌍 AX Agent Registry

The official global repository for [AX (Agent Package Manager)](https://github.com/ahmed6ww/ax). 

This registry serves as the central hub where developers from around the world share, discover, and improve specialized AI agent configurations. By contributing to this registry, you are helping to build a universal library of expert "identities" that can run anywhere (Claude Code, Cursor, etc.).

## 🎯 Purpose

- **Democratize Expert Knowledge**: Share specialized prompts and skillsets (e.g., "Senior Rust Engineer", "QA Specialist") so anyone can spin up an expert agent in seconds.
- **Write Once, Run Anywhere**: Define an agent's behavior once in a universal YAML format, and let AX compile it for any supported environment.
- **Community Driven**: A collaborative space to iterate on what makes a "good" agent.

## 🤝 How to Contribute

We welcome contributions from developers across the globe! Whether you've crafted the perfect Python debugging assistant or a deeply knowledgeable Kubernetes operator, we want your agent.

### Quick Start Guide

1.  **Fork & Clone**
    Fork this repository and clone it to your local machine.

2.  **Create Your Agent**
    Add a new YAML file in the `agents/` directory (e.g., `agents/my-special-agent.yaml`).
    
    ```yaml
    name: "my-special-agent"
    version: "1.0.0"
    identity:
      system_prompt: "..."
    skills:
      - name: "my-skill"
        content: "..."
    ```

3.  **Register It**
    Add your agent's metadata to `registry.json` so the CLI can find it.

4.  **Submit a PR**
    Open a Pull Request with your new agent. Once approved, it will be instantly available to all AX users via `ax install my-special-agent`.

For detailed schema documentation and strict guidelines, please read [CONTRIBUTING.md](./CONTRIBUTING.md).

## 📦 Available Agents

| Agent | Description | Author |
|-------|-------------|--------|
| 🦀 [rust-architect](agents/rust-architect.yaml) | Senior Rust Systems Engineer optimized for Tokio & zero-cost abstractions | ahmed6ww |
| ⚡ [fullstack-next](agents/fullstack-next.yaml) | Next.js 15 + FastAPI + ShadcnUI full-stack expert | ahmed6ww |
| 🧪 [qa-testing-squad](agents/qa-testing-squad.yaml) | Playwright + Jest testing configuration specialist | ahmed6ww |

## License

MIT
