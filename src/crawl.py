from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    normalized = f"{parsed.netloc}{parsed.path}"
    print(normalized)

    return normalized
