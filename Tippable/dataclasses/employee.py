"""Module for the employee dataclass"""

import dataclasses

@dataclasses.dataclass
class Employee:
    """Class that represents an employee"""
    name: str
    id_: str
    tippable_hours: float = 0.0
    amount_received: int = 0

    def __hash__(self):
        return hash(self.id_)
