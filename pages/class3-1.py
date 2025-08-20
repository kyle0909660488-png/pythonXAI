import streamlit as st

# 標題：說明這個頁面展示欄位（columns）相關元件
st.title("欄位元件")

# 基本的兩欄佈局 (兩個 column 等寬)
col1, col2 = st.columns(2)
# 在 col1 中放一個按鈕，按下後會回傳 True（但此處未捕捉回傳值）
col1.button("按鈕1", key="btn1")
# 在 col2 中放另一個按鈕（注意 key 要唯一避免衝突）
col2.button("按鈕2", key="btn2")

# 可以用比例設定每個 column 的寬度，比例放在 list 中（例如 [1,2]）
col1, col2 = st.columns([1, 2])
col1.button("按鈕3", key="btn3")  # 較窄的欄位放按鈕
col2.button("按鈕4", key="btn4")  # 較寬的欄位也可以放元件

# 三欄範例，欄位寬度依序為 1,2,3
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="btn5")
col2.button("按鈕6", key="btn6")
col3.button("按鈕7", key="btn7")

st.write("---")  # 顯示分隔線

# 使用 with 區塊在特定 column 中放多個元件
col1, col2 = st.columns([1, 2])
with col1:
    # 在 col1 中顯示文字，並放一個按鈕；如果按下會觸發氣球動畫
    st.write("這是col1")
    if st.button("按鈕8", key="btn8"):
        st.balloons()  # 顯示氣球動畫（視覺效果）
with col2:
    # 在 col2 中顯示多行文字與按鈕
    st.write("這是col2")
    st.button("按鈕9", key="btn9")

# 動態建立多個 columns：使用者輸入要幾個欄位 (n)，然後建立 n 個 column
n = st.number_input("輸入欄位數", min_value=1, value=4, step=1)
cols = st.columns(n)  # 回傳一個 columns 的 list，索引從 0 開始
for i in range(len(cols)):
    # 對於每個欄位使用 with，然後放一個按鈕（注意 key 要唯一）
    with cols[i]:
        st.button(f"for當中的按鈕{i+1}", key=f"多col{i+10}")
        # 這邊按鈕的 key 會是: 多col10, 多col11, ...（確保不同按鈕的 key 不重複）

st.write("---")
st.title("columns排列元件效果比較")

# 範例：一個 row，兩個 columns，各放入不同數量的元件來比較排列
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="btn10")
    st.button("按鈕2", key="btn11")
    st.button("按鈕3", key="btn12")
with col2:
    # col2 放多個文字，觀察文字與按鈕的排列差異
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")

st.write("---")

# 範例：建立三個 row，每個 row 有兩個 columns
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")

st.write("---")
st.title("session_state")

# 一個簡單的變數示範（不是 session state）
ans = 1  # 設定變數 ans 初始為 1
if st.button("按下去ans+1", key="btn_ans"):
    # 當按鈕按下時，局部變數 ans 加 1（此做法在 Streamlit 中通常不會持久化）
    ans = ans + 1
st.write(f"ans={ans}")  # 顯示目前 ans 的值

# 使用 session_state 來保存狀態（跨互動保留變數）
if "ans" not in st.session_state:
    # 如果 session_state 沒有 ans，就初始化為 1（只會在第一次執行時設置）
    st.session_state.ans = 1

if st.button("按下去ans+1", key="btn_ans2"):
    # 使用 session_state 更新會在互動之間保留數值
    st.session_state.ans = st.session_state.ans + 1
st.write(f"ans={st.session_state.ans}")  # 顯示 session_state 中的 ans 值

# 有時候按鈕按下後未必會完整重新整理畫面，
# 可以使用 st.rerun() 強制重新執行整個 script 以刷新畫面
if st.button("重新整理畫面", key="banana"):
    st.rerun()

st.write("---")
st.title("文字輸入元件")
# st.text_input指令格式：st.text_input(輸入欄位的標題,value="預設顯示文字")
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是 {text}")
