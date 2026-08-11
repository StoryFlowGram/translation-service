import asyncio
import time
from collections import defaultdict, deque

from fastapi import HTTPException, status


class InMemoryRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._hits: dict[str, deque[float]] = defaultdict(deque)
        self._lock = asyncio.Lock()

    async def check(self, key: str):
        now = time.monotonic()
        async with self._lock:
            bucket = self._hits[key]
            while bucket and now - bucket[0] >= self.window_seconds:
                bucket.popleft()

            if len(bucket) >= self.max_requests:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Please try again later.",
                )

            bucket.append(now)
