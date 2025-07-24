import redis
from typing import Any

class RedisService:
    def __init__(self, host: str, port: int):
        self.client = redis.Redis(host=host, port=port)

    def get(self, key: str) -> Any:
        return self.client.get(key)

    def set(self, key: str, value: Any, ex: int = None):
        self.client.set(key, value, ex=ex)
