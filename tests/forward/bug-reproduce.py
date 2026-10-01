from tasks import search_tasks

tasks = [{"title": "Ship demo"}, {"title": "Write notes"}]
for query in ("", " \t\n ", "SHIP", "missing"):
    expected = tasks if not query.strip() else (tasks[:1] if query == "SHIP" else [])
    actual = search_tasks(tasks, query)
    print(f"query={query!r} expected={expected!r} actual={actual!r} matches={actual == expected}")
