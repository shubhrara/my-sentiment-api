from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

positive_words = {
    "love", "great", "excellent", "amazing", "awesome",
    "happy", "wonderful", "fantastic", "good", "best",
    "like", "enjoy"
}

negative_words = {
    "hate", "terrible", "awful", "bad", "worst",
    "sad", "angry", "disappointed", "horrible",
    "poor", "upset"
}

@app.post("/sentiment")
async def sentiment(req: SentimentRequest):
    results = []

    for sentence in req.sentences:
        text = sentence.lower()

        pos = sum(word in text for word in positive_words)
        neg = sum(word in text for word in negative_words)

        if pos > neg:
            label = "happy"
        elif neg > pos:
            label = "sad"
        else:
            label = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": label
        })

    return {"results": results}
