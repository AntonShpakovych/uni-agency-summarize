from pydantic import BaseModel, Field

from docs import summarize


class InputText(BaseModel):
    text: str = Field(min_length=150, example=summarize.INPUT_EXAMPLE)


class OutputText(BaseModel):
    text: str = Field(example=summarize.OUTPUT_EXAMPLE)
