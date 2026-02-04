#!/usr/bin/env python3
"""
Git Workshop: Collaborative Task Manager
"""

from datetime import datetime
from typing import Optional


# DATA STRUCTURES (provided - do not modify)

# Valid priority values (use these strings)
PRIORITIES: list[str] = ["low", "medium", "high"]

# A Task is a dictionary with these keys:
# {
#     "id": int,
#     "title": str,
#     "description": str,
#     "priority": str,        # "low", "medium", or "high"
#     "completed": bool,
#     "created_at": str,      # ISO format datetime string
# }

# Type alias for clarity
Task = dict

# Global task storage
_tasks: list[Task] = []
_next_id: int = 1


# ============================================================================
# STUDENT FUNCTIONS - Each student implements ONE function
# ============================================================================

# --------------------------------------------------------------------------
# STUDENT 1: Generate Task ID
# --------------------------------------------------------------------------
def generate_task_id() -> int:
    """
    Generate a unique ID for a new task.

    Uses the global _next_id variable to track the next available ID.
    Should increment _next_id after getting the current value.

    Returns:
        int: A unique task ID

    Example:
        >>> # If _next_id is 1
        >>> id1 = generate_task_id()  # Returns 1, _next_id becomes 2
        >>> id2 = generate_task_id()  # Returns 2, _next_id becomes 3
    """
    global _next_id
    # TODO: Student 1 - Implement this function
    # Hint: Get current _next_id, increment it, return the old value
    raise NotImplementedError("Student 1: Implement generate_task_id()")


# --------------------------------------------------------------------------
# STUDENT 2: Create Task
# --------------------------------------------------------------------------
def create_task(title: str, description: str, priority: str) -> Task:
    """
    Create a new task dictionary with the given parameters.

    Args:
        title: The task title
        description: Detailed description of the task
        priority: Priority level ("low", "medium", or "high")

    Returns:
        Task: A new task dictionary with a unique ID

    Example:
        >>> task = create_task("Buy milk", "Get 2% milk", "low")
        >>> task["title"]
        'Buy milk'
        >>> task["completed"]
        False
    """
    # TODO: Student 2 - Implement this function
    # Hint: Use generate_task_id() and create a dict with all required keys
    # Keys needed: "id", "title", "description", "priority", "completed", "created_at"
    # Use datetime.now().isoformat() for created_at
    raise NotImplementedError("Student 2: Implement create_task()")


# --------------------------------------------------------------------------
# STUDENT 3: Add Task to Storage
# --------------------------------------------------------------------------
def add_task(task: Task) -> bool:
    """
    Add a task to the global task list.

    Args:
        task: The task dictionary to add

    Returns:
        bool: True if added successfully, False if task with same ID exists

    Example:
        >>> task = create_task("Test", "Description", "low")
        >>> add_task(task)
        True
    """
    # TODO: Student 3 - Implement this function
    # Hint: Check if task["id"] already exists in _tasks before adding
    raise NotImplementedError("Student 3: Implement add_task()")


# --------------------------------------------------------------------------
# STUDENT 4: Find Task by ID
# --------------------------------------------------------------------------
def find_task_by_id(task_id: int) -> Optional[Task]:
    """
    Find and return a task by its ID.

    Args:
        task_id: The ID of the task to find

    Returns:
        Optional[Task]: The task dict if found, None otherwise

    Example:
        >>> task = find_task_by_id(1)
        >>> task["title"] if task else "Not found"
    """
    # TODO: Student 4 - Implement this function
    # Hint: Loop through _tasks and check each task's "id" key
    raise NotImplementedError("Student 4: Implement find_task_by_id()")


# --------------------------------------------------------------------------
# STUDENT 5: Mark Task Complete
# --------------------------------------------------------------------------
def mark_complete(task_id: int) -> bool:
    """
    Mark a task as completed.

    Args:
        task_id: The ID of the task to mark complete

    Returns:
        bool: True if task was found and marked, False otherwise

    Example:
        >>> mark_complete(1)
        True
    """
    # TODO: Student 5 - Implement this function
    # Hint: Use find_task_by_id() and set "completed" to True
    raise NotImplementedError("Student 5: Implement mark_complete()")


