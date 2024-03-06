from fastapi import HTTPException
from langdetect import detect
from starlette import status

import docs.summarize
from schemas import InputText


def get_english_text(input_data: InputText) -> str:
    if detect(input_data.text) != docs.summarize.REQUIRED_LANGUAGE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=docs.summarize.ERROR_MESSAGE_FOR_LANGUAGE
        )
    return input_data.text
