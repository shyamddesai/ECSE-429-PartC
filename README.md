
# PerfChecker

PerfChecker is a comprehensive testing framework designed to conduct both **dynamic** and **static** software analyses, focusing on performance metrics, code quality, and maintainability. This project was developed to assess the API handling capabilities of a todo manager application, measure system performance under load, and analyze code structure for quality improvement.

## Key Features
1. **Dynamic Analysis**: 
   - Conducts load testing by adding, modifying, and deleting objects (todos and projects) in a database.
   - Tracks performance metrics like memory usage, CPU load, and transaction time, allowing developers to identify bottlenecks.
   - Utilizes Windows Performance Monitor to collect detailed data at various load levels, from 1 to 8000 objects, and logs transaction impact on memory and processor utilization.

2. **Static Analysis**:
   - Configured with **SonarQube** and **SonarScanner** for Python code analysis.
   - Measures code quality through cyclomatic and cognitive complexity, technical debt, and code smells.
   - Assesses code coverage (72.3%) and identifies maintainability issues (e.g., naming conventions and unused variables).

3. **Comprehensive Reporting**:
   - Performance reports visualize memory usage and CPU load as object count increases.
   - Code quality insights highlight areas for improvement, including potential bugs, security hotspots, and maintainability suggestions.

---

## Capabilities
### /todos/:id
#### DELETE
- Deleting an id also deletes all `taskof` and categories associated with it.

### /todos/:id/tasksof
#### POST
- Create a new task if no task id is specified (undocumented behavior).
- Add a task to specified `:id`.
- Add an existing task to `id` by specifying the task id in the body.
- Example request for `http://localhost:4567/todos/1/tasksof`:

```json
{
    "id": "4",
    "title": "Test Taskof Title",
    "completed": false,
    "active": false,
    "description": "Test Taskof description"
}
```

### /projects
- Projects are linked with `/todos/:id/tasksof`. Any task created will appear in projects; however, deleting ids will not delete any project.
- Deleting a project deletes its categories and `taskof`, just like todos.


## Bugs
#### /todos/:id/categories
- **GET**: Returns all categories instead of specific ones for `id`.
  
#### /todos/:id/tasksof
- **POST**: Duplicate IDs issue when creating new tasks with an existing ID.

#### /projects/:id/tasks
- **GET**: Returns all tasks instead of filtering by `id`.

---

## Technical Stack
- **Testing Tools**: Windows Performance Monitor for dynamic analysis, SonarQube, and SonarScanner for static analysis.
- **Language**: Python for API load testing scripts and static analysis configuration.
- **Database**: JSON-based todos and projects data simulation.
- **Reporting**: Data visualized in CSV and Excel spreadsheets, with graphs for transaction time vs. memory usage and CPU load.

## Setup and Execution
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/PerfCheckAI
   cd PerfCheckAI
   ```

2. **Run Dynamic Analysis**:
   - In the main project directory, execute:
     ```bash
     python dynamic_analysis.py
     ```

3. **Static Analysis**:
   - Set up SonarQube on localhost (requires Java 17).
   - Install SonarScanner and configure it to analyze Python code:
     ```bash
     sonar-scanner -Dsonar.projectKey=Python-project -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000
     ```
---

## Usage
### Running All Tests
To run all tests:
```bash
bash run_unittests.sh  # Linux
python -m unittest discover -p "test_*.py"  # Others
```

### Running One Module at a Time
Replace "filename.py" with the name of the test file:
```bash
python -m unittest discover -p "filename.py"
```
