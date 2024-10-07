from datetime import datetime


def now(fmt: str) -> str:
    return datetime.now().strftime(fmt)


def filters():
    return {"now": now}
