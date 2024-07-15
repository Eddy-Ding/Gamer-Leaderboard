import requests
from pymongo import MongoClient

api_key = "RGAPI-7a8c6d41-610b-4e79-8cb2-073b83b93e3e"
country = "americas"
region = "na1"
ranks = ["challengerleagues", "grandmasterleagues", "masterleagues"]

client = MongoClient("mongodb://localhost:27017/")
db = client.riot_data
collection = db.lol_leaderboard

# Drop the collection before adding new data
collection.drop()

def get_leaderboard(rank):
    url = f"https://{region}.api.riotgames.com/lol/league/v4/{rank}/by-queue/RANKED_SOLO_5x5"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve {rank} leaderboard: {response.status_code}")
        return None

def get_summoner_puuid(summoner_id):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('puuid')
    else:
        print(f"Failed to retrieve puuid for summoner ID {summoner_id}: {response.status_code}")
        return None

def get_summoner_name(puuid):
    url = f"https://{country}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('gameName')
    else:
        print(f"Failed to retrieve game name for PUUID {puuid}: {response.status_code}")
        return None

for rank in ranks:
    leaderboard = get_leaderboard(rank)
    if leaderboard:
        for entry in leaderboard['entries']:
            puuid = get_summoner_puuid(entry['summonerId'])
            if puuid:
                game_name = get_summoner_name(puuid)
                if game_name:
                    entry['rank_type'] = rank
                    entry['puuid'] = puuid
                    entry['game_name'] = game_name
                    print(f"Summoner: {entry['game_name']}, PUUID: {entry['puuid']}, Rank Type: {rank}, LP: {entry['leaguePoints']}, Wins: {entry['wins']}, Losses: {entry['losses']}")
                    collection.insert_one(entry)

print("Leaderboards data has been saved to MongoDB.")
