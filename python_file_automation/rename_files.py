import os
target_folder = "copied_folder"
file_list = os.listdir(target_folder)

count = 1
for file_name in file_list:
    if file_name.endswith(".txt"):
        old_path = os.path.join(target_folder, file_name)
        new_file_name = f"renamed_{count}.txt"
        new_path = os.path.join(target_folder, new_file_name)
        os.rename(old_path, new_path)
        print(f"{file_name} -> {new_file_name}")
        count += 1

