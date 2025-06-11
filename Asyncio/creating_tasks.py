import asyncio

async def main():
    # Schedule result1 to run in the background
    task1 = asyncio.create_task(asyncio.sleep(10, result='hello1'))

    # Wait for the shorter task first
    result2 = await asyncio.sleep(3, result='hello2')
    print(result2)

    # Now wait for the longer task
    result1 = await task1
    print(result1)

asyncio.run(main())
