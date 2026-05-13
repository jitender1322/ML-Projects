from pydantic import BaseModel
from typing import List


class GrammarFeedback(BaseModel):
    wrong: str
    correct: str
    message: str


class GrammarAnalysisResponse(BaseModel):
    original_text: str
    corrected_text: str
    fluency_score: int
    grammar_feedback: List[GrammarFeedback]
    vocabulary_suggestions: List[str]