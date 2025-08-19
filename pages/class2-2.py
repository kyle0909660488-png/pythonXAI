import streamlit as st  # 匯入 streamlit 並取別名為 st，用於建立簡單的網頁介面

# number_input() 會顯示一個數字輸入欄位
# step 參數定義每次增減的步長，min_value 與 max_value 定義可輸入的最小/最大值
number = st.number_input("請輸入密碼:", step=1, min_value=0, max_value=100)

# write() 可以將文字或變數輸出到網頁上
st.write(f"你輸入的數字是 {number}")  # 顯示使用者輸入的數字

st.write("---")  # 顯示分隔線


score = st.number_input("請輸入分數:", step=1, min_value=0, max_value=100)
if score < 60 and score >= 0:
    st.write("F")
elif score < 70 and score >= 60:
    st.write("D")
elif score < 80 and score >= 70:
    st.write("C")
elif score < 90 and score >= 80:
    st.write("B")
elif score <= 100 and score >= 90:
    st.write("A")

st.write("---")

# 按鈕練習：在 Streamlit 中按鈕會回傳布林值（點擊時為 True），通常用來觸發一次性的動作
# st.write("### 按鈕練習") 會把文字按照 Markdown 標題 3 顯示
st.write("### 按鈕練習")

# 下面示範三個按鈕，使用不同的 key 來區分按鈕的狀態
# 1) 單純建立按鈕（此處沒有綁定後續動作）
st.button("按一下", key="button1")

# 2) 按下按鈕時呼叫 st.balloons() 顯示慶祝動畫
#    注意：st.button() 在每次重新執行時會檢查是否剛剛被點選一次
if st.button("按一下", key="balloons"):
    st.balloons()

# 3) 按下按鈕時呼叫 st.snow() 顯示下雪動畫
if st.button("按一下", key="snow"):
    st.snow()

st.write("---")
