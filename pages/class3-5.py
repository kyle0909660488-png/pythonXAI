import random  # 匯入 random 模組以產生亂數
import streamlit as st  # 匯入 streamlit 用於建立網頁互動介面

# 初始化遊戲狀態，儲存在 st.session_state 中以維持頁面重新整理後的狀態
if "answer" not in st.session_state:
    # 電腦隨機想一個 1 到 100 的數字作為答案
    st.session_state.answer = random.randint(1, 100)
    st.session_state.min_num = 1  # 當前可猜的最小值
    st.session_state.max_num = 100  # 當前可猜的最大值
    st.session_state.message = "電腦心裡想了一個 1 到 100 的數字，快來猜猜看！"

# 顯示目前可猜的範圍，使用 f-string 插入變數
st.write(
    f"現在你可以輸入 **{st.session_state.min_num} 到 {st.session_state.max_num}** 之間的數字"
)

# 使用者輸入數字，st.number_input 會回傳數字（此處設定 min/max 與 step）
num = st.number_input("請輸入你猜的數字：", min_value=1, max_value=100, step=1)

# 當使用者按下「送出答案」按鈕時，檢查輸入與答案的大小關係
if st.button("送出答案"):
    if num > st.session_state.answer:
        st.session_state.message = "太大了！再小一點～"  # 提示太大
        # 若輸入值小於目前的上限，可縮小上限範圍
        if num < st.session_state.max_num:
            st.session_state.max_num = num
    elif num < st.session_state.answer:
        st.session_state.message = "太小了！再大一點～"  # 提示太小
        # 若輸入值大於目前的下限，可提高下限範圍
        if num > st.session_state.min_num:
            st.session_state.min_num = num
    else:
        st.session_state.message = "🎉 恭喜你猜對了！"  # 猜中顯示成功訊息

# 用 subheader 顯示目前的提示訊息
st.subheader(st.session_state.message)

# 重新開始遊戲按鈕：重置 session_state 中的遊戲相關變數，並重新執行頁面
if st.button("重新開始"):
    st.session_state.answer = random.randint(1, 100)
    st.session_state.min_num = 1
    st.session_state.max_num = 100
    st.session_state.message = "電腦心裡想了一個 1 到 100 的數字，快來猜猜看！"
    st.experimental_rerun()
