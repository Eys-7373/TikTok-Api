import requests
import time
# 設定你的 TikTok 使用者名稱
TIKTOK_USERNAME = "wei_0510"
# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1338724556717949008/8o_OdJ3r3wwMILiolG3vbvZDNzXE1K8KrTx204Ql0IIjcWZ5meEngYWhRUFQR9mly1qG"
def check_live_status():
    url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}/live"
    response = requests.get(url)
    if "LIVE" in response.text:  # 偵測 TikTok 直播頁面關鍵字
        return True
    return False
def send_discord_notification():
    data = {
        "content": f"🚀 @everyone {睿} 開始直播了！快來觀看！\n🔗 https://www.tiktok.com/@{wei_0510}/live"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)
while True:
    if check_live_status():
        send_discord_notification()
    time.sleep(60)  # 每 60 秒檢查一次
