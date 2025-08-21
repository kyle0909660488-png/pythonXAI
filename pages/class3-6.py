import random  # 內建套件: 提供產生亂數的功能
import streamlit as st  # streamlit 用來建立簡單的網頁互動介面

# from streamlit import session_state as ss
# 簡短名稱: 使用 session_state 儲存跨互動的狀態
import time  # 提供 sleep 等時間相關工具

ss = st.session_state
# --- 初始化 session 狀態（只在第一次載入時建立預設值）
if "ans" not in ss:  # 如果 session_state 中沒有儲存答案
    # 將答案設定為 1 到 100 的隨機整數, 並儲存在 session 中以保持跨次互動的狀態
    ss.ans = random.randint(1, 100)

if "max_num" not in ss:  # 如果沒有設定最大可猜數值
    ss.max_num = 100  # 初始上限為 100

if "min_num" not in ss:  # 如果沒有設定最小可猜數值
    ss.min_num = 1  # 初始下限為 1


# --- UI: 標題與輸入元件
st.title("猜數字遊戲")  # 在頁面顯示標題

# number_input 會顯示一個數字輸入框, step=1 表示每次增加/減少為 1
# 使用 f-string 顯示目前允許的範圍 (min 到 max)
num = st.number_input(f"請輸入 {ss.min_num} 到 {ss.max_num} 的整數：", step=1)

# 當使用者按下「猜」的按鈕時, 進入判斷流程
if st.button("猜"):
    # 如果輸入比答案大
    if num > ss.ans:
        st.write("太大了！")  # 顯示提示文字給使用者
        # 如果使用者輸入的數字比目前的上限還小, 則可以把上限縮小到使用者輸入的值
        # 這會讓下一次使用者輸入時, 輸入欄位的提示範圍更精準
        if num < ss.max_num:
            ss.max_num = num  # 更新 session 中的最大可猜數值

    # 如果輸入比答案小
    elif num < ss.ans:
        st.write("太小了！")  # 顯示提示文字給使用者
        # 如果使用者輸入的數字比目前的下限還大, 則可以把下限提高到使用者輸入的值
        if num > ss.min_num:
            ss.min_num = num  # 更新 session 中的最小可猜數值

    # 使用者猜中答案
    else:
        st.write("恭喜你！")  # 顯示猜對訊息
        st.balloons()  # streamlit 的慶祝動畫

    # 等候一秒, 讓使用者看到提示或動畫，再重新執行頁面以更新顯示的範圍
    time.sleep(1)
    st.rerun()  # 重新執行應用程式使變更生效
