INPUT_EXAMPLE = (
    "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, "
    "and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on "
    "each side. During its construction, the Eiffel Tower surpassed the Washington Monument to "
    "become the tallest man-made structure in the world, a title it held for 41 years until the "
    "Chrysler Building in New York City was finished in 1930. It was the first structure to reach "
    "a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower "
    "in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, "
    "the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
)
OUTPUT_EXAMPLE = (
    "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. "
    "Its base is square, measuring 125 metres (410 ft) on each side. During its construction, "
    "the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world."
)
DESCRIPTION = "Provide summary for your text [ONLY ENGLISH]."
MIN_LENGTH_SCHEMA_INPUT_TEXT = 150
RATE_LIMITER_TIMES = 1
RATE_LIMITER_SECONDS = 30
REQUIRED_LANGUAGE = "en"
ERROR_MESSAGE_FOR_LANGUAGE = "Only English is allowed"
