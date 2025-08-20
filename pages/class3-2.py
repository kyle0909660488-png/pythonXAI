import streamlit as st

# 標題：簡單點餐機示範
st.title("點餐機")

# 使用 session_state 來保存購物車（跨互動保留）
if "order" not in st.session_state:
    # 初始化 session_state.order 為空 list（第一次載入時執行）
    st.session_state.order = []

# 將 session_state.order 指派給本地變數以方便操作
ss_order = st.session_state.order  # 運用 session_state 當作購物車 list

# 兩欄佈局：左邊輸入餐點、右邊放加入按鈕
col1, col2 = st.columns(2)
with col1:
    # text_input 讓使用者輸入餐點名稱（回傳字串）
    dishes = st.text_input("請輸入餐點")
with col2:
    # 當按下「加入」按鈕，將輸入的餐點加入購物車
    if st.button("加入", key="add_order"):
        # 若使用者輸入空字串，也會加入；可依需求加入驗證
        ss_order.append(dishes)

st.title("購物車")
# 顯示購物車內容並提供刪除功能
# 注意：直接用 `for i in ss_order` 會在按鈕 key 上造成衝突，
# 因此使用索引方式（range(len(ss_order))) 並為每個按鈕指定唯一 key
for i in range(len(ss_order)):
    col1, col2 = st.columns(2)
    with col1:
        # 在左邊欄位顯示第 i 項餐點
        st.write(ss_order[i])  # 在購物車中顯示餐點名稱
    with col2:
        # 右邊放刪除按鈕：按下後從 list 中移除該項並重新整理畫面
        if st.button("刪除", key=f"{i}"):
            ss_order.pop(i)
            st.rerun()  # 刪除後強制重新執行 script 以更新畫面
