from chunking import dynamic_chunk, parse_records

sample_text = (
    "This is a sample document for dynamic chunking. "
    "It contains multiple sentences that can be split into manageable chunks. "
    "The goal is to keep each chunk useful and readable while preserving context. "
    "This is a simple but effective parsing workflow for text processing tasks."
)

chunks = dynamic_chunk(sample_text, chunk_size=80, overlap=20)
records = parse_records(chunks)

for record in records:
    print(f"Record {record['id']}: {record['content']}")
    print(f"Length: {record['length']}")
    print("-" * 40)
