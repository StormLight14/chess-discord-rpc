from pypresence import Presence
import time
import requests

client_id = "1079473290462117920"
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

start = int(time.time())

rapid_rating = 9999
blitz_rating = 9999
bullet_rating = 9999

while True:  # The presence will stay on as long as the program is running
    for i in range(1000):
        if i == 1:
            response = requests.get(
                "https://api.chess.com/pub/player/stormlightnoway/stats").json()

            # response = json.load(response)
            rapid_rating = response["chess_rapid"]["last"]["rating"]
            blitz_rating = response["chess_blitz"]["last"]["rating"]
            bullet_rating = response["chess_bullet"]["last"]["rating"]

        RPC.update(details=f"Rapid ELO: {rapid_rating}", start=start, large_image="large", buttons=[
            {"label": "My Lichess Profile", "url": "https://lichess.org/@/Stormlightnoway"}, {"label": "My Chess.com Profile", "url": "https://www.chess.com/member/stormlightnoway"}])  # Set the presence

        start = start
        time.sleep(1)
