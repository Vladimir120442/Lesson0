import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')  # Объявление участников

    for i in range(1, 6):    # Соревнование (самый сильный - самый быстрый)
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():  # Репортаж о соревновании (задачи участникам)

    tasks = [start_strongman('Иван', 4),
             start_strongman('Петр', 3),
             start_strongman('Сидор', 5)]

    await asyncio.gather(*tasks)  # Ожидание завершения соревнований (задач участникам)

if __name__ == '__main__':
    asyncio.run(start_tournament())

