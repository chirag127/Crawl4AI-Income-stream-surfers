# Examples

This document provides examples of using our product in various scenarios.

## Basic Example

```python
from our_product import Client

client = Client()
result = client.process("Hello, world!")
print(result)
```

## Advanced Example

```python
import json
from our_product import Client

# Initialize client with custom settings
client = Client(
    api_key="your-api-key",
    endpoint="https://custom-api.example.com"
)

# Process complex data
data = {
    "text": "Hello, world!",
    "options": {
        "language": "en",
        "format": "json"
    }
}

result = client.analyze(data)

# Save result to file
with open("result.json", "w") as f:
    json.dump(result, f, indent=2)
```

## Batch Processing

```python
from our_product import Client

client = Client()

# Process multiple items
texts = [
    "First item to process",
    "Second item to process",
    "Third item to process"
]

results = []
for text in texts:
    result = client.process(text)
    results.append(result)

# Analyze results
for i, result in enumerate(results):
    print(f"Result {i+1}: {result}")
```

## Error Handling

```python
from our_product import Client, APIError

client = Client()

try:
    result = client.process("Hello, world!")
    print(result)
except APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```
