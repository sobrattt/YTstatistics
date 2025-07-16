from flask import Blueprint, redirect, request
from app.utils import get_credentials


router = Blueprint("oauth", "oauth")

credentials = get_credentials()
client_id = credentials.get("client_id")
auth_uri = credentials.get("auth_uri")
redirect_uris = credentials.get("redirect_uris")
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
    return code
