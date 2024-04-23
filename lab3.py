import asyncio


async def do_some_work(x):
    print("Жұмыс істеу басталды:", x)

    await asyncio.sleep(2)
    return f"Жұмыс аяқталды: {x}"


async def main():

    result1 = await do_some_work(1)
    print(result1)

    result2 = await do_some_work(2)
    print(result2)


asyncio.run(main())
