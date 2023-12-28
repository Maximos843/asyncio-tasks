from asyncio import Task
from typing import Callable, Coroutine, Any
import asyncio


async def await_my_func(f: Callable[..., Coroutine] or Task or Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        # YOUR CODE GOES HERE
        result = await asyncio.create_task(f)
        return result
    elif isinstance(f, Task):
        # YOUR CODE GOES HERE
        result = await f
        return result
    elif isinstance(f, Coroutine):
       result = await f
       return result
    else:
        raise ValueError('invalid argument')
