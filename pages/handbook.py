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
"""手冊：僅使用教材中已出現的語法與 API，程式碼示例使用 Markdown 三引號並標示 python 高亮。

本檔會用到的 streamlit API（由教材掃描得出）：
- st.title
- st.write
- st.text
- st.markdown
- st.number_input
- st.button
- st.balloons
- st.snow

以下內容依教材出現順序撰寫，示例程式碼皆以三引號 python 區塊呈現。
"""

import streamlit as st

st.title("📘 程式學習筆記（依教材已學內容）")

st.write("下列內容只用到教材中已出現過的語法與 Streamlit API，方便複習與擴充。")

st.markdown(
    """
## 1. 基本型態

- **整數 (int)**：例如 1, -1, 0
- **浮點數 (float)**：例如 1.0, 3.14
- **字串 (str)**：用引號包起來，例如 "apple"
- **布林 (bool)**：True / False

程式碼範例：

```python
print(1)
print(1.234)
print("apple")
print(True)
```
"""
)

st.markdown(
    """
## 2. 變數與賦值

```python
a = 10
b = "banana"
print(a)
print(b)
```
"""
)

st.markdown(
    """
## 3. 運算子與優先順序

- 加減乘除：`+ - * /`
- 整數除法：`//`
- 餘數：`%`
- 次方：`**`

示例：

```python
print(1 + 1)
print(2**3)
print(5 // 2)
print(5 % 2)
```
"""
)

st.markdown(
    """
## 4. 字串操作與格式化

- 串接與重複：`"Hello" + "World"`, `"Hi" * 3`
- f-string（教材已有）：在字串中使用 `{}` 插入變數。

```python
name = "Kai"
age = 10
print(f"My name is {name} and I am {age} years old.")
```
"""
)

st.markdown(
    """
## 5. 型態檢查與轉換

- `type(x)` 可查看變數型態。
- `int()`, `float()`, `str()`, `bool()` 可做基本轉換（失敗會拋錯，例如 `int("apple")`）。

```python
print(type(1))
print(int(1.0))
print(str(1.234))
```
"""
)

st.markdown(
    """
## 6. 長度與輸入（終端）

- `len()` 在教材中有出現，用於計算長度。
- `input()` 與 `print()` 為終端互動示例（教材示範於非 Streamlit 範例）。

```python
text = input("請輸入文字: ")
print("你輸入：", text)
print(len(text))
```
"""
)

st.markdown(
    """
## 7. Streamlit 基本用法（教材中出現的 API）

- `st.title`, `st.write`, `st.text`, `st.markdown`
- `st.number_input`（數字輸入）
- `st.button`, `st.balloons`, `st.snow`

範例：

```python
import streamlit as st

number = st.number_input("請輸入數字:", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是 {number}")

if st.button("按一下", key="balloons"):
    st.balloons()

if st.button("按一下", key="snow"):
    st.snow()
```
"""
)

st.markdown(
    """
## 8. 總結 / 下一步建議

- 本手冊僅包含教材中已教過的語法與 API。若教材增加新內容，下一次掃描會自動納入。
- 若要把本手冊變得更互動（例如：表單或圖表），需等教材加入對應的 `st.` API（尚未學）。
"""
)

st.write("---")

st.text(
    "執行指引：在本機執行前請安裝 streamlit，然後用 streamlit run pages/handbook.py 啟動。"
)
