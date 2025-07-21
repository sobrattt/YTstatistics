from flask import Blueprint, redirect, request, render_template
from app.storage import token_storage
router = Blueprint("main", "main")

@router.route("/")
def main_page_handler():
    channel_title = token_storage.keys()
    return render_template("main.html", accounts=channel_title)
