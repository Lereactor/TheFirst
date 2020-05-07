import asyncio
from asyncio import transports

class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server' #класс сервер
    transport: transports.Transport

class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def __init__(self):
        self.clients = []

    async def create_protocol(self):
        return ClientProtocol()

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            "127.0.0.1",
            8888,
        )

        print("server started...")
        await coroutine.serve_forever()

process = Server()

asyncio.run(process.start())