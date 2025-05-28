try:
    num = int(input("整数を入力してください: "))
except ValueError:
    print("整数を入力してください！")
else:
    print(f"{num}の2倍は{num * 2}です")
