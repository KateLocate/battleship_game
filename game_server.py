# For this game we need socket connection and two devices for privacy, obviously we don`t want players
# to see each other ship`s positions.
# We can use simple char-filled play fields as in the snake game.
# I will use websockets library for communication.
# I can test client-server interactions on one machine and then move to two/three separate ones.

# First of all we'll use websockets.serve function to be able to get limitless connections from clients.
# Next we need to make our server to let only 2 players connect and wait for each to access it
# one by one sending something.
# After that we will start to describe the game rules and UI.

import websockets
import asyncio


class Game:
    PLAYERS = {'player_1': None, 'player_2': None}  # connections storage

    field_1, field_2 = [['*' * 10] * 10], [['*' * 10] * 10]

    def add_players(self):
        ...

    def autogenerate_ships(self):
        ...

    async def handler(self, websocket):
        user_id = ...  # identify user in your app's context
        self.PLAYERS[user_id] = websocket
        try:
            await websocket.wait_closed()
        finally:
            del self.PLAYERS[user_id]

    def message_all(self, message):
        websockets.broadcast(self.PLAYERS, message)


# websockets usage example
async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
