import requests

BASE_URL = "https://cpmnuker.anasov.ly/api"

class CPMNuker:

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    def _post(self, endpoint, data=None):
        payload = {
            "account_email": self.email,
            "account_password": self.password
        }
        if data:
            payload.update(data)
        response = requests.post(f"{BASE_URL}/{endpoint}", data=payload)
        return response.json()

    def login(self) -> int:
        response_decoded = self._post("account_login")
        return response_decoded.get("error")
    
    def register(self) -> int:
        response_decoded = self._post("account_register")
        return response_decoded.get("error")
    
    def delete(self):
        self._post("account_delete")

    def get_player_data(self) -> any:
        return self._post("get_data")
    
    def set_player_rank(self) -> bool:
        response_decoded = self._post("set_rank")
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        response = requests.get(f"{BASE_URL}/get_key_data")
        return response.json()
    
    def set_player_money(self, amount) -> bool:
        response_decoded = self._post("set_money", {"amount": amount})
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        response_decoded = self._post("set_coins", {"amount": amount})
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        response_decoded = self._post("set_name", {"name": name})
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        response_decoded = self._post("set_id", {"id": id})
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        response_decoded = self._post("set_plates")
        return response_decoded.get("ok")
    
    def get_player_car(self, car_id) -> any:
        response_decoded = self._post("get_car", {"car_id": car_id})
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        response_decoded = self._post("delete_friends")
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        response_decoded = self._post("unlock_w16")
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        response_decoded = self._post("unlock_horns")
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        response_decoded = self._post("disable_damage")
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        response_decoded = self._post("unlimited_fuel")
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        response_decoded = self._post("set_race_wins", {"amount": amount})
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        response_decoded = self._post("set_race_loses", {"amount": amount})
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        response_decoded = self._post("unlock_houses")
        return response_decoded.get("ok")
    
    def unlock_smoke(self) -> bool:
        response_decoded = self._post("unlock_smoke")
        return response_decoded.get("ok")
    
    def unlock_paid_cars(self) -> bool:
        response_decoded = self._post("unlock_paid_cars")
        return response_decoded.get("ok")
    
    def unlock_all_cars(self) -> bool:
        response_decoded = self._post("unlock_all_cars")
        return response_decoded.get("ok")
    
    def unlock_all_cars_siren(self) -> bool:
        response_decoded = self._post("unlock_all_cars_siren")
        return response_decoded.get("ok")
    
    def account_clone(self, account_email, account_password) -> bool:
        response_decoded = self._post("clone", {
            "account_email": account_email, 
            "account_password": account_password
        })
        return response_decoded.get("ok")