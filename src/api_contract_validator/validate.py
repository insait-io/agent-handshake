import json
from typing import Any, Dict, Union
from .model import RequestModel
from pydantic import ValidationError

def validate_request(payload: Union[Dict[str, Any], str]) -> RequestModel:
    if isinstance(payload, str):
        payload = json.loads(payload)
    return RequestModel.model_validate(payload)
