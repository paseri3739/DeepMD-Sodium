#!/bin/bash

# Gaussianの実行コマンドを設定
GAUSSIAN_COMMAND="g16" # またはあなたの環境に合わせてg09など

# 最初のファイル番号と最後のファイル番号を設定
FIRST=1
LAST=853 # 例として100を設定。実際の最後のファイル番号に置き換えてください。

# FIRSTからLASTまでのファイルを処理する
for (( i=FIRST; i<=LAST; i++ ))
do
    # ファイル名を生成
    FILENAME="coordinates_${i}.com"

    # ファイルが存在するか確認
    if [[ -f "$FILENAME" ]]; then
        # Gaussian計算を実行
        $GAUSSIAN_COMMAND < "$FILENAME" > "./log/coordinates_${i}.log"

        # Gaussianの終了ステータスを確認
        if [ $? -ne 0 ]; then
            echo "Warning: Gaussian calculation for $FILENAME ended with an error." >&2
        fi
    else
        echo "Warning: File $FILENAME does not exist." >&2
    fi
done
