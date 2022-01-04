import asyncio 
import typing 


async def foo() -> typing.NoReturn:
    ...

async def sleep() -> typing.NoReturn:
    import time 
    print(1)
    await asyncio.sleep(3)
    task = asyncio.create_task(foo())

async def main() -> typing.NoReturn:
    task1 = asyncio.create_task(sleep())
    await asyncio.sleep(2)
    await task1


    # await asyncio.sleep(0.5)
    # await print_numbers()
    # await print_numbers()



asyncio.run(main())