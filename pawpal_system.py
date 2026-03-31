"""Core system classes for the PawPal+ pet care app.

This module provides a starter skeleton based on the UML design:
Owner, Pet, Task, Plan, and Scheduler.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Owner:
    """Stores owner details, constraints, and care priorities."""

    owner_name: str
    constraints: list[str] = field(default_factory=list)
    priorities: list[str] = field(default_factory=list)

    def get_owner_name(self) -> str:
        return self.owner_name

    def get_constraints(self) -> list[str]:
        return self.constraints

    def get_priorities(self) -> list[str]:
        return self.priorities


@dataclass
class Pet:
    """Stores basic pet information."""

    pet_desc: str
    pet_height: float
    pet_weight: float

    def get_pet_desc(self) -> str:
        return self.pet_desc

    def get_pet_height(self) -> float:
        return self.pet_height

    def get_pet_weight(self) -> float:
        return self.pet_weight


@dataclass
class Task:
    """Represents one pet-care task that can be added or edited."""

    title: str
    description: str = ""
    duration_minutes: int = 0
    priority: str = "medium"

    def get_task_info(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "duration_minutes": self.duration_minutes,
            "priority": self.priority,
        }

    def edit_task(
        self,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        duration_minutes: Optional[int] = None,
        priority: Optional[str] = None,
    ) -> None:
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if duration_minutes is not None:
            self.duration_minutes = duration_minutes
        if priority is not None:
            self.priority = priority


@dataclass
class Plan:
    """Represents the generated daily schedule or care plan."""

    tasks: list[Task] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    priorities: list[str] = field(default_factory=list)

    def get_plan(self) -> list[Task]:
        return self.tasks

    def edit_plan(
        self,
        *,
        tasks: Optional[list[Task]] = None,
        constraints: Optional[list[str]] = None,
        priorities: Optional[list[str]] = None,
    ) -> None:
        if tasks is not None:
            self.tasks = tasks
        if constraints is not None:
            self.constraints = constraints
        if priorities is not None:
            self.priorities = priorities


class Scheduler:
    """Creates a simple daily plan from owner preferences and task priority."""

    PRIORITY_ORDER = {"high": 3, "medium": 2, "low": 1}

    def generate_daily_plan(self, owner: Owner, pet: Pet, tasks: list[Task]) -> Plan:
        """Return a starter plan sorted by task priority.

        This is simple starter logic you can improve later with more scheduling rules.
        """
        del pet  # reserved for future pet-specific scheduling logic

        sorted_tasks = sorted(
            tasks,
            key=lambda task: self.PRIORITY_ORDER.get(task.priority.lower(), 0),
            reverse=True,
        )

        return Plan(
            tasks=sorted_tasks,
            constraints=owner.get_constraints(),
            priorities=owner.get_priorities(),
        )
