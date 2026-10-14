def dynamic_chunk(text, chunk_size=200, overlap=0):
    """Split text into chunks with optional overlap.

    Args:
        text (str): source text
        chunk_size (int): maximum characters per chunk
        overlap (int): number of characters shared between chunks

    Returns:
        list[str]: list of text chunks
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if not text:
        return []

    step = chunk_size - overlap
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        if end >= len(text):
            break
        start += step

    return chunks
