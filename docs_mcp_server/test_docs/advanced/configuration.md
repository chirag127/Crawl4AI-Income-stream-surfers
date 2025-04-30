# Advanced Configuration

This document provides information about advanced configuration options.

## Configuration File

The configuration file supports the following advanced options:

```yaml
api_key: your-api-key
endpoint: https://api.example.com
timeout: 30
retry:
  max_attempts: 3
  backoff_factor: 2
  status_forcelist: [500, 502, 503, 504]
logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "/path/to/log/file.log"
cache:
  enabled: true
  ttl: 3600
  max_size: 1000
```

## Environment Variables

All configuration options can also be set using environment variables:

```bash
export OUR_PRODUCT_API_KEY=your-api-key
export OUR_PRODUCT_ENDPOINT=https://api.example.com
export OUR_PRODUCT_TIMEOUT=30
export OUR_PRODUCT_RETRY_MAX_ATTEMPTS=3
export OUR_PRODUCT_RETRY_BACKOFF_FACTOR=2
export OUR_PRODUCT_RETRY_STATUS_FORCELIST=500,502,503,504
export OUR_PRODUCT_LOGGING_LEVEL=INFO
export OUR_PRODUCT_LOGGING_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
export OUR_PRODUCT_LOGGING_FILE=/path/to/log/file.log
export OUR_PRODUCT_CACHE_ENABLED=true
export OUR_PRODUCT_CACHE_TTL=3600
export OUR_PRODUCT_CACHE_MAX_SIZE=1000
```

## Programmatic Configuration

You can also configure the client programmatically:

```python
from our_product import Client, RetryConfig, LoggingConfig, CacheConfig

retry_config = RetryConfig(
    max_attempts=3,
    backoff_factor=2,
    status_forcelist=[500, 502, 503, 504]
)

logging_config = LoggingConfig(
    level="INFO",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    file="/path/to/log/file.log"
)

cache_config = CacheConfig(
    enabled=True,
    ttl=3600,
    max_size=1000
)

client = Client(
    api_key="your-api-key",
    endpoint="https://api.example.com",
    timeout=30,
    retry_config=retry_config,
    logging_config=logging_config,
    cache_config=cache_config
)
```
