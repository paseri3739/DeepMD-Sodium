# random_coords_for_gaussian
本プロジェクトは科学技術の発展振興のため、GPL3.0により公開する。改変したプログラムを公開する場合GPLを適用しソースコード全体を公開せよ。

このプログラムは、複数のガウス分布の座標を生成して機械学習を行うための一連のフローを提供する。

# 設計の説明:
Atom, AtomClusterInterface, GeneralAtomCluster, FourAtomCluster, GaussianWriterの4つのクラスを定義している。

Atom型は、原子の名前、座標の情報を持つデータ型である。座標はnumpyの配列として格納する。そのように定義することで数学的なベクトル演算が簡単かつ高速に行えるようになる。
AtomClusterInterfaceはAtomのリストをもつ。GeneralAtomCluster, FourAtomClusterの継承元となるインターフェースであり、一般の原子系に適用可能なプロットメソッドと原子の座標取得メソッドを実装している。

GeneralAtomClusterはAtomClusterInterfaceを継承し、将来的にN原子系に対応する。
FourAtomCluster型は、4つのAtom型リストに特化した型として定義した。これにより一般のN原子系のルーチンと分け、呼び出し元はAtomClusterInterfaceを参照するようにすることで将来的な保守性を高めるように設計した。

これらのクラスをgenerate_gaussian_fileパッケージからimportしてmainプログラムを作成することで必要に応じて座標の配置、可視化、そして配置した座標をもとに原子間距離とグラフの交差を基準にして実現可能性のある原子配置をGaussian用の計算ファイルに必要な数だけ書き込むことができる。
`/generate_gaussian_file/generate_gaussian_file.py <number to loop>`
で3次元の配置を行う。

# インストールと実行
インストールはDockerイメージにより簡単に行うことができる。requirements.txtを参照して直接パッケージをインストールして実行することも可能。`docker run`
コマンドで仮想のコンソールに入り、そこからpythonを起動することができる。イメージ作成手順は以下。

cdしたのち、
`docker build -t <your_image_name> .` (最後のドットに注意！)
でイメージを作成して
`docker images`
で作成した名前のイメージがあることを確認し、
`docker run -it --rm <your_image_name>`
とするとdockerに構築された環境のシェルに入ることができる。これで仮想環境でシェルコマンドやPythonを実行することができる。Dockerコンテナのマウントについては割愛。

dockerを利用しない場合にはvenvで環境を構築することができる。
プロジェクトのルートにcdして、install用のシェルスクリプト、batファイルを実行する。仮想環境がプロジェクトのルートディレクトリに作成されたことを確認した後
`source venv/bin/activate` (Unixの場合,Winはバックスラッシュ)
のようにして仮想環境に入ることができる。(仮想環境の名前はシェルスクリプトかbatファイルを直接編集して変更できる)
# 後処理用スクリプトの説明:

# split_gaussian.py

`python split_gaussian.py <logファイルのpath>`
でlogファイルを1つの計算毎にsplitedディレクトリに分割して格納する。これはdeepmd-kit学習用ファイルを作成するためのdpdataが、複数の計算を格納したlogファイルのインポートに対応していないため、分割して1つのディレクトリに格納し、そのディレクトリを読み込む必要があるためである。

# import_gaussian_from_dir.py

`python import_gaussian_from_dir.py <splitedディレクトリのpath>`
で複数のlogファイルをdpdataによりインポートしてdeepmd-kit学習用のrawファイルを生成する。

# plot_from_gaussian.py

`python plot_from_gaussian.py <--plot=2d> </path/to/gaussian.com>`
でgaussian.comの出力をデフォルトでは3次元プロットする。
コマンドライン引数を指定すると2dプロットにすることができる。二次元での計算が保証されている場合に利用する。x,y,zの縮尺は1:1:1になるように固定している。

# オートメーション
`./automation.sh` <number of generate to write>
でgaussianファイルの生成からlogファイルの分割、dpdataによるインポートまでを実行する。



