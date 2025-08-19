import streamlit as st  # 匯入 streamlit 套件並命名為 st，用於建立簡易網頁介面

# number_input 會在網頁上顯示一個數字輸入欄位
# "Enter a number: " 是提示文字，min_value 最小值，max_value 最大值，step 步進
number = st.number_input("Enter a number: ", min_value=1, max_value=9, step=1)

# 迴圈從 1 到使用者輸入的 number（包含 number）
for i in range(1, number + 1):
    # 將數字 i 轉為字串後重複 i 次，並用 st.write 顯示在頁面上
    # 例如 i=3 時會顯示 '333'
    st.write(str(i) * i)
