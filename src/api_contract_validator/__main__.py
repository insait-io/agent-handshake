import argparse
import sys
import json
from pathlib import Path
from .validate import validate_request
from .model import RequestModel

SCHEMA_PATH = Path(__file__).parent / "schemas" / "request.schema.json"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("validate", nargs="?", help="Validate a request JSON file.")
    parser.add_argument("file", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("--print-schema", action="store_true", help="Print the request JSON schema.")
    args = parser.parse_args()

    if args.print_schema:
        print(SCHEMA_PATH.read_text())
        return

    if args.validate and args.file:
        try:
            with open(args.file) as f:
                data = json.load(f)
            model = validate_request(data)
            print(model.model_dump_json(indent=2))
            sys.exit(0)
        except Exception as e:
            print(f"Validation error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
