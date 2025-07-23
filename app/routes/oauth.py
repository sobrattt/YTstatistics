from flask import Blueprint, redirect, request
from app.utils import get_credentials
import requests
from app.api.youtube_data_api import get_chanel_info
from app import storage


router = Blueprint("oauth", "oauth")

credentials = get_credentials()
client_id = credentials.get("client_id")
auth_uri = credentials.get("auth_uri")
redirect_uris = credentials.get("redirect_uris")
token_uri = credentials.get("token_uri")
client_secret = credentials.get("client_secret")
scopes = " ".join([
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",
    "https://www.googleapis.com/auth/yt-analytics.readonly"
])
google_oauth_page = f"{auth_uri}?client_id={client_id}&redirect_uri={redirect_uris[0]}&response_type=code&scope={scopes}"

print(google_oauth_page)
@router.route("/login")
def login():

    return redirect(google_oauth_page)

@router.route("/google_auth_code_exchange")
def token_handler():
    code = request.args.get("code")
    response = requests.post(token_uri, data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type" : "authorization_code",
        "redirect_uri": redirect_uris[0]
    })
    token = response.json().get("access_token")
    channel_info = get_chanel_info(token)
    channel = channel_info["items"][0]
    channel_id = channel["id"]
    channel_title = channel["snippet"]["title"]
    storage.token_storage[channel_title] = {
        "channel_id": channel_id,
        "token": token
    }
    print(storage.token_storage)
    return redirect("/")


