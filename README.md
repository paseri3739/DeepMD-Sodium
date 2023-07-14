# random_coords_for_gaussian
random_coords.pyは乱数により複数の座標の組を持った入力ファイルを作成する。
python(3) random_coords.py <number of loops>

python(3) split_gaussian.py <logファイルのpath> でlogファイルをsplitedディレクトリに分割して格納する。

python(3) import_multiple.py <splitedディレクトリのpath> で複数のlogファイルをdpdataによりインポートして学習用のrawファイルを生成する　
