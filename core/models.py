from pydantic import BaseModel
from typing import List, Optional

class TestCase(BaseModel):
    id: int
    scenario: str
    prompt: str
    expected_behavior: str

class TestResult(BaseModel):
    test_id: int
    scenario: str
    actual_output: str
    score: int
    reasoning: str
    status: str  # PASS / FAIL
