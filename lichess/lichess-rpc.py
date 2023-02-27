from pypresence import Presence
import time
import requests

client_id = "1079473450269286541"
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

start = int(time.time())

time_amount = "0:00"
rapid_rating = 9999

while True:
    for i in range(1000):
        if i == 0:
            response = requests.get(
                "https://lichess.org/api/user/stormlightnoway/rating-history").json()

            rapid_rating = response[2]["points"][0][3]

        RPC.update(details=f"Rapid ELO: {rapid_rating}", start=start, large_image="large", buttons=[
            {"label": "My Lichess Profile", "url": "https://lichess.org/@/Stormlightnoway"}, {"label": "My Chess.com Profile", "url": "https://www.chess.com/member/stormlightnoway"}])  # Set the presence
        time.sleep(1)

        start = start
