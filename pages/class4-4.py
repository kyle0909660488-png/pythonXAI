# def
# 新增一個函數要用 def 開頭, 後面接著函數名稱,再加上小括號,最後加上冒號
def hello():
    print("Hello World!")


# 函數 (function)
# 在 Python 定義函數使用關鍵字 def，格式為：def 函數名稱(參數):
# 函數內的程式區塊以縮排表示，並可使用 return 回傳值。

# 範例：不帶參數的函數


for i in range(10):
    print()


# 帶參數的函數
# 下面的 hello 函數接受一個參數 name，呼叫時可以傳入任何值（字串、數字等）
# 有傳入參數的函數
# 這個函數有一個參數 name, 當呼叫這個函數, 可以傳入一筆資料給name
def hello(name):
    print(f"Hello {name}!")


hello("Kyle")
hello("Joasmine")

# 有回傳值的函數
# 使用 return 回傳一個值，呼叫者可以將回傳值存入變數
hello("henry")
for i in range(10):
    hello(i)  # 這裡的i 會被當作 name 的值


# 有回傳值的函數
# 這格函數會回傳一個值, 當呼叫這個函數時, 可以把回傳的值存起來
# 在指令當中只要執行return就可以回傳值, 並結束函數


# 函數可以回傳多個值
# 在 Python 中回傳多個值會實際上回傳一個 tuple，可以用多個變數接收
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("Hello", "World"))

# 多個 return 路徑
# 函數內可以有條件判斷，根據情況回傳不同的值
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個會回傳兩個值, 當呼叫這個函數時, 可以把回傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum = {sum}, sub = {sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))
