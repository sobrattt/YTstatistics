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

def request_analytics(token, channel_id, metrics, start_date, end_date):
    response = requests.get(
        url="https://youtubeanalytics.googleapis.com/v2/reports",
        headers={
            "Authorization": f"Bearer {token}"
        },
        params={
            "ids": f"channel=={channel_id}",
            "metrics": ",".join(metrics),
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": "day"
        }
    )

    return response.json()



