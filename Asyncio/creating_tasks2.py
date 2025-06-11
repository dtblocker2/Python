import asyncio

async def sleep_and_return(delay, name):
    await asyncio.sleep(delay)
    return f"{name} finished after {delay} seconds"

async def main():
    task1 = asyncio.create_task(sleep_and_return(10, "Task1"))
    task2 = asyncio.create_task(sleep_and_return(3, "Task2"))
    task3 = asyncio.create_task(sleep_and_return(5, "Task3"))

    done, pending = await asyncio.wait(
        [task1, task2, task3],
        return_when=asyncio.FIRST_COMPLETED
    )

    # Get and print the first completed task's result
    for task in done:
        print(await task)

    # Optional: Cancel or continue waiting for the others
    for task in pending:
        print(f"Cancelling {task.get_coro().__name__}")
        task.cancel()

asyncio.run(main())
