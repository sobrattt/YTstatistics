from flask import Blueprint, redirect, request, render_template
from app.storage import token_storage
from app.api.youtube_data_api import request_analytics
from app.utils import transform_analytic_response, get_time_gaps



router = Blueprint("weeklystatistics", "weeklystatistics")

@router.route("/weeklystatistics", methods=["POST"])
def form_handler():
    response = request.form
    accounts = response.get("accounts")
    metrics = response.getlist("option")
    token = token_storage[accounts]["token"]
    channel_id = token_storage[accounts]["channel_id"]
    start, end, start_last, end_last = get_time_gaps()

    analytics_current_week = request_analytics(
        token, channel_id,
        metrics,
        start,
        end
    )
    analytics_last_week = request_analytics(
        token, channel_id,
        metrics,
        start_last,
        end_last
    )
    data_current, averages_current = transform_analytic_response(analytics_current_week)
    headers_current = data_current[0]

    data_last, averages_last = transform_analytic_response(analytics_last_week)
    headers_last = data_last[0]


    return

