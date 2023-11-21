import time

from helper_functions import *

# only modify the following two lines
steps = (1, 10, 25, 50, 100, 250, 500, 1000, 2000, 4000, 8000)
steps_delete = (1, 10, 25, 50, 100, 250, 500, 1000, 2000, 4000)


def todos_add(n):
    # todosSetUp("todos")
    addRandomEntries("todos", n, getRandomTestDataID)


def projects_add(n):
    # projectsSetUp("projects")
    addRandomEntries("projects", n, generateRandomTestDataProject)


def todos_modify(n):
    modifyRandomEntries(
        "todos",
        n,
        getRandomTodosID,
        getRandomTestDataID,
    )


def projects_modify(n):
    modifyRandomEntries(
        "projects",
        n,
        getRandomProjectsID,
        generateRandomTestDataProject,
    )


def todos_delete(n):
    deleteRandomEntries(
        "todos",
        n,
        getRandomTodosID,
    )
    addRandomEntries("todos", n, getRandomTestDataID)


def projects_delete(n):
    deleteRandomEntries(
        "projects",
        n,
        getRandomProjectsID,
    )
    addRandomEntries("projects", n, generateRandomTestDataProject)


if __name__ == "__main__":
    while True:
        print(
            """
1. Add random entries in todos
2. Add random entries in projects
3. Delete random entries in todos
4. Delete random entries in projects
5. Modify random entries in todos
6. Modify random entries in projects
"""
        )
        user_input = input(
            "Enter anything beside 1-6 to exit. Choose which test to run: "
        ).lower()
        try:
            user_input = int(user_input)
        except ValueError:
            print("Exiting...")
            break
        if not (1 <= user_input <= 6):
            print("Exiting...")
            break

        todosSetUp("todos")
        projectsSetUp("projects")

        if user_input == 1:
            function = todos_add
        elif user_input == 2:
            function = projects_add
        elif user_input == 3:
            steps = steps_delete
            todos_add(max(steps))
            function = todos_delete
        elif user_input == 4:
            steps = steps_delete
            projects_add(max(steps))
            function = projects_delete
        elif user_input == 5:
            todos_add(max(steps))
            function = todos_modify
        elif user_input == 6:
            projects_add(max(steps))
            function = projects_modify

        for i in steps:
            start = time.time()
            function(i)
            end = time.time()
            print(f"{i} entries: {end - start:.4f}s")
            # time.sleep(5)
