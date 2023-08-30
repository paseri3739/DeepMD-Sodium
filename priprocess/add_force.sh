#!/bin/bash

# 引数の数を確認
if [ "$#" -ne 1 ]; then
  echo "使用法: $0 <ファイル名>"
  exit 1
fi

# ファイルの存在を確認
if [ ! -f "$1" ]; then
  echo "エラー: ファイル '$1' が見つかりません。"
  exit 1
fi

# 改行コードの置換
dos2unix "$1"

# 出力ディレクトリの作成
output_dir="added_output"
mkdir -p "$output_dir"

# 出力ファイルパスの生成
output_file="$output_dir/$(basename "$1")"

# 検索と置換して出力ファイルに書き込む
sed '/b3lyp\/6-311+g(d)/ s/$/ force/' "$1" > "$output_file"

# 最後の行に"--Link1--"があれば削除する
sed -i '$ {/--Link1--/d;}' "$output_file"

echo "処理が完了しました。出力ファイル: $output_file"

