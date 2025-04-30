# API Reference

This document provides a reference for all API endpoints and client methods.

## Client

### `Client(api_key=None, endpoint=None)`

Creates a new client instance.

**Parameters:**
- `api_key` (str, optional): API key for authentication. If not provided, will be read from environment variable `OUR_PRODUCT_API_KEY`.
- `endpoint` (str, optional): API endpoint URL. If not provided, will use the default endpoint.

**Returns:**
- A new `Client` instance.

### `Client.process(text)`

Process the given text.

**Parameters:**
- `text` (str): Text to process.

**Returns:**
- `dict`: Processing result.

### `Client.analyze(data)`

Analyze the given data.

**Parameters:**
- `data` (dict): Data to analyze.

**Returns:**
- `dict`: Analysis result.

## REST API

### `POST /api/v1/process`

Process text.

**Request Body:**
```json
{
  "text": "Text to process"
}
```

**Response:**
```json
{
  "result": "Processing result"
}
```

### `POST /api/v1/analyze`

Analyze data.

**Request Body:**
```json
{
  "data": {
    "key": "value"
  }
}
```

**Response:**
```json
{
  "analysis": {
    "key": "analysis value"
  }
}
```