# --------------------------------------------------------------------------
# STUDENT 6: Delete Task
# --------------------------------------------------------------------------
def delete_task(task_id: int) -> bool:
    """
    Delete a task from the task list.

    Args:
        task_id: The ID of the task to delete

    Returns:
        bool: True if task was found and deleted, False otherwise

    Example:
        >>> delete_task(1)
        True
    """
    global _tasks
    # TODO: Student 6 - Implement this function
    # Hint: Find the task index, remove it from _tasks if found
    raise NotImplementedError("Student 6: Implement delete_task()")


# --------------------------------------------------------------------------
# STUDENT 7: Get All Tasks
# --------------------------------------------------------------------------
def get_all_tasks() -> list[Task]:
    """
    Return a copy of all tasks.

    Returns:
        list[Task]: A copy of the task list (not the original)

    Example:
        >>> tasks = get_all_tasks()
        >>> len(tasks)
        3
    """
    # TODO: Student 7 - Implement this function
    # Hint: Return a copy using list() or _tasks[:]
    raise NotImplementedError("Student 7: Implement get_all_tasks()")


# --------------------------------------------------------------------------
# STUDENT 8: Filter by Priority
# --------------------------------------------------------------------------
def get_tasks_by_priority(priority: str) -> list[Task]:
    """
    Get all tasks with a specific priority.

    Args:
        priority: The priority level to filter by ("low", "medium", "high")

    Returns:
        list[Task]: List of tasks matching the priority

    Example:
        >>> high_priority = get_tasks_by_priority("high")
    """
    # TODO: Student 8 - Implement this function
    # Hint: Create empty list, loop through _tasks, append matches
    raise NotImplementedError("Student 8: Implement get_tasks_by_priority()")


# --------------------------------------------------------------------------
# STUDENT 9: Get Incomplete Tasks
# --------------------------------------------------------------------------
def get_incomplete_tasks() -> list[Task]:
    """
    Get all tasks that are not completed.

    Returns:
        list[Task]: List of incomplete tasks

    Example:
        >>> incomplete = get_incomplete_tasks()
    """
    # TODO: Student 9 - Implement this function
    # Hint: Filter _tasks where "completed" is False
    raise NotImplementedError("Student 9: Implement get_incomplete_tasks()")


# --------------------------------------------------------------------------
# STUDENT 10: Count Tasks
# --------------------------------------------------------------------------
def count_tasks() -> dict[str, int]:
    """
    Count tasks by status.

    Returns:
        dict[str, int]: Dictionary with keys "total", "completed", "incomplete"

    Example:
        >>> counts = count_tasks()
        >>> counts
        {"total": 5, "completed": 2, "incomplete": 3}
    """
    # TODO: Student 10 - Implement this function
    # Hint: Count total with len(), loop to count completed
    raise NotImplementedError("Student 10: Implement count_tasks()")


# --------------------------------------------------------------------------
# STUDENT 11: Format Task for Display
# --------------------------------------------------------------------------
def format_task(task: Task) -> str:
    """
    Format a task as a readable string for display.

    Args:
        task: The task dictionary to format

    Returns:
        str: Formatted string representation

    Example:
        >>> print(format_task(task))
        [X] #1 Buy milk (high) - Get 2% milk
        or
        [ ] #1 Buy milk (high) - Get 2% milk
    """
    # TODO: Student 11 - Implement this function
    return f"[X] #1 Buy milk (high) - Get 2% milk"


