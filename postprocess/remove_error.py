import os
import sys
import shutil


def remove_error_from_gaussian_output(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    # 最後の行が"Normal termination of Gaussian 16"を含んでいる場合、エラー除去をスキップ
    if "Normal termination of Gaussian 16" in lines[-1]:
        return lines

    # "Initial command:"で始まる行を探し、ヒットする最後の行のインデックスを取得
    index_to_remove = None
    for i, line in enumerate(lines):
        if line.startswith("Initial command:"):
            index_to_remove = i

    # その行以降を削除
    if index_to_remove is not None:
        lines = lines[:index_to_remove]

    with open(input_file, "w") as f:
        f.writelines(lines)

    return lines


def combine_files(directory, all_lines):
    with open(os.path.join(directory, "combined_output.log"), "w") as f:
        for lines in all_lines:
            f.writelines(lines)
            f.write("\n\n")  # 2つのファイルの間に空行を追加


def main():
    # コマンドライン引数からディレクトリを取得
    original_directory = sys.argv[1]
    copied_directory = original_directory + "_copy"

    # ディレクトリのコピーを作成
    shutil.copytree(original_directory, copied_directory)

    all_lines = []

    # コピーされたディレクトリ内のすべての.logファイルを処理
    for filename in os.listdir(copied_directory):
        if filename.endswith(".log"):
            file_path = os.path.join(copied_directory, filename)
            lines = remove_error_from_gaussian_output(file_path)
            all_lines.append(lines)

    # エラーを取り除いたすべてのファイルを結合
    combine_files(copied_directory, all_lines)


if __name__ == "__main__":
    main()
