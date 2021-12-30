from requests import post

class Notification:
    
    token = "Token {}"
    url = "https://api.pushe.co/v2/messaging/notifications"

    def __init__(self, user, app_id, auth_token):
        self.__user = user
        self.__app_id = app_id
        self.__auth_token = auth_token

        assert app_id, "app_id is required"
        assert auth_token, "auth_token is required"

    def send(self, title, content):
        
        headers = {
            "Authorization": self.token.format(self.__auth_token),
            "Content-Type": "application/json"
        }

        payload = {
            "app_ids": self.__app_id,
            "data": {
                "title": title,
                "content": content
            },
            "filters": {
                "device_id": [self.__user.device_id]
            }
        }

        try:
            res = post(self.url, json=payload, headers=headers)
        except Exception as exc:
            print(f"could not send push notification, exc: {exc}")
        else:
            print(f"successfully sent notification to {self.__user.username}")