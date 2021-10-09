import asyncio


async def other_coroutine(arg):
    "A coroutine"
    print(arg)


async def main():
    "The top-level coroutine."
    await other_coroutine(42)


#каноническая точка входа
asyncio.run(main())
