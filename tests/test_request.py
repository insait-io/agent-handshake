import json
import pytest
from src.api_contract_validator import validate_request
from pydantic import ValidationError

EXAMPLE_PATH = "examples/request-valid.json"

def test_valid_request_passes():
    with open(EXAMPLE_PATH) as f:
        data = json.load(f)
    model = validate_request(data)
    assert model.conversation_id
    assert model.last_message == "Hello!"

def test_missing_nullable_key_fails():
    with open(EXAMPLE_PATH) as f:
        data = json.load(f)
    data.pop("task_prompt", None)
    with pytest.raises(ValidationError):
        validate_request(data)
