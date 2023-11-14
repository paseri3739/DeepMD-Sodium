import os
from ase.io import read, write
from ase.calculators.gaussian import Gaussian

# ディレクトリ内の全ての.xyzファイルをリストアップ
xyz_files = [f for f in os.listdir("./coordinates") if f.endswith(".xyz")]

# 出力ディレクトリが存在しない場合は作成
output_dir = "./coordinates_for_gaussian"
os.makedirs(output_dir, exist_ok=True)

# 各ファイルに対して変換処理を実行
for xyz in xyz_files:
    # ファイル名から拡張子を除いた名前を取得
    name = os.path.splitext(xyz)[0]
    # XYZファイルを読み込む
    atoms = read(f"./coordinates/{xyz}")

    # Gaussianの計算設定を定義
    calc = Gaussian(
        label=f"{output_dir}/{name}",
        method="B3LYP",
        basis="6-311+g(d) force",
        nprocshared=16,
        mem="14GB",
        chk="checkpoint.chk",
        mult=2,
    )

    # 計算器をatomsオブジェクトに割り当てる
    atoms.calc = calc

    # ジョブスクリプトの書き出しを実行（入力ファイルと同じディレクトリに）
    atoms.calc.write_input(atoms)

    # この例では計算は実行せず、入力ファイルの生成のみ行う
    # 実際に計算を実行する場合は以下のコメントを外す
    # atoms.get_potential_energy()

# 全てのXYZファイルに対して処理が完了したことを表示
print("Gaussian input files have been created for all XYZ files.")
