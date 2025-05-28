word = " Python入門 "

print(word.strip())           # 前後の空白削除 → "Python入門"
print(word.upper())           # 全部大文字 → " PYTHON入門 "
print(word.lower())           # 全部小文字 → " python入門 "
print(word.replace("入門", "基礎"))  # → " Python基礎 "


