import streamlit as st

# Handbook - 今天學到的程式技巧（用國小生可以懂的方式）

st.title("📘 程式小手冊：今天學到的技巧")

st.write("下面用很簡單的句子整理今天學到的重要觀念，方便複習。")

st.markdown(
    """
## 1. 基本資料型態

- **整數 (int)**：像 1、2、-1，沒有小數點。
- **浮點數 (float)**：像 1.0、3.14，有小數點。
- **文字 (str)**：像 "apple" 或 "你好"，要用引號包起來。
- **布林值 (bool)**：只有 True 或 False，表示對或錯。
"""
)

st.markdown(
    """
## 2. 變數（放東西的盒子）

- 變數就像貼標籤的盒子，裡面可以放數字或文字：

```python
a = 10
b = "banana"
```
"""
)

st.markdown(
    """
## 3. 常用的算式（運算子）

- 加法：1 + 1
- 減法：1 - 1
- 乘法：2 * 3
- 除法：4 / 2  (會有小數)
- 取商：5 // 2  (只要整數部分)
- 取餘數：5 % 2
- 次方：2 ** 3
"""
)

st.markdown(
    """
## 4. 字串（文字）的操作

- 字串相加："Hello, " + "World!" → "Hello, World!"
- 字串重複："Hi" * 3 → "HiHiHi"
- 字串內插（f-string）：

```python
name = "Kai"
age = 10
f"My name is {name} and I am {age} years old."
```
"""
)

st.markdown(
    """
## 5. 型態與轉換

- `type(x)` 可以看 x 是哪種型態（int、float、str、bool）。
- 可以用 `int()`, `float()`, `str()`, `bool()` 把資料換成別的型態。
  但有些轉換會失敗，例如 `int("apple")` 會錯。
"""
)

st.markdown(
    """
## 6. 輸入與輸出（在終端機）

- `input("提示文字")`：讓使用者在終端機輸入，回傳字串。
- `print()`：在終端機顯示資料。
"""
)

st.subheader("簡單示範：計算圓面積")
st.text("下面示範用變數和運算算圓的面積（不會要求你輸入）。")

# 範例演算
r = 5  # 半徑
area = r * r * 3.14
st.write(f"當半徑是 {r} 時，圓的面積大約是 {area}")

st.markdown(
    """
---

小提醒：

- 有些指令要小心使用，像把非數字的文字 `"apple"` 直接用 `int()` 會出錯。
- 我們在網頁上用到的 `st.title`, `st.write`, `st.text`, `st.markdown` 是用來把內容顯示在網頁上。

如果你想把這份手冊變得更互動（例如讓同學輸入數字看結果），告訴我要用哪些互動元件，我可以再加上去。
"""
)
