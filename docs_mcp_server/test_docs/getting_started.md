# Getting Started

This guide will help you get started with our product.

## Installation

To install the product, run the following command:

```bash
pip install our-product
```

## Configuration

Create a configuration file at `~/.config/our-product/config.yaml` with the following content:

```yaml
api_key: your-api-key
endpoint: https://api.example.com
timeout: 30
```

## Usage

Here's a simple example of using the product:

```python
from our_product import Client

client = Client()
result = client.process("Hello, world!")
print(result)
```

## Next Steps

- Read the [API Reference](api_reference.md)
- Check out the [Examples](examples.md)
- Join our [Community](community.md)
