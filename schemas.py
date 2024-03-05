from pydantic import BaseModel, Field

from docs import summarize


class InputText(BaseModel):
    text: str = Field(
        min_length=summarize.MIN_LENGTH_SCHEMA_INPUT_TEXT,
        example=summarize.INPUT_EXAMPLE
    )


class OutputText(BaseModel):
    text: str = Field(example=summarize.OUTPUT_EXAMPLE)
