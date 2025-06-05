import shutil
import os

source_folder = "test_folder"
destination_folder = "copied_folder"

# フォルダ内のファイル一覧を取得
file_list = os.listdir(source_folder)

# 拡張子が.txtのファイルだけコピー
for file_name in file_list:
    if file_name.endswith(".txt"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy2(source_path, destination_path)
        print(f"{file_name}をコピーしました！")
