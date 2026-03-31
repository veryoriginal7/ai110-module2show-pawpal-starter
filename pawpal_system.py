"""Core system classes for the PawPal+ pet care app.

This module provides a starter skeleton based on the UML design:
Owner, Pet, Task, Plan, and Scheduler.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    """Represents a single pet-care activity."""

    title: str
    description: str = ""
    time: str = ""
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def get_task_info(self) -> dict:
        """Return this task's details as a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "completed": self.completed,
        }

    def edit_task(
        self,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        time: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> None:
        """Update any provided task fields."""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if time is not None:
            self.time = time
        if frequency is not None:
            self.frequency = frequency


@dataclass
class Pet:
    """Stores pet details and a list of associated tasks."""

    pet_name: str
    pet_desc: str = ""
    pet_height: float = 0.0
    pet_weight: float = 0.0
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, title: str) -> None:
        """Remove tasks matching the given title."""
        self.tasks = [t for t in self.tasks if t.title != title]

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""

    owner_name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name."""
        self.pets = [p for p in self.pets if p.pet_name != pet_name]

    def get_pets(self) -> list[Pet]:
        """Return all pets owned by this owner."""
        return self.pets

    def get_all_tasks(self) -> list[tuple[Pet, Task]]:
        """Return all (pet, task) pairs across every pet."""
        return [(pet, task) for pet in self.pets for task in pet.get_tasks()]


@dataclass
class Plan:
    """Represents the generated daily schedule or care plan."""

    tasks: list[Task] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    priorities: list[str] = field(default_factory=list)

    def get_plan(self) -> list[Task]:
        """Return the tasks in this plan."""
        return self.tasks

    def edit_plan(
        self,
        *,
        tasks: Optional[list[Task]] = None,
        constraints: Optional[list[str]] = None,
        priorities: Optional[list[str]] = None,
    ) -> None:
        """Update the plan with any provided values."""
        if tasks is not None:
            self.tasks = tasks
        if constraints is not None:
            self.constraints = constraints
        if priorities is not None:
            self.priorities = priorities


class Scheduler:
    """The brain that retrieves, organizes, and manages tasks across pets."""

    def get_tasks_for_pet(self, pet: Pet) -> list[Task]:
        """Return all tasks for a single pet."""
        return pet.get_tasks()

    def get_all_tasks(self, owner: Owner) -> list[tuple[Pet, Task]]:
        """Return all (pet, task) pairs across every pet owned by the owner."""
        return owner.get_all_tasks()

    def get_pending_tasks(self, owner: Owner) -> list[tuple[Pet, Task]]:
        """Return only incomplete (pet, task) pairs."""
        return [(pet, task) for pet, task in owner.get_all_tasks() if not task.completed]

    def mark_task_complete(self, owner: Owner, pet_name: str, task_title: str) -> bool:
        """Mark a specific task as complete. Returns True if found and marked."""
        for pet in owner.get_pets():
            if pet.pet_name == pet_name:
                for task in pet.get_tasks():
                    if task.title == task_title:
                        task.mark_complete()
                        return True
        return False

    def organize_by_time(self, owner: Owner) -> list[tuple[Pet, Task]]:
        """Return all pending tasks sorted by scheduled time."""
        pending = self.get_pending_tasks(owner)
        return sorted(pending, key=lambda pt: pt[1].time)
