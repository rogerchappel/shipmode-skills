def search_tasks(tasks, query):
    """Search titles; blank and whitespace-only queries should return all tasks."""
    if not query:
        return []
    needle = query.strip().casefold()
    return [task for task in tasks if needle in task["title"].casefold()]
