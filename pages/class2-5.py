print([])  # 這是一個空的 list，沒有元素
print([1, 2, 3])  # 這是一個有三個元素的 list，元素為整數 1,2,3
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的 list，包含整數與字串
print(
    [1, 2, 3, ["a", "b", "c"]]
)  # 這是一個有四個元素的 list，其中最後一個元素本身是另一個 list（巢狀 list）
print(
    [1, True, "a", 1.23]
)  # 這是一個有四個元素的 list，展示不同型態可以混合在同一個 list 中

# CRUD 是常見的資料操作模式，代表四種基本操作
# C: Create (建立)
# R: Read (讀取)
# U: Update (更新)
# D: Delete (刪除)

# CRUD - Read（讀取）操作示範
# 在 Python 中 list 的 index 從 0 開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 取出 index 0 的元素，輸出 1
print(L[1])  # 取出 index 1 的元素，輸出 2
print(L[2])  # 取出 index 2 的元素，輸出 3
print(L[3])  # 取出 index 3 的元素，輸出 "a"

L = [1, 2, 3, "a", "b", "c"]
# slice（切片）語法: [start:stop:step]
# L[::2] 從頭到尾，每隔兩個元素取一個 -> [1, 3, 'b']
print(L[::2])
# L[1:4] 從 index 1 取到 index 3 (不包含 4) -> [2, 3, 'a']
print(L[1:4])
# L[1:4:2] 從 index 1 取到 index 3，每兩個元素取一次 -> [2, 'a']
print(L[1:4:2])
# 切片的行為跟 range 類似，使用不同的符號表達

# 走訪 list 中的元素（iteration）
# 方法一：使用 index（透過 range 與 len）
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])  # 透過 index 取得元素，這裡每隔一個 index 取一次
# 方法二：直接把 list 當作可迭代物件（更直觀）
for i in L:
    print(i)  # 直接取得元素本身

# CRUD - Update（更新）操作示範
# 可以透過 index 去指定並修改 list 中的元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 把 index 0 的元素改成 2
print(L)  # 輸出修改後的 list

# 注意：以下原本範例中有錯誤（對不可變整數進行索引操作）
# 在 Python 中，整數是不可變（immutable），不能用索引修改，所以原本的 a = 1; b = a; b[0]=2 會發生錯誤
# 正確示範 mutable（可變）物件與 copy 行為如下：
a = [1, 2, 3]
b = a  # 指派會讓 a 與 b 指向同一個 list（同一個記憶體位置）
b[0] = 2
print(a, b)  # 由於指向同一個 list，a 與 b 都會反映改變

# 如果想要複製 list（淺複製）使其指向不同記憶體位置，可以使用 copy()
a = [1, 2, 3]
b = a.copy()  # b 現在是 a 的淺複製，兩者為不同的物件
b[0] = 2
print(a, b)  # 修改 b 不會影響 a

# CRUD - Delete（刪除）操作示範
# 方法一：使用 remove(value) 移除指定值，會移除第一個符合的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個出現的 "a"
# 注意：remove 會從頭開始搜尋並移除第一個符合的元素
# 若要移除所有特定值，建議用 list comprehension 或建立新的 list
L = [x for x in L if x != "a"]  # 範例：移除所有的 "a"

# 方法二：使用 pop(index) 移除指定 index 的元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除 index 0 的元素
# 如果不指定 index，pop() 會移除並回傳最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # 顯示剩下的元素

# 檔案開啟模式說明：
# r  - 讀取模式，檔案必須存在
# w  - 寫入模式，檔案不存在會自動建立（會覆蓋原本檔案）
# a  - 附加模式，檔案不存在會自動建立（在檔案尾端新增）
# r+ - 讀取與寫入模式，檔案必須存在
# w+ - 讀取與寫入模式，檔案不存在會自動建立
# a+ - 讀取與附加模式，檔案不存在會自動建立

# 範例（傳統方式）：先手動 open，讀取後必須 close
f = open(
    "pages\\class1-1.py", "r", encoding="utf-8"
)  # 開啟檔案（注意 Windows 路徑的反斜線）
content = f.read()  # 讀取整個檔案內容
print(content)  # 印出檔案內容
f.close()  # 關閉檔案，釋放系統資源

# 範例（推薦方式）：使用 with 會自動關閉檔案
with open("pages\\class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 印出內容
# 不需要顯式呼叫 f.close()，with 會自動幫你關檔

# 字串的小工具：檢查字串是否以指定結尾
filename = "class1.md"
print(filename.endswith(".md"))  # 檢查 filename 是否以 .md 結尾 -> True
filename2 = "note.txt"
print(filename2.endswith(".md"))  # 檢查 filename2 是否以 .md 結尾 -> False
