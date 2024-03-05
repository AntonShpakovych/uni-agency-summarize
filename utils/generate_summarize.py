from transformers import PreTrainedModel, PreTrainedTokenizer


def generate_summarize(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    text: str,
    max_length: int,
    min_length: int
) -> str:
    tokenized_text = tokenizer.encode(text, return_tensors="pt")
    tokens = tokenizer.tokenize(text)

    if len(tokens) > max_length:
        chunk_size = max_length
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

        summaries = []
        for chunk in chunks:
            summary = generate_summarize(
                text=chunk,
                max_length=max_length,
                min_length=min_length,
                model=model,
                tokenizer=tokenizer
            )
            summaries.append(summary)

        final_summary = " ".join(summaries)
        return final_summary
    else:
        summary = model.generate(
            input_ids=tokenized_text,
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            early_stopping=True
        )
        return tokenizer.decode(summary[0], skip_special_tokens=True)
