import os
import requests
from dotenv import load_dotenv

load_dotenv()

class TMDBClient:
    def __init__(self):
        self.api_key = os.getenv("TMDB_API_KEY")
        self.base_url = "https://api.themoviedb.org/3"

        if not self.api_key:
            raise ValueError("ERROR: API key do not found in .env")
    
    def search_tv_show(self, query):
        """ 
        Looks for a series by its name.
        Returns the dictionary of the first series found or None.
        """
        endpoint = f"{self.base_url}/search/tv"
        params = {
            "api_key": self.api_key,
            "query": query,
            # "language": "pt-BR"
            "language": "en-US"
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status() #Throws error - goes to except

            data = response.json()

            if data['results']:
                return data['results'][0] #First index (0) is the most relevant
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error on API conection: {e}")
            return None
        
    def get_show_details(self, show_id):
        endpoint = f"{self.base_url}/tv/{show_id}"
        params = {
            "api_key": self.api_key,
            # "language": "pt-BR"
            "language": "en-US"
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status() #Throws error - goes to except

            data = response.json()

            if data['results']:
                return data['results'][0] ##First index (0) is the most relevant
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error looking for show's details (ID {show_id}): {e}")
            return None