from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(owner: Owner, scheduler: Scheduler) -> None:
    print("=" * 40)
    print("       TODAY'S SCHEDULE")
    print("=" * 40)

    pending = scheduler.organize_by_time(owner)

    if not pending:
        print("No pending tasks for today!")
    else:
        for pet, task in pending:
            status = "[x]" if task.completed else "[ ]"
            print(f"{status} {task.time:>5}  |  {pet.pet_name:<10}  |  {task.title}")
            if task.description:
                print(f"              {task.description}")

    print("=" * 40)


def main() -> None:
    # --- Create owner ---
    owner = Owner(owner_name="Dat")

    # --- Create pets ---
    buddy = Pet(pet_name="Buddy", pet_desc="Golden Retriever", pet_weight=30.0, pet_height=60.0)
    mochi = Pet(pet_name="Mochi", pet_desc="Persian Cat", pet_weight=4.5, pet_height=25.0)

    owner.add_pet(buddy)
    owner.add_pet(mochi)

    # --- Add tasks to Buddy ---
    buddy.add_task(Task(title="Morning Walk",    description="30-min walk around the block", time="07:00", frequency="daily"))
    buddy.add_task(Task(title="Dinner",          description="1 cup dry kibble",             time="18:00", frequency="daily"))

    # --- Add tasks to Mochi ---
    mochi.add_task(Task(title="Brush Coat",      description="Use the fine-tooth comb",      time="09:00", frequency="daily"))
    mochi.add_task(Task(title="Vet Check-up",    description="Annual vaccination booster",   time="14:30", frequency="yearly"))
    mochi.add_task(Task(title="Evening Feeding", description="Half can of wet food",         time="19:00", frequency="daily"))

    # --- Print schedule ---
    scheduler = Scheduler()
    print_schedule(owner, scheduler)


if __name__ == "__main__":
    main()
