import json
from categoriser import categorise

def evaluate():
    with open('tests/golden_dataset.json', 'r') as f:
        dataset = json.load(f)

    successes = 0
    failures = 0
    field_matches = 0
    total_fields = 0

    for entry in dataset:
        try:
            result = categorise(entry['task'])
            successes += 1

            # Field accuracy check
            if result.category == entry['expected_category']:
                field_matches += 1
            total_fields += 1
            if result.priority == entry['expected_priority']:
                field_matches += 1
            total_fields += 1

        except Exception as e:
            # Check for API-specific errors to distinguish from parsing failures
            if 'RESOURCE_EXHAUSTED' in str(e) or '503' in str(e) or '504' in str(e):
                print(f"Skipping: {entry['task']} (API error: {e})")
                continue

            underlying_error = e.last_attempt.exception() if hasattr(e, 'last_attempt') else e
            print(f"Failed to parse: {entry['task']}. Error: {underlying_error}")
            failures += 1

    print(f"Schema adherence: {(successes / (len(dataset) - failures - (len(dataset) - successes - failures))) * 100:.2f}%")
    print(f"Field accuracy: {(field_matches / total_fields) * 100:.2f}%")
    print(f"Total failures: {failures}")

if __name__ == "__main__":
    evaluate()
