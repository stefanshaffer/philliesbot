import requests
import random
import tkinter as tk

API_KEY = "f9530621486645bf88b923e517024fb6"  # Replace with your SportsDataIO API key
TEAM_CODE = "PHI"

def get_phillies_players():
    endpoint = f"https://api.sportsdata.io/v3/mlb/scores/json/PlayersBasic/{TEAM_CODE}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Ocp-Apim-Subscription-Key": API_KEY
    }

    response = requests.get(endpoint, headers=headers)
    

    if response.status_code == 200:
        data = response.json()
        data = {"data" : data}
        return data
    else:
        print("Error fetching Phillies player data.")
        print(response.status_code)
        return None
if __name__ == "__main__":
    players_data = get_phillies_players()

    if players_data:
        # Create an empty dictionary to store player information
        phillies_players = {}

        # Extract and process player information
        for player in players_data['data']:
            player_status = player.get('Status')
            player_first_name = player.get('FirstName' , '')
            player_last_name = player.get('LastName' , '')
            player_position = player.get('Position')
            player_hometown = player.get('BirthCity')
            player_name = player_first_name + " " + player_last_name
    

            # Store player information in the dictionary
            if player_status == "Active":
                player_info = {
                    'Status': player_status,
                    'Name': player_name,
                    'Height': player_position,
                    'Hometown': player_hometown
                }
                phillies_players[player_name] = player_info

    window = tk.Tk()
    window.title("Random Active Phillie")
    label = tk.Label(window, text="Placholder", font=("Arial", 12), fg ="black" )
    label.pack()

    # Create a label to display the selected player's name
    
    def get_random_phillie():
        phillies_names = list(phillies_players.keys())
        random_player = random.choice(phillies_names)
        label.config(text=f"Random Active Phillie: {random_player}")
        print(random_player)

    # Create a button
    button = tk.Button(window, text="Get Random Active Phillie", command=get_random_phillie)
    button.pack()

    # Start the Tkinter event loop
    window.mainloop()