# --------------------------------------------------------------------------
# STUDENT 12: Validate Priority
# --------------------------------------------------------------------------
def is_valid_priority(priority_str: str) -> bool:
    """
    Check if a string is a valid priority value.

    Args:
        priority_str: String to validate (case-insensitive)

    Returns:
        bool: True if valid priority, False otherwise

    Example:
        >>> is_valid_priority("HIGH")
        True
        >>> is_valid_priority("high")
        True
        >>> is_valid_priority("invalid")
        False
    """
    # TODO: Student 12 - Implement this function
    # Hint: Convert to lowercase and check if in PRIORITIES list
    raise NotImplementedError("Student 12: Implement is_valid_priority()")


# ============================================================================
# MAIN APPLICATION (provided - uses all student functions)
# ============================================================================

def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("📋 TASK MANAGER")
    print("=" * 50)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. View tasks by priority")
    print("4. Mark task complete")
    print("5. Delete task")
    print("6. View statistics")
    print("7. Exit")
    print("-" * 50)


def get_user_input(prompt: str) -> str:
    """Get input from user with a prompt."""
    return input(f"{prompt}: ").strip()


def run_app() -> None:
    """Main application loop."""
    print("\n🎉 Welcome to the Collaborative Task Manager!")
    print("Built by students learning Git!\n")

    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-7)")

        try:
            if choice == "1":
                # Add new task
                title = get_user_input("Task title")
                description = get_user_input("Description")
                priority_str = get_user_input("Priority (low/medium/high)")
                priority = priority_str.lower()

                if not is_valid_priority(priority):
                    print("❌ Invalid priority. Use: low, medium, or high")
                    continue

                task = create_task(title, description, priority)
                if add_task(task):
                    print(f"✅ Task #{task['id']} created successfully!")
                else:
                    print("❌ Failed to create task")

            elif choice == "2":
                # View all tasks
                tasks = get_all_tasks()
                if not tasks:
                    print("📭 No tasks found")
                else:
                    print("\n📋 All Tasks:")
                    for task in tasks:
                        print(f"  {format_task(task)}")

            elif choice == "3":
                # View by priority
                priority_str = get_user_input("Priority (low/medium/high)")
                priority = priority_str.lower()

                if not is_valid_priority(priority):
                    print("❌ Invalid priority")
                    continue

                tasks = get_tasks_by_priority(priority)
                if not tasks:
                    print(f"📭 No {priority} priority tasks")
                else:
                    print(f"\n📋 {priority.upper()} Priority Tasks:")
                    for task in tasks:
                        print(f"  {format_task(task)}")

            elif choice == "4":
                # Mark complete
                task_id_str = get_user_input("Task ID to mark complete")
                try:
                    task_id = int(task_id_str)
                    if mark_complete(task_id):
                        print(f"✅ Task #{task_id} marked complete!")
                    else:
                        print(f"❌ Task #{task_id} not found")
                except ValueError:
                    print("❌ Invalid task ID")

            elif choice == "5":
                # Delete task
                task_id_str = get_user_input("Task ID to delete")
                try:
                    task_id = int(task_id_str)
                    if delete_task(task_id):
                        print(f"🗑️ Task #{task_id} deleted!")
                    else:
                        print(f"❌ Task #{task_id} not found")
                except ValueError:
                    print("❌ Invalid task ID")

            elif choice == "6":
                # Statistics
                counts = count_tasks()
                incomplete = get_incomplete_tasks()

                print("\n📊 Task Statistics:")
                print(f"  Total tasks: {counts['total']}")
                print(f"  Completed: {counts['completed']}")
                print(f"  Incomplete: {counts['incomplete']}")

                if incomplete:
                    print("\n⏳ Incomplete tasks:")
                    for task in incomplete:
                        print(f"  {format_task(task)}")

            elif choice == "7":
                print("\n👋 Goodbye! Happy coding with Git!")
                break

            else:
                print("❌ Invalid choice. Please enter 1-7")

        except NotImplementedError as e:
            print(f"\n⚠️ Function not yet implemented: {e}")
            print("Keep working on Git - more pull requests needed! 🔧")


if __name__ == "__main__":
    run_app()