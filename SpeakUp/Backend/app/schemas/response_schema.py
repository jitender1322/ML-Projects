from pydantic import BaseModel
from typing import Optional

from app.schemas.grammar_schema import GrammarAnalysisResponse


class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[GrammarAnalysisResponse] = None