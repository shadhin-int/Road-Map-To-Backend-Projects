# Task Tracker CLI
## Requirements

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

-   Add, Update, and Delete tasks
-   Mark a task as in progress or done
-   List all tasks
-   List all tasks that are done
-   List all tasks that are not done
-   List all tasks that are in progress


## Example

The list of commands and their usage is given below:

### Adding a new task
```bash
python task-cli add "Buy groceries"
Output: Task added successfully (ID: 1)
```

### Updating tasks
```bash
python task-cli update 1 "Buy groceries and cook dinner"
```
### Deleting a task
```bash
task-cli delete 1
```

### Marking a task as in progress or done
``` bash
python task-cli mark-in-progress 1
task-cli mark-done 1
```

### Listing all tasks
``` bash
python task-cli list
```

### Listing tasks by status

``` bash
python task-cli list done
python task-cli list todo
python task-cli list in-progress
```

## Project Link

For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).