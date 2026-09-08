## Blocking

- The main javascript thread that is running can't continue with another task until unless the current operation finishes
  Example: Synchronous operations - readFileSync

## Non blocking

- Can continue with other tasks and come back to the task once the result is ready
  Example: Asynchronous operations - readFile
