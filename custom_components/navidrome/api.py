import hashlib
import secrets
import string
import requests


class NavidromeAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password

    def _generate_token(self):
        alphabet = string.ascii_letters + string.digits
        salt = ''.join(secrets.choice(alphabet) for _ in range(16))
        token = hashlib.md5((self.password + salt).encode()).hexdigest()
        return salt, token

    def _request(self, endpoint, params=None):
        salt, token = self._generate_token()

        base_params = {
            "u": self.username,
            "t": token,
            "s": salt,
            "v": "1.16.1",
            "c": "homeassistant",
            "f": "json"
        }

        if params:
            base_params.update(params)

        url = f"{self.base_url}/rest/{endpoint}"

        response = requests.get(url, params=base_params, timeout=10)
        response.raise_for_status()

        return response.json()

    def get_now_playing(self):
        data = self._request("getNowPlaying.view")
        return data.get("subsonic-response", {}).get("nowPlaying", {}).get("entry", [])

    def get_scan_status(self):
        data = self._request("getScanStatus.view")
        return data.get("subsonic-response", {}).get("scanStatus", {})

    def get_system_info(self):
        data = self._request("ping.view")
        return data.get("subsonic-response", {})

    def start_scan(self):
        return self._request("startScan.view")
    
    def get_genres(self):
        data = self._request("getGenres.view")
        return data.get("subsonic-response", {}).get("genres", {}).get("genre", [])

    def get_artists(self):
        data = self._request("getArtists.view")
        return data.get("subsonic-response", {}).get("artists", {}).get("index", [])

    def next(self, player_id):
        return self._request("next.view", {"id": player_id})

    def previous(self, player_id):
        return self._request("previous.view", {"id": player_id})