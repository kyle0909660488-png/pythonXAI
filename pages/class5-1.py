# 預設參數
# 可以在函數的參數中設定預設值,當呼叫這個參數時,如果沒有導入參數,則會使用預設值
# 多個參數時,有預設值的參數要放在沒有預設值參數後面
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


hello("Kyle")
hello("Jasmine", "Good morning")


# 限制傳入參數型態
# 可以在函數的參數中設定型態,當呼叫這個參數時,可以提示使用者要傳入的參數型態
# 變數: 型態=預設值
# -> 型態,代表回傳值的型態
def add(a: int, b: int = 0) -> int:
    return a + b


print(add(1, 2))
print(add("Hello, ", "World!"))

# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數, area 是區域變數
    # length = length + 1 # 這行會出錯
    # 因為在函數內部length是區域變數,不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯,因為area是區域變數,只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數, area 是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
# 因為要等到函數被呼叫時才會執行,所以area的值是在函數被呼叫時才會被計算


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數, area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100
# 這時候指令內部的area是區域變數,不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length 是全域變數, area 是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是 25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用global, 將area變成全域變數,可以在函數內部修改全域變數的值
    area = length**2  # length 是全域變數, area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 25


def hello(name: str):  # 函數除入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name: str - 姓名

    回傳:None

    範例:Hello("Kyle") # Hello, Kyle!
    """
    print(f"Hello, {name}!")
