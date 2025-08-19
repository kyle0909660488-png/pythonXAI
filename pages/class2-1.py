print(1 == 1)  # == 等於: 檢查左右是否相等，結果為布林值 True 或 False
print(1 != 1)  # != 不等於: 檢查左右是否不相等
print(1 < 2)  # < 小於: 比較數值大小，回傳 True/False
print(1 > 2)  # > 大於: 比較數值大小，回傳 True/False
print(1 <= 1)  # <= 小於或等於: 比較時包含等於情況
print(1 >= 1)  # >= 大於或等於: 比較時包含等於情況

# 布林運算 - and: 只有左右都為 True 時，結果才是 True
print(True and True)  # True and True => True
print(True and False)  # True and False => False
print(False and True)  # False and True => False
print(False and False)  # False and False => False

# 布林運算 - or: 只要左右任一為 True，結果就為 True
print(True or True)  # True or True => True
print(True or False)  # True or False => True
print(False or True)  # False or True => True
print(False or False)  # False or False => False

# 布林運算 - not: 反轉布林值
print(not True)  # not True => False
print(not False)  # not False => True

# 運算子優先順序 (由高到低)
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘、除、取商、取餘
# 4. + - 加、減
# 5. 比較運算子: == != < > <= >=
# 6. not
# 7. and
# 8. or

# 範例: 使用 input() 讀取使用者輸入的密碼，並依條件輸出不同訊息
password = input("請輸入密碼: ")  # input 輸入的結果為字串
if password == "1124":
    print("歡迎Kyle")  # 當密碼為 "1124" 時顯示歡迎 Kyle
elif password == "0627":
    print("歡迎Jasmine")  # 當密碼為 "0627" 時顯示歡迎 Jasmine
elif password == "2427":
    print("你答對了")  # 當密碼為 "2427" 時顯示你答對了
else:
    print("再試一次")
# 連續使用if跟使用if elif else的差異
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省時間
# 但是如果是使用多個if來做獨立判斷，則每個if都會被執行，所以效率較低
