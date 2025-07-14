from flask import Blueprint, redirect

router = Blueprint("oauth", "oauth")

@router.route("/login")
def login():
    return "ok"

