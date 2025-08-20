import os
import streamlit as st

files = os.listdir("markdown")  # 取得資料夾內所有檔案
print(files)

files.sort()  # 將清單排序,預設是由小到大
print(files)

for f in files:  # ['class1.md', 'class2.md']逐一讀取所有 .md檔案
    # markdown/class2.md
    with open(f"markdown/{f}", "r", encoding="utf-8") as file:
        content = file.read()

    with st.expander(f[:-3]):  # 使用expander,標題為檔案名稱去掉.md
        st.write(content)  # 將檔案內容顯示在網頁上
