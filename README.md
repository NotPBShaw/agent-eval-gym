# Agent Eval Gym

Benchmark autonomous agents against scenario rubrics.

[![CI](https://github.com/NotPBShaw/agent-eval-gym/actions/workflows/ci.yml/badge.svg)](https://github.com/NotPBShaw/agent-eval-gym/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Define scenarios with required steps, score agent trajectories, and export evaluation reports.

## Why this exists

Agent demos look impressive until you measure them. Eval Gym provides a lightweight harness for grading whether an agent actually completed the steps a scenario requires.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
pytest -q
```

## Usage

```python
from eval_gym.scenario import Scenario
from eval_gym.scoring import score_trajectory

scenario = Scenario("checkout", required_steps=["open", "add", "pay"])
trajectory = ["open", "add", "pay", "confirm"]
print(score_trajectory(scenario, trajectory))  # 1.0
```

See `examples/scenarios.json` for sample scenario definitions.

## Architecture

- `scenario.py` — scenario definitions and required-step rubrics
- `scoring.py` — trajectory scoring against rubrics
- `report.py` — summary report formatting

## Roadmap

- [ ] CLI runner for batch scenario evaluation
- [ ] JSON report export with per-step breakdown
- [ ] Optional LLM-judge adapter hook

## Development

```bash
pytest -q
```

## License

MIT — see [LICENSE](LICENSE).
