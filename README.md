# random_coords_for_gaussian
本プロジェクトは科学技術の発展振興のため、GPL3.0により公開する。


# 設計の説明:
Atom, AtomClusterInterface, GeneralAtomCluster, FourAtomCluster, GaussianWriterの4つのクラスを定義している。

Atom型は、原子の名前、座標の情報を持つデータ型である。座標はnumpyの配列として格納する。そのように定義することで数学的なベクトル演算が簡単かつ高速に行えるようになる。
AtomClusterInterfaceはAtomのリストをもつ。GeneralAtomCluster, FourAtomClusterの継承元となるインターフェースであり、一般の原子系に適用可能なプロットメソッドと原子の座標取得メソッドを実装している。

GeneralAtomClusterはAtomClusterInterfaceを継承し、将来的にN原子系に対応する。
FourAtomCluster型は、4つのAtom型リストに特化した型として定義した。これにより一般のN原子系のルーチンと分け、呼び出し元はAtomClusterInterfaceを参照するようにすることで将来的な保守性を高めるように設計した。

これらのクラスをgenerate_gaussian_fileパッケージからimportしてmainプログラムを作成することで必要に応じて座標の配置、可視化、そして配置した座標をもとに原子間距離とグラフの交差を基準にして実現可能性のある原子配置をGaussian用の計算ファイルに必要な数だけ書き込むことができる。
```bash
/generate_gaussian_file/generate_gaussian_file.py <number to loop> <dimension>
```
で1~3次元の配置を指定回数行う。

# インストールと実行
インストールはDockerイメージにより簡単に行うことができる。requirements.txtを参照して直接パッケージをインストールして実行することも可能。
```bash
docker run
```
コマンドで仮想のコンソールに入り、そこからpythonを起動することができる。イメージ作成手順は以下。

cdしたのち、
```bash
docker build -t <your_image_name> .
```
(最後のドットに注意！)
でイメージを作成して
```bash
docker images
```
で作成した名前のイメージがあることを確認し、
```bash
docker run -it --rm <your_image_name>
```
とするとdockerに構築された環境のシェルに入ることができる。これで仮想環境でシェルコマンドやPythonを実行することができる。Dockerコンテナのマウントについては割愛。

dockerを利用しない場合にはvenvで環境を構築することができる。
プロジェクトのルートにcdして、install用のシェルスクリプト、batファイルを実行する。仮想環境がプロジェクトのルートディレクトリに作成されたことを確認した後
```bash
source venv/bin/activate
```
(Unixの場合,Winはバックスラッシュ)
のようにして仮想環境に入ることができる。(仮想環境の名前はシェルスクリプトかbatファイルを直接編集して変更できる)
# 後処理用スクリプトの説明:

# split_gaussian.py

```bash
python split_gaussian.py <logファイルのpath>
```
でlogファイルを1つの計算毎にsplitedディレクトリに分割して格納する。これはdeepmd-kit学習用ファイルを作成するためのdpdataが、複数の系(異なる分子の種類)を格納したlogファイルのインポートに対応していないため、分割して1つのディレクトリに格納し、そのディレクトリを読み込む必要があるためである。

# import_gaussian_from_dir.py

```bash
python import_gaussian_from_dir.py <splitedディレクトリのpath>
```
で複数の系をもつlogファイルをdpdataによりインポートしてdeepmd-kit学習用のrawファイル及びnpyファイルを生成する。

# import_gaussian_multiframes.py

```bash
python import_gaussian_multiframes.py <file path to import>
```
で単一分子について複数の計算結果を格納したlogファイルをインポートして学習用ファイルを生成する。(dimension)_set_(index).logという命名規則に従っていないものはエラーを返すようにしている。

# remove_error.py

```bash
python remove_error.py <path to directory>
```
で、指定ディレクトリに存在するすべてのlogファイルに対して異常終了部を消去した上で、すべての結果をマージした新たなlogファイルを作成する。適宜リネームしてインポート用のスクリプトで学習データセットを作る。

# plot_from_gaussian.py

```bash
python plot_from_gaussian.py <--plot=2d> </path/to/gaussian.com>
```
でgaussian.comの出力をデフォルトでは3次元プロットする。
コマンドライン引数を指定すると2dプロットにすることができる。二次元での計算が保証されている場合に利用する。x,y,zの縮尺は1:1:1になるように固定している。

# plot_from_lammps_dump.py

```bash
python plot_from_lammps_dump.py /path/to/dump
```
でlammpsのdumpファイルを読み込んで3次元プロットする。カレントディレクトリの直下に同名のディレクトリが作成され、その中にすべてのステップをプロットした画像が保存される。

# plot_from_lammps_dump_2d.py

```bash
python plot_from_lammps_dump_2d.py /path/to/dump
```

# オートメーション
```bash
cd <project_root_directory>
./automation.sh <number of generate to write> <dimension>
```
で指定した次元配置の分子を指定回数生成し、gaussian logファイルの生成までを行う。

```bash
cd <project_root_directory>
./batch.sh <number of generate to write in each file> <dimension>
```
でautomation.shの実行を複数回、バックグラウンドで行うことができる。バッチ処理の回数はautomation.shにハードコーディングしている。



