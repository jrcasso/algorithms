import hashlib

class Codec:
    def __init__(self):
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tinyUrl = hashlib.md5(longUrl.encode())
        self.url_map[tinyUrl] = longUrl
        return tinyUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map.get(shortUrl, '')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
