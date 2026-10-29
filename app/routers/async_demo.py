import asyncio
import time

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/async", tags=["async-demo"])


async def _slow(name: str, seconds: float = 1.0) -> dict:
    await asyncio.sleep(seconds)
    return {"name": name, "seconds": seconds}


def _blocking_work(seconds: float = 1.0) -> dict:
    time.sleep(seconds)
    return {"mode": "blocking", "seconds": seconds}


@router.get("/sequential")
async def sequential() -> dict:
    start = time.perf_counter()
    a = await _slow("Stock", 1.0)
    b = await _slow("Price", 1.0)
    c = await _slow("Shipping", 1.0)
    return {
        "mode": "sequential",
        "elapsed": round(time.perf_counter() - start, 3),
        "result": [a, b, c],
    }


@router.get("/concurrent")
async def concurrent() -> dict:
    start = time.perf_counter()
    results = await asyncio.gather(
        _slow("Stock", 1.0),
        _slow("Price", 1.0),
        _slow("Shipping", 1.0),
    )
    return {
        "mode": "concurrent",
        "elapsed": round(time.perf_counter() - start, 3),
        "result": results,
    }


@router.get("/timeout")
async def with_timeout(delay: float = 5.0) -> dict:
    try:
        result = await asyncio.wait_for(_slow("external", delay), timeout=2.0)
        return {"mode": "timeout", "result": result}
    except TimeoutError:
        raise HTTPException(status_code=504, detail="Upstream timed out")


@router.get("/to-thread")
async def to_thread_demo() -> dict:
    start = time.perf_counter()
    other = await _slow("async-part", 0.5)
    blocking = await asyncio.to_thread(_blocking_work, 1.0)
    return {
        "mode": "to-thread",
        "elapsed": round(time.perf_counter() - start, 3),
        "result": [other, blocking],
    }
