import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルを読み込み
df = pd.read_csv("sneakers.csv")

# データの中身を表示
print(df)

# ブランドごとの売上合計を計算
brand_sum = df.groupby("brand")["sales"].sum()

# 結果を表示
print("ブランド別売上合計：")
print(brand_sum)

#棒グラフを描画
brand_sum.plot(kind="bar", title="ブランド別合計売上")

#ラベルを追加
plt.xlabel("ブランド")
plt.ylabel("売上(合計)")

#グラフを表示
plt.tight_layout()
plt.show()

