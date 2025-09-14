# Development

## Setup

```bash
# Install in development mode
pip install -e ".[dev]"
```

## Testing

```bash
# Run unit tests
pytest tests/test_client.py

# Run integration tests (requires test environment)
pytest tests/test_integration.py
```

### Integration Test Setup

Integration tests require environment variables:

- `TEST_DATAPRESS_API_KEY`: API key for test instance
- `TEST_DATAPRESS_INSTANCE`: Test DataPress instance URL  
- `TEST_DATAPRESS_DATASET_ID`: Dataset ID for testing

## Code Quality

```bash
# Format code
black datapress/ tests/

# Sort imports
isort datapress/ tests/

# Type checking, although the results look very poor if you're coming from Typescript.
mypy datapress/
```

## Features

- **Authentication**: Automatic API key handling from environment variables
- **Dataset Access**: Retrieve dataset information by ID  
- **Dataset Patching**: Modify datasets using JSON Patch operations
- **Chunked Uploads**: Efficient file uploads using 5MB chunks
- **File Downloads**: Download files from datasets with authentication
- **Error Handling**: Comprehensive error handling with detailed error information
- **Type Hints**: Full type annotation support

## API Reference

### DataPressClient

#### `__init__(api_key=None, base_url=None)`

Initialize the client with optional API key and base URL. If not provided, reads from environment variables.

#### `whoami()`

Returns information about the current user including ID, name, email, admin status, and team memberships.

#### `get_dataset(dataset_id)`

Retrieve a dataset by its 5-character ID.

#### `patch_dataset(dataset_id, patch)`

Apply JSON Patch operations to a dataset. Supports all standard operations: add, remove, replace, move, copy, test.

#### `upload_file(dataset_id, file_path, resource_id=None, title=None, description=None, order=None)`

Upload a file to a dataset using chunked uploads. All files are uploaded in 5MB chunks regardless of size.

#### `download_file(dataset_id, resource_id)`

Download a file from a dataset resource with authentication.

## Deployment to pypi

python3 -m build
python -m twine upload dist/*