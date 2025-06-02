import os

folder_path = "test_folder"

# フォルダ内のファイル一覧を取得
file_list = os.listdir(folder_path)

print("フォルダ内のファイル一覧:")
for file_name in file_list:
    print(file_name)