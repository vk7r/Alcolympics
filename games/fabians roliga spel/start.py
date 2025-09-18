import asyncio
import websockets
import json
import webbrowser
from pathlib import Path
from datetime import date

HOST = "localhost"
PORT = 8765

def create_dummy_gamesession():
    today = date.today().isoformat()
    return [
        {
            "name": "Alice",
            "klunkar_druckna": 2,
            "klunkar_givna": 3,
            "Ws": 1,
            "Ls": 0,
            "games_played": 1,
            "date": today
        },
        {
            "name": "Bob",
            "klunkar_druckna": 1,
            "klunkar_givna": 2,
            "Ws": 0,
            "Ls": 1,
            "games_played": 1,
            "date": today
        },
        {
            "name": "clemens",
            "klunkar_druckna": 1,
            "klunkar_givna": 2,
            "Ws": 0,
            "Ls": 1,
            "games_played": 1,
            "date": today
        }
    ]

async def handle_connection(websocket, gamesession, updated_gamesession_future):
    print("WebSocket connected.")
    await websocket.send(json.dumps({"gamesession": gamesession}))
    async for message in websocket:
        data = json.loads(message)
        print(f"Updated GameSession received: {data}")
        await websocket.send(json.dumps({"status": "ok", "action": "close"}))
        updated_gamesession_future.set_result(data.get("gamesession", gamesession))
        return

async def start_server(gamesession, updated_gamesession_future):
    async with websockets.serve(
        lambda ws: handle_connection(ws, gamesession, updated_gamesession_future), HOST, PORT
    ):
        print(f"Server running at ws://{HOST}:{PORT}")
        await updated_gamesession_future

def start_game(gamesession):
    loop = asyncio.get_event_loop()
    updated_gamesession_future = loop.create_future()

    web_path = Path(__file__).parent / "web" / "index.html"
    if not web_path.exists():
        raise FileNotFoundError(f"Web page not found: {web_path}")

    webbrowser.open(web_path.as_uri())

    try:
        loop.run_until_complete(start_server(gamesession, updated_gamesession_future))
    except KeyboardInterrupt:
        print("Server stopped.")

    return updated_gamesession_future.result()

if __name__ == "__main__":
    dummy_gamesession = create_dummy_gamesession()
    updated_gamesession = start_game(dummy_gamesession)
    print("Final GameSession:", updated_gamesession)