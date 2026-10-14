def parse_records(chunks):
    """Parse a list of chunks into simple record-like dicts.

    This is intentionally lightweight and can be extended for custom parsing.
    Each chunk is converted into a dict containing the chunk text and a simple
    index field.
    """
    records = []
    for index, chunk in enumerate(chunks, start=1):
        records.append({
            "id": index,
            "content": chunk.strip(),
            "length": len(chunk.strip()),
        })
    return records
