# 📝 我的程式學習筆

## 1. 字典（dictionary）

- 字典就像一個小盒子，裡面有「名字(key)」跟「東西(value)」一組一組放好。
- 用名字就能找到裡面的東西，不需要數第幾個。

### 我學到的用法：

- 建立字典：

  ```python
  d = {"a": 1, "b": 2, "c": 3}
  ```

- 讀取：用名字找東西

  ```python
  print(d["a"])  # 找到 1
  ```

- 取得所有名字：`d.keys()`
- 取得所有東西：`d.values()`
- 同時拿名字和東西：`d.items()`
- 新增東西：`d["d"] = 4`
- 改值：`d["a"] = 5`
- 刪除：`d.pop("a")`
- 檢查有沒有這個名字：`"a" in d`

---

## 2. 函數（function）

- 函數就像一個「小機器」，把資料丟進去，它會幫你做事情，最後可能會給你一個結果。

### 我學到的用法：

- 沒有資料的小機器：

  ```python
  def hello():
      print("Hello World!")
  ```

- 有資料的小機器：

  ```python
  def hello(name):
      print(f"Hello {name}!")
  hello("Kyle")
  ```

- 有結果的小機器（回傳值）：

  ```python
  def add(a, b):
      return a + b
  print(add(1, 2))  # 會印出 3
  ```

---

## 3. Streamlit（讓程式變成網頁）

- Streamlit 就像魔法，能把程式放到網頁上，讓我們用按鈕、輸入框、圖片互動。

### 我學到的東西：

1. **標題**：`st.title("購物平台")`
2. **顯示圖片**：

   ```python
   st.image("image/香蕉圖片.png", width=500)
   ```

3. **輸入數字**：

   ```python
   image_size = st.number_input("圖片大小", min_value=20, step=50, value=100)
   ```

4. **下拉選單**：

   ```python
   st.selectbox("選擇圖片", image_files, index=0)
   ```

5. **按鈕**：

   ```python
   if st.button("購買 apple"):
       # 減少庫存
   ```

6. **session_state**：

   - 這是「小書包」，可以記住資料，就算網頁刷新，東西也不會消失。

---

## 4. 小結

- **字典**：用名字存東西。
- **函數**：像小機器，可以丟資料進去拿結果。
- **Streamlit**：讓程式變得好玩，可以放圖片、選單、按鈕，還能做購物平台。
