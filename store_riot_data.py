import requests

# Riot API setup
api_key = "RGAPI-222443a5-e998-4954-b18a-8ca56ec34231"
country = "americas"
account_name = "DanJam"
tagline = "NA1"

def get_account_puuid(account_name, tagline):
    account_url = f"https://{country}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{account_name}/{tagline}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(account_url, headers=headers)
    if response.status_code == 200:
        return response.json().get("puuid")
    else:
        print(f"Failed to fetch account data: {response.status_code} - {response.text}")
        return None

def get_league_summoner_data(puuid, region):
    summoner_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    print(summoner_url)
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(summoner_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch league summoner data: {response.status_code} - {response.text}")
        return None

def get_league_rank_info(league_summoner_id, region):
    rank_url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{league_summoner_id}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(rank_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch rank data: {response.status_code} - {response.text}")
        return None
    
def get_tft_summoner_data(puuid, region):
    summoner_url = f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{puuid}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(summoner_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch tft summoner data: {response.status_code} - {response.text}")
        return None

def get_tft_rank_info(tft_summoner_id, region):
    tft_rank_url = f"https://{region}.api.riotgames.com/tft/league/v1/entries/by-summoner/{tft_summoner_id}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(tft_rank_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch TFT rank data: {response.status_code} - {response.text}")
        return None


def main(account_name, tagline, region):
    puuid = get_account_puuid(account_name, tagline)
    if puuid:
        print(puuid)
        league_summoner_data = get_league_summoner_data(puuid, region)
        tft_summoner_data = get_tft_summoner_data(puuid, region)

        if league_summoner_data:
            summoner_id = league_summoner_data['id']
            league_ranks = get_league_rank_info(summoner_id, region)
            print("League of Legends Ranks:", league_ranks)

        if tft_summoner_data:
            tft_ranks = get_tft_rank_info(summoner_id, region)
            print("TFT Ranks:", tft_ranks)

if __name__ == "__main__":
    region = "NA1" 
    main(account_name, tagline, region)
