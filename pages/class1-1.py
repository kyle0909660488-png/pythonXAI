# 這是註解,不會被程式執行
# Ctrl+?可以把單行程式註解起來
# 如果框選多行程式碼,按Ctrl+?可以把多行程式碼註解起來

# 基本型態
print(1)  # int這是整數,-1,0,1,2
print(1.0)  # float這是浮點數
print(1.234)  # float這是浮點數
print("apple")  # str這是字串 "sadasd123125557",
print("1")  # str這是字串 "1",'1'
print(True)  # bool這是布林值,True或False
print(False)  # bool這是布林值,T或F

# 變數
a = 10  # 新增一個儲存空間並取名為a, "="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為"apple"
print(a)  # 在終端機顯示a所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1.()括號
# 2.**次方
# 3.*/ // % 乘 除 取商 取餘
# 4.+ - 加 減

# 請用前面的用詞標準來完成以下的程式碼的註解

# 字串運算, + , *
print("Hello, " + "World!")  # 字串相加
print("Hello, " * 3)  # 字串重複

# 字串格式化
name = "Kai"  # 字串變數
age = 25  # 整數變數
print(f"My name is {name} and I am {age} years old.")  # 使用f-string格式化字串
# 可以將變數或其他型態的資料放到f字串裡面的{},這樣就可以在字串中顯示
# len() 函式可以計算任何型態的資料長度
print(len("apple"))  # 計算字串的長度

# type() 可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(0))  # float轉int
print(str(1.234))  # float轉str
print(float("1.234"))  # str轉float
print(bool(1.234))  # float轉bool
# print(int("apple"))  # 這行會錯誤,因為"apple"不能轉成整數

print("輸入開始")
# input() 函式可以讓使用者輸入資料
# ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入你的名字: ")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入的資料是字串


r = int(input("請輸入圓的半徑: "))  # 讓使用者輸入圓的半徑,並轉換成整數
a = r * r * 3.14  # 計算圓的面積
print(f"圓的面積是: {a}")  # 顯示計算結果
