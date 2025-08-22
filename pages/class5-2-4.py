import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
ss = st.session_state
# 初始化對話紀錄
if "history" not in ss:
    ss.history = [{"role": "system", "content": "請用繁體中文進行後續對話"}]
    # 如果對話紀錄不存在, 創建一個空列表

col_chat, col_clear = st.columns([9, 1])
with col_clear:
    # 新增刪除對話紀錄按鈕,按鈕上的文字不需要直接用 emoji
    if st.button("🗑️"):
        ss.history = [{"role": "system", "content": "請用繁體中文進行後續對話"}]
        st.rerun()
with col_chat:
    # 從對話紀錄中迭代每個訊息並顯示
    for message in ss.history:
        if message["role"] == "user":  # 如果是使用者訊息
            st.chat_message("user", avatar="👤").write(message["content"])
        if message["role"] == "assistant":  # 如果是 AI 回應
            st.chat_message("assistant", avatar="💻").write(message["content"])

prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話輸入框,等待使用者輸入訊息
if prompt:  # 如果使用者輸入了訊息
    ss.history.append({"role": "user", "content": prompt})  # 將使用者的訊息加入對話紀錄

    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=ss.history,  # 使用聊天歷史紀錄
    )

    assistant_message = response.choices[0].message.content  # 取得AI助手回傳的訊息內容
    ss.history.append({"role": "assistant", "content": assistant_message})
    # 將 AI 助手的訊息加入聊天紀錄
    st.rerun()
