import asyncio
import websockets


async def chat():
    uri = "ws://127.0.0.1:8000/ws/chat"
    async with websockets.connect(uri) as websocket:
        print("Connected to chat server.")

        async def send():
            while True:
                message = 'new hello'
                await websocket.send(message)

        async def receive():
            while True:
                response = await websocket.recv()
                print(f"Friend: {response}")

        await asyncio.gather(send(), receive())


if __name__ == "__main__":
    asyncio.run(chat())
