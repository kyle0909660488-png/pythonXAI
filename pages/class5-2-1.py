import openai  # pip install openai -U
from dotenv import load_dotenv  # pip install python-dotenv -U
import os

load_dotenv()  # 載入 .env 檔案內容

# 設定 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")
history = [
    {"role": "system", "content": "請用繁體中文進行後續對話"}
]  # 初始化聊天歷史紀錄

while True:
    user_input = input("你：")  # 終端機輸入使用者訊息
    if user_input == "exit":
        break

    history.append({"role": "user", "content": user_input})  # 將使用者訊息加入歷史紀錄
    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=history,  # 使用聊天歷史紀錄
    )

    assistant_message = response.choices[0].message.content
    history.append(
        {"role": "assistant", "content": assistant_message}
    )  # 將 AI 回應加入歷史紀錄
    print(f"AI: {assistant_message}")
