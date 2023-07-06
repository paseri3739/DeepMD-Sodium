#!/bin/bash

# コマンドライン引数から入力ファイルを取得
input_file="$1"
output_dir="output"
counter=1

# 引数の数をチェック
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

# 入力ファイルが存在するかチェック
if [[ ! -f "$input_file" ]]; then
  echo "Input file '$input_file' does not exist."
  exit 1
fi

# 出力ディレクトリが存在しない場合は作成
mkdir -p "$output_dir"

# 検索対象の文字列
search_string="Normal termination of Gaussian 16"

# テキストファイルを行ごとに読み込み、検索文字列を含む行の次の行から新しいファイルを分割して処理
awk -v s="$search_string" -v d="$output_dir" -v c="$counter" \
'BEGIN {output=d"/output_"c".txt"} /'"$search_string"'/ {print > output; c++; output=d"/output_"c".txt";next} {print > output}' "$input_file"

