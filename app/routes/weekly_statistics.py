from flask import Blueprint, redirect, request, render_template
from app.storage import token_storage
from app.api.youtube_data_api import request_analytics
from app.utils import transform_analytic_response, get_time_gaps, calculate_averages



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
    averages_current[0] = f"Current week: {start} - {end}"
    data_last, averages_last = transform_analytic_response(analytics_last_week)
    averages_last[0] = f"Last week: {start_last} - {end_last}"
    headers_last = data_last[0]
    headers_last[0] = "period"
    difference = calculate_averages(averages_current[1:], averages_last[1:])
    return render_template("table_weekly.html", headers=headers_last, averages_1=averages_current, averages_2=averages_last, difference=difference)

