"""
student10
"""
tasks = [
    {'status': 'completed'},
    {'status': 'completed'},
    {'status': 'incomplete'},
    {'status': 'incomplete'},
    {'status': 'incomplete'}
]

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
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task['status'] == 'completed':
            completed += 1
    incomplete = total - completed
    return {"total": total, "completed": completed, "incomplete": incomplete}

 if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
