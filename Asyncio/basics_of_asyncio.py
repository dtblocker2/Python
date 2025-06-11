import time

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

async def main2():
    print('Hello2 ...')
    print('... World2!')

async def main3():
    main()
    await main2()

asyncio.run(main3())