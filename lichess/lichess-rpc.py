from pypresence import Presence
import time
import requests

client_id = "1079473450269286541"
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

start = int(time.time())

rapid_rating = 9999
blitz_rating = 9999
bullet_rating = 9999
status = "Idle"

username = "Stormlightnoway"

# do not make this too low, avoid spamming lichess.org api.
sleep_time = 20

api_delay = sleep_time * (sleep_time * 2)

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def current_game_elo(speed, bullet, blitz, rapid):
    if speed == "bullet":
        return f"Bullet rating: {bullet}"
    if speed == "blitz":
        return f"Blitz rating: {blitz}"
    if speed == "rapid":
        return f"Rapid rating: {rapid}"


while True:
    for i in range(api_delay):
        # occasionally check lichess.org elo
        if i == 0:
            stats = requests.get(
                f"https://lichess.org/api/user/{username}/rating-history"
            ).json()

            bullet_rating = stats[0]["points"][0][3]
            blitz_rating = stats[0]["points"][1][3]
            rapid_rating = stats[2]["points"][0][3]

        try:
            currently_playing = requests.get(
                f"https://lichess.org/api/users/status?ids={username}"
            ).json()[0]["playing"]
        except:
            currently_playing = False

        current_game = requests.get(
            f"https://lichess.org/api/user/{username}/current-game", headers=headers
        ).json()
        white_player = current_game["players"]["white"]["user"]["name"]
        black_player = current_game["players"]["black"]["user"]["name"]
        if currently_playing == True:
            speed = current_game["speed"]
        else:
            speed = "rapid"

        if currently_playing:
            if white_player == username:
                opponent = black_player
                side = "White"
            else:
                opponent = white_player
                side = "Black"
            status = f"Playing {speed} vs {opponent}"
        else:
            status = "Idle"

        print(status)

        RPC.update(details=f"{current_game_elo(speed, bullet_rating, blitz_rating, rapid_rating)}", state=status, start=start, large_image="large", buttons=[
            {"label": "My Lichess Profile", "url": f"https://lichess.org/@/{username}"}, {"label": "My Chess.com Profile", "url": f"https://www.chess.com/member/{username}"}])

        time.sleep(sleep_time)
        start = start
