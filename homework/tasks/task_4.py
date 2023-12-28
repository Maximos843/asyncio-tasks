async def task_1(i: int):
    global const
    if i == 0:
        return
    if i > 5:
        const += '2'
        await task_2(i // 2)
    else:
        const += '2'
        await task_2(i - 1)


async def task_2(i: int):
    global const
    if i == 0:
        return
    if i % 2 == 0:
        const += '1'
        await task_1(i // 2)
    else:
        const += '2'
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 7) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    global const
    const = ''
    await task_1(i)
    return int(const)

    # YOUR CODE GOES HERE
