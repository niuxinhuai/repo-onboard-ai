# Repo Onboard AI

[![CI](https://github.com/niuxinhuai/repo-onboard-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/niuxinhuai/repo-onboard-ai/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

[中文文档](README.zh-CN.md)

Scan a repository and generate a practical `ONBOARDING.md` for new contributors.

Repo Onboard AI detects languages, top-level areas, likely entry points, and command hints. It runs locally by default and can optionally ask an OpenAI-compatible model to improve the guide.

## Features

- Scans repository files while ignoring common generated and dependency directories.
- Detects language mix and top-level areas.
- Suggests reading order and likely entry points.
- Infers install, run, build, and test commands from common manifests.
- Can include a compact repository tree with `--tree`.
- Supports Markdown and JSON output.

## Install

```bash
python3 -m pip install -e .
```

## Usage

```bash
repo-onboard-ai --repo .
repo-onboard-ai --repo . --tree
repo-onboard-ai --repo . --output ONBOARDING.md
repo-onboard-ai --repo . --format json
repo-onboard-ai --repo ../some-project --max-files 1200
```

See generated examples in [`examples/output.md`](examples/output.md) and [`examples/output.json`](examples/output.json).

Use AI polishing:

```bash
export AI_API_KEY="your-key"
repo-onboard-ai --repo . --ai --output ONBOARDING.md
```

## Development

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests
```

## License

MIT
