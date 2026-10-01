def search_tasks(tasks, query):
    if not query:
        return list(tasks)
    needle = query.strip().casefold()
    if not needle:
        return []
    return [task for task in tasks if needle in task["title"].casefold()]
