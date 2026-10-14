from chunking import dynamic_chunk, parse_records


def test_dynamic_chunk_basic():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunks = dynamic_chunk(text, chunk_size=5, overlap=2)
    assert len(chunks) > 0
    assert all(len(chunk) <= 5 for chunk in chunks)


def test_parse_records():
    chunks = ["one", "two", "three"]
    records = parse_records(chunks)
    assert len(records) == 3
    assert records[0]["content"] == "one"


def test_overlap_behavior():
    text = "abcdefghijklm"
    chunks = dynamic_chunk(text, chunk_size=6, overlap=2)
    assert len(chunks) >= 2
    assert chunks[0][:2] == "ab"
