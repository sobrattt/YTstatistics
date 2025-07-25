from flask import Blueprint, redirect, request, render_template
from app.storage import token_storage
from app.api.youtube_data_api import request_analytics
from app.utils import transform_analytic_response
router = Blueprint("statistics", "statistics")

@router.route("/statistics", methods=["POST"])
def form_handler():
    response = request.form
    accounts = response.get("accounts")
    start_date = response.get("start_date")
    end_date = response.get("end_date")
    metrics = response.getlist("option")
    token = token_storage[accounts]["token"]
    channel_id = token_storage[accounts]["channel_id"]
    analytics = request_analytics(token, channel_id, metrics, start_date, end_date)
    data = transform_analytic_response(analytics)
    headers = data[0]
    rows = data[1:]
    return render_template("table.html", headers=headers, rows=rows)