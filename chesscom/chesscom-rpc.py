from pypresence import Presence
import time, requests, datetime

client_id = "1079473290462117920"
RPC = Presence(client_id)
RPC.connect()

start = int(time.time())

today = datetime.date.today()
month = f'{today.month:02d}'

rapid_rating = 9999
blitz_rating = 9999
bullet_rating = 9999

username = "Stormlightnoway"

# do not make this too low, don't spam chess.com api.
sleep_time = 20

api_delay = sleep_time * (sleep_time * 2)

while True:
    for i in range(api_delay):
        # add a pretty big delay to checking elo stats
        if i == 0:
            stats = requests.get(
                f"https://api.chess.com/pub/player/{username}/stats"
                ).json()
            
            
            rapid_rating = stats["chess_rapid"]["last"]["rating"]
            blitz_rating = stats["chess_blitz"]["last"]["rating"]
            bullet_rating = stats["chess_bullet"]["last"]["rating"]

        # get the player's current game(s), check more often than stats
        current_playing = requests.get(
                f"https://api.chess.com/pub/player/{username}/games/{today.year}/{month}"
            ).json()
        print(len(current_playing))

        RPC.update(details=f"Rapid ELO: {rapid_rating}", start=start, large_image="large", buttons=[
            {"label": "My Lichess Profile", "url": f"https://lichess.org/@/{username}"}, {"label": "My Chess.com Profile", "url": f"https://www.chess.com/member/{username}"}])  # Set the presence

        start = start
        time.sleep(sleep_time)
