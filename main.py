import streamlit as st

# 設定頁面配置(必須在其他 Streamlit 命令之前)
st.set_page_config(page_title="Python XAI", page_icon="🐍")

# 選單內容 - 要加新課程就改這裡
# 在每個標題都要根據內容性質加上, emojis, 這樣看起來更有趣
all_pages = {
    "🏠 導覽": [
        st.Page("pages/home.py", title="首頁", icon="🏠"),
        st.Page("pages/handbook.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown", icon="📝"),
        st.Page("pages/class2-2.py", title="成績評分", icon="🖊️"),
        st.Page("pages/class2-4.py", title="數字金字塔", icon="🔺"),
        st.Page("pages/class3-1.py", title="columns 與 session_state", icon="📂"),
        st.Page("pages/class3-2.py", title="點餐機", icon="🤖"),
        st.Page("pages/class3-5.py", title="猜數字遊戲", icon="🎮"),
        st.Page("pages/class4-2.py", title="圖片練習", icon="🖼️"),
        st.Page("pages/class4-3.py", title="購物平台", icon="🏬"),
    ],
}

# 統一使用 st.navigation 管理選單
nav = st.navigation(all_pages, position="sidebar")
nav.run()
