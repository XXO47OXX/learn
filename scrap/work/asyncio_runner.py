from collections import deque
import asyncio


class AsyncioRunner:
    def __init__(self, task_count=5) -> None:
        self.task_count = task_count
        self.running = set()
        self.waiting = deque()

    @property
    def running_task_count(self) -> int:
        return len(self.running)

    def add_task(self, coro) -> None:
        if len(self.running) >= self.task_count:
            self.waiting.append(coro)
        else:
            self._start_task(coro)

    def _start_task(self, coro) -> None:
        self.running.add(coro)
        asyncio.create_task(self._task(coro))

    async def _task(self, coro):
        try:
            return await coro
        finally:
            self.running.remove(coro)
            if self.waiting:
                coro2 = self.waiting.popleft()
                self._start_task(coro2)
