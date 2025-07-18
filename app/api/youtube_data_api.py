import requests

def get_chanel_info(token):
    response = requests.get(
        url="https://www.googleapis.com/youtube/v3/channels",
        params={
            "part": "snippet",
            "mine": True
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    return response.json()

