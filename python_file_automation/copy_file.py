import shutil
import os

source = os.path.join("test_folder", "sample1.txt") # コピー元
destination = os.path.join("copied_folder", "sample1.txt") # コピー先

# ファイルをコピー
shutil.copy2(source, destination)

print("ファイルをコピーしました！")