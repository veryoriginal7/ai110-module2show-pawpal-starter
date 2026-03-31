from pawpal_system import Pet, Task


def test_mark_complete_changes_task_status():
    task = Task(title="Feed breakfast")

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(pet_name="Buddy")
    initial_count = len(pet.get_tasks())

    pet.add_task(Task(title="Go for a walk"))

    assert len(pet.get_tasks()) == initial_count + 1
