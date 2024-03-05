from contextlib import asynccontextmanager

import redis.asyncio as redis
from transformers import BartForConditionalGeneration, BartTokenizer

from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from fastapi_globals import GlobalsMiddleware, g
from settings import Settings
from schemas import OutputText, InputText
from utils.generate_summarize import generate_summarize
from docs import summarize as docs_summarize


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = Settings()
    tokenizer = BartTokenizer.from_pretrained(settings.model_name)
    model = BartForConditionalGeneration.from_pretrained(settings.model_name)
    g.set_default("model", model)
    g.set_default("tokenizer", tokenizer)
    g.set_default("settings", settings)
    redis_connection = redis.from_url(settings.redis_url, encoding="utf8")
    await FastAPILimiter.init(redis_connection)
    yield
    del tokenizer, model, settings
    g.cleanup()
    await FastAPILimiter.close()


app = FastAPI(lifespan=lifespan)
app.add_middleware(GlobalsMiddleware)


@app.post(
    "/summarize",
    description=docs_summarize.DESCRIPTION,
    response_model=OutputText,
    dependencies=[
        Depends(
            RateLimiter(
                times=1,
                seconds=30
            )
        )
    ]
)
def summarize(input_text: InputText):
    summary = generate_summarize(
        text=input_text.text,
        max_length=g.settings.max_length,
        min_length=g.settings.min_length,
        tokenizer=g.tokenizer,
        model=g.model
    )

    return OutputText(text=summary)
