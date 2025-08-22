import streamlit as st

ss = st.session_state
# 初始化對話紀錄
if "history" not in ss:
    ss.history = []

# 顯示歷史紀錄
for message in ss.history:
    st.chat_message("user", avatar="👤").write(message["content"])

# 聊天輸入框
prompt = st.chat_input("請輸入訊息")
if prompt:
    ss.history.append({"role": "user", "content": prompt})
    st.rerun()  # 重新整理頁面顯示新訊息
