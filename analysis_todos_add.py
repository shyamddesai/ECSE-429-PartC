import time

from helper_functions import *

for i in steps:
    todosSetUp("todos")

    start = time.time()
    addRandomEntries(number_of_entries=i)
    end = time.time()
    print(f"Add {i} entries: {end - start:.4f}s")
