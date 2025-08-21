import streamlit as st
import os

# 標題：展示圖片元件的用法
st.title("圖片元件")

# st.image: 用來在 Streamlit 顯示圖片
# 第一個參數為圖片路徑（或 URL），第二個常用參數為 width，可指定圖片寬度
st.image("image/香蕉圖片.png", width=500)  # 顯示單張圖片，寬度設定為 500

# 取得圖片資料夾與檔案清單
image_folder = "image"  # 存放圖片的資料夾（相對路徑）
image_files = os.listdir(image_folder)  # 取得該資料夾下所有檔案名稱
st.write(image_files)  # 在頁面上列出檔案清單，方便檢視有哪些圖片

# number_input: 讓使用者輸入數值，這裡用來控制圖片顯示大小
# - min_value: 最小值
# - step: 每次增加/減少的步長
# - value: 預設值
image_size = st.number_input("圖片大小", min_value=20, step=50, value=100)
# 註：範例設定 step=50，代表每次按上下箭號會變化 50

# 根據使用者輸入的大小顯示所有圖片
for image_file in image_files:
    # 使用 width 參數控制寬度
    st.image(f"{image_folder}/{image_file}", width=image_size)

# 也可以使用 use_container_width 讓圖片自動填滿容器（寬度由 layout 決定）
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_container_width=True)

# selectbox: 下拉選單讓使用者選擇特定圖片，並顯示選擇結果
selected_image = st.selectbox("選擇圖片", image_files, index=0)  # 預設選第一張
st.image(
    f"{image_folder}/{selected_image}", width=300
)  # 顯示使用者選擇的圖片，寬度 300
