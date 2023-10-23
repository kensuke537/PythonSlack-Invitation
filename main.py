import requests
import json

# Botトークン
SLACK_BOT_TOKEN = ""

# 招待を送信するチャンネルのID
CHANNEL_ID = ""


# 招待するユーザーのメールアドレスを入力
USER_EMAIL = ""


# Slack APIのusers.lookupByEmailメソッドを使用して、ユーザーIDを取得
def get_user_id():
    url = "https://slack.com/api/users.lookupByEmail"
    headers = {"Authorization": "Bearer " + SLACK_BOT_TOKEN}
    data = {"email": USER_EMAIL}
    response = requests.post(url, headers=headers, data=data)
    response_json = json.loads(response.text)
    user_id = response_json["user"]["id"]
    return user_id

# 招待を送信するSlack APIのURLを作成し、リクエストを送信
def invite_user_to_channel():
    # Botトークンを使用して認証する
    url = "https://slack.com/api/users.identity"
    headers = {"Authorization": "Bearer " + SLACK_BOT_TOKEN}
    response = requests.get(url, headers=headers)

    # ユーザーIDを取得
    user_id = get_user_id()

    # チャンネルにユーザーを招待する
    url = "https://slack.com/api/conversations.invite"
    headers = {"Authorization": "Bearer " + SLACK_BOT_TOKEN}
    data = {"channel": CHANNEL_ID, "users": user_id}
    response = requests.post(url, headers=headers, data=data)
    response_json = json.loads(response.text)
    return response_json

# ユーザーを招待する
invite_user_to_channel()
