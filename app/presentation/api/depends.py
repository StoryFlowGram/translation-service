from fastapi import Header, HTTPException

async def translation_repo():
    raise NotImplementedError("Должен быть переопределён в слое инфры")


async def cgpt_repo():
    raise NotImplementedError("Должен быть переопределён в слое инфры")



async def get_current_user(x_user_id: str = Header(default=None, alias="X-User-Id")):
    if x_user_id is None:
        raise HTTPException(status_code=401, detail="X-User-ID Хедер отсутствует")
    return x_user_id