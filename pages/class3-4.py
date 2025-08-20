import random  # 匯入 random 模組以產生亂數

# 猜數字遊戲：電腦隨機產生一個 1 到 100 的整數，使用者不斷猜測直到猜中為止
ans = random.randint(1, 100)  # 隨機產生 1 ~ 100 的整數作為答案
max_num = 100  # 當前可猜的最大值（初始為100）
min_num = 1  # 當前可猜的最小值（初始為1）
while True:  # 不斷重複提示使用者直到猜中
    # input() 會回傳字串，使用 int() 轉型成整數後存入 num
    num = int(
        input(f"請輸入 {min_num} 到 {max_num} 的整數：")
    )  # 讀取使用者輸入並轉成 int

    if num > ans:  # 如果使用者輸入的數字大於答案
        print("太大了！")  # 提示數字太大
        # 如果使用者輸入的數字小於目前的上限，表示可以縮小上限範圍
        if num < max_num:
            max_num = num  # 更新上限為使用者輸入的數字，下一次提示會更精準
    elif num < ans:  # 如果使用者輸入的數字小於答案
        print("太小了！")  # 提示數字太小
        # 如果使用者輸入的數字大於目前的下限，表示可以提高下限範圍
        if num > min_num:
            min_num = num  # 更新下限為使用者輸入的數字，下一次提示會更精準
    else:  # 使用者猜中答案
        print("恭喜你！")  # 顯示猜中訊息
        break  # 跳出迴圈，程式結束
