import os

# ここに初期構造データファイルがあるディレクトリのパスを設定します。
directory_path = "./dpgen/init_comfile/"

# ディレクトリ内のすべての .com ファイルを検索します。
com_files = [
    os.path.join(directory_path, f)
    for f in os.listdir(directory_path)
    if f.endswith(".com")
]

# param.yaml 形式で出力します。
print("sys_configs:")
for file_path in com_files:
    print(f"  - {file_path}")
