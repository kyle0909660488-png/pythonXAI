# 字典 (dictionary)
# dict 是用 key:value 的方式儲存資料。
# - key (鍵) 必須是不可變的資料型態，例如 int、float、str 等。
# - value (值) 可以是任意資料型態。
# dict 內的項目是無序的，無法用 index 來存取，需透過 key 來取得對應的 value。

# 建立一個 dict，包含三個 key-value
d = {"a": 1, "b": 2, "c": 3}

# CRUD - Read (讀取資料)
# 可以透過指定的 key 取得對應的 value
print(d["a"])  # 1
print(d["b"])  # 2
print(d["c"])  # 3

# 取得 dict 的所有 keys
# 回傳值是 dict_keys，可用於迭代
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)  # 逐一印出所有 key

# 取得 dict 的所有 values
# 回傳值是 dict_values，也可以迭代
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)  # 逐一印出所有 value

# 取得 dict 的所有 key-value pair
# items() 會回傳一個包含 (key, value) tuple 的可迭代物件
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)  # 同時取得 key 與對應的 value

# CRUD - Create / Update (新增或修改資料)
# 直接指定一個不存在的 key 就會新增該 key:value
d["d"] = 4  # 新增一個 key 為 'd' 的項目
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 如果指定的 key 已存在，會改變其對應的 value（更新資料）
d["a"] = 5  # 修改 key 'a' 的值為 5
print(d)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# CRUD - Delete (刪除資料)
# pop() 可以移除指定的 key 並回傳被移除的 value
print(d.pop("a"))  # 5，會移除 key 'a' 並印出原本的值

# 如果要移除不存在的 key，可以提供第二個參數作為預設值，避免拋出錯誤
print(d.pop("e", "Not found"))  # Not found
# 如果未提供預設值且 key 不存在，pop() 會丟出 KeyError

# 取得 dict 的長度（項目數）
print(len(d))  # 3

# 檢查某個 key 是否存在於 dict
# 使用 in 只會檢查 keys（不會檢查 values）
print("a" in d)  # False（因為剛剛已經用 pop 移除 'a'）
print("e" in d)  # False
