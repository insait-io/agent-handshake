# insait-agent-handsahke SDK Documentation

## Overview
`insait-agent-handsahke` is a minimal Python package for validating API request payloads against a strict contract. It uses Pydantic v2 for runtime validation and provides both a Python API and a CLI.

## Installation
```sh
pip install -e .
```

## Usage
### Python API
```python
from insait_agent_handsahke import validate_request

payload = {...}  # dict or JSON string
model = validate_request(payload)
# model is a RequestModel instance
```

#### Function: `validate_request`
```python
def validate_request(payload: dict | str) -> RequestModel
```
- **payload**: A Python dict or JSON string matching the contract.
- **Returns**: A validated `RequestModel` instance.
- **Raises**: `pydantic.ValidationError` if validation fails.

### CLI
```sh
python -m insait_agent_handsahke validate path/to/request.json
python -m insait_agent_handsahke --print-schema
```

## Model Reference
### `RequestModel`
- `conversation_id: UUID` — Conversation UUID
- `user_id: UUID` — User UUID
- `conversation_history: list[HistoryItem]` — List of history items
- `last_message: str | None` — Last message (nullable)
- `query: str` — Query string
- `task_prompt: str | None` — Task prompt (nullable)
- `timestamp: datetime` — Timestamp

#### `HistoryItem`
- `timestamp: datetime` — Message timestamp
- `sender: str` — Sender name
- `message: str` — Message content

## Validation Rules
- All required keys must be present, including nullable ones (`last_message`, `task_prompt`).
- Extra fields are allowed.
- Validation errors are raised as `pydantic.ValidationError`.

## Example
```python
from insait_agent_handsahke import validate_request

payload = {
    "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
    "user_id": "123e4567-e89b-12d3-a456-426614174001",
    "conversation_history": [
        {"timestamp": "2025-09-02T12:00:00Z", "sender": "user", "message": "Hello!"}
    ],
    "last_message": "Hello!",
    "query": "What is the weather?",
    "task_prompt": None,
    "timestamp": "2025-09-02T12:00:01Z"
}
model = validate_request(payload)
print(model.model_dump_json(indent=2))
```

## License
MIT
