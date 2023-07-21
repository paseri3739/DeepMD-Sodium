from typing import List, Tuple


class GaussianWriter:
    # インスタンス全てで共有するデフォルト値はここで定義しておく
    default_header: str = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"

    # コンストラクタ。ファイルパスと原子の種類を受け取る。インスタンス毎に変えるべき初期値はここで定義する。
    # 都度変わるインスタンス変数はself.で定義する。
    def __init__(self, file_path: str, atom: str):
        self.file_path = file_path
        self.header = self.default_header  # デフォルトヘッダを代入
        self.atom = atom

    def set_header(self, header: str = default_header) -> None:
        self.header = header

    def format_coord(self, coords: List[Tuple[float, float, float]]) -> str:
        lines: List[str] = []
        for i, coord in enumerate(coords):
            line = f"{self.atom}    {coord[0]}    {coord[1]}    {coord[2]}\n"
            lines.append(line)
        return "".join(lines)

    def write(self, coords_list: List[List[Tuple[float, float, float]]]) -> None:
        with open(self.file_path, "w") as file:
            for i, coords in enumerate(coords_list):
                if self.header is not None:
                    file.write(self.header)
                file.write(self.format_coord(coords))
                if i < len(coords_list) - 1:
                    file.write("\n--Link1--\n")
            file.write("\n")
