import asyncio

async def print_count(x):
        for number in range(x):
            print(number)
            await asyncio.sleep(.5) #спать 5 сек

async def start(x):
    coroutines = []

    for number in range(x):
        coroutines.append(
            asyncio.create_task(print_count(x))
        )

    await asyncio.wait(coroutines)

user = input('user = ')
asyncio.run(start(user))