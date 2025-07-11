import json

class BankDatabase:
    def __init__(self, filename="users.json"):
        self.filename = filename

    def save_users(self, user_dict):
        with open(self.filename, "w") as f:
            json.dump(user_dict, f, indent=4)

    def load_users(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}