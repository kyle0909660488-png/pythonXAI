import streamlit as st
import os

# 使用 st.session_state 儲存跨互動的狀態
# st.session_state 可用來儲存變數，讓按鈕點擊或重整後資料仍保留
ss = st.session_state

# 讀取圖片資料夾，將檔名當作商品來源
image_folder = "image"
image_files = os.listdir(image_folder)  # 讀取 image 資料夾內的所有檔案

# 初始化商品資料（只在 session_state 中不存在時建立）
# ss.products 的結構範例：
# ss.products = {
#   "apple": {"price": 10, "stock": 10, "image": "image/apple.png"},
#   "banana": {"price": 10, "stock": 10, "image": "image/banana.png"}
# }
if "products" not in ss:
    ss.products = {}  # 建立 products 字典以儲存所有商品的詳細資料

# 將資料夾中的每個檔案加入到 ss.products（若商品不存在才新增）
for image_file in image_files:
    # product_name 以檔名去掉副檔名作為商品名稱
    product_name = image_file[:-4]
    if product_name not in ss.products:  # 如果商品不存在，則新增商品預設值
        ss.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }

# 範例：如何存取資料
# - ss.products["apple"]["price"]  取得 apple 的價格
# - ss.products["banana"]["stock"] 取得 banana 的庫存
# - ss.products["orange"]["image"] 取得 orange 的圖片路徑

st.title("購物平台")  # 頁面標題

# 使用多欄位顯示商品，這裡預設分成 3 欄
cols = st.columns(3)
i = 0
for product_name, details in ss.products.items():
    # product_name 裡面是商品名稱，details 是該商品的詳細字典
    # details 範例： {"price": 10, "stock": 10, "image": "image/apple.png"}
    with cols[i % len(cols)]:  # 透過取餘數決定商品顯示在哪一欄
        # 顯示商品圖片，使用 use_container_width 讓圖片適應欄位寬度
        st.image(details["image"], use_container_width=True)
        st.write(f"### {product_name}")
        st.write(f"價格: ${details['price']}")
        st.write(f"庫存: {details['stock']}")

        # 每個商品放一個購買按鈕，key 設成商品名稱保證唯一
        # 當按下按鈕時，如果庫存>0，便從 session_state 的該商品庫存扣除
        if st.button(f"購買 {product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                ss.products[product_name]["stock"] -= 1  # 扣除庫存
            # 按下後重新整理頁面以更新顯示（例如庫存數量）
            st.rerun()
        i += 1


st.title("新增庫存")  # 新增庫存區塊標題
col_1, col_2, col_3 = st.columns(3)
with col_1:
    # selectbox 用來選擇要補貨的商品（使用 ss.products 的 keys 作為選項）
    selected_product = st.selectbox("選擇商品", ss.products.keys())
with col_2:
    # number_input 用戶輸入要新增的數量
    new_stock = st.number_input("新增庫存", min_value=0, step=1, value=1)
with col_3:
    # 補貨按鈕，按下後將所選商品的庫存加上輸入數量
    if st.button("補貨"):
        ss.products[selected_product]["stock"] += new_stock
    # 補貨後重新整理頁面以顯示更新後的庫存
    st.rerun()
