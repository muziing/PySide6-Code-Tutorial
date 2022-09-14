"""
调用cloc代码行数统计工具统计本项目代码量的脚本

https://github.com/AlDanial/cloc
"""

import pathlib
from os import popen

# 配置项
Git_Ignore_File = "../.gitignore"  # gitignore文件路径，用以排除不需要列目录的文件
Project_Root_Path = "../"  # 项目根目录路径
# 配置项完


def cloc(gitignore_file: str = ".gitignore") -> None:
    """
    使用cloc统计项目代码行数 \n
    :param gitignore_file: gitignore文件路径
    :return: None
    """

    ignored_dir = ""
    gitignore_file_p = pathlib.Path(gitignore_file)
    with gitignore_file_p.open("r", encoding="UTF-8") as f:
        for dir_name in f.readlines():
            if not dir_name.startswith("#"):
                dir_name = dir_name.replace("/", "").replace("\n", ",")
                ignored_dir += dir_name

    # 调用cloc，并排除gitignore中的目录，需要提前将cloc添加到系统环境变量
    cmd = f"cloc --exclude-dir {ignored_dir} {Project_Root_Path}"

    with popen(cmd) as p:
        cmd_result = p.read()
        # 如果cmd执行正常退出则p.close()返回None，失败则返回状态码
        if p.close():
            print("cloc调用失败，请检查")
        else:
            # 根据cloc返回结果，连续两个换行符后面的内容是需要的信息
            cloc_result = cmd_result.split("\n\n", 1)[1]
            print(cloc_result)
    # TODO 将 self.cloc_result 写入 Markdown 文件


if __name__ == "__main__":
    cloc(Git_Ignore_File)
