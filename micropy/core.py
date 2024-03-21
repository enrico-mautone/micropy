from fastapi import FastAPI, Request
from enum import Enum, auto

class HttpMethod(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    # Aggiungi altri metodi HTTP se necessario

class MicroserviceBuilder:
    def __init__(self):
        self.app = FastAPI()
        self.endpoints = []

    def add_endpoint(self, path: str, method: HttpMethod, func):
        if method == HttpMethod.GET:
            self.app.get(path)(func)
        elif method == HttpMethod.POST:
            self.app.post(path)(func)
        # Aggiungi il supporto per altri metodi HTTP qui
        self.endpoints.append((path, method, func))
        return self

    def build(self):
        return self.app

