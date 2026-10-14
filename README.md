# Dynamic Chunking and Parsing

A simple and functional Python project for chunking text dynamically and parsing structured data from those chunks.

## Features
- Split text into chunks by character count or token-like segments
- Support overlap between chunks
- Parse chunked output into records using a simple parser
- Includes a working example and tests

## Project structure
```text
dynamic-chunking-parsing/
├── chunking/
│   ├── __init__.py
│   ├── chunker.py
│   └── parser.py
├── examples/
│   └── sample_usage.py
├── tests/
│   └── test_chunking.py
├── README.md
├── requirements.txt
└── setup.py
```

## Install
```bash
pip install -r requirements.txt
```

## Run example
```bash
python examples/sample_usage.py
```

## Example output
```python
chunks = dynamic_chunk(text, chunk_size=80, overlap=20)
records = parse_records(chunks)
```

## License
MIT
