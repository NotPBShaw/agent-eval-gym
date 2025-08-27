from dataclasses import dataclass


@dataclass
class Scenario:
    name: str
    required_steps: list[str]
