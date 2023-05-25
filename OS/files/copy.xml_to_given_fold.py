# Дан путь к папке (через cmd). Нужно найти и скопировать все файлы с расширением .xml, в котором есть тег
# `<SAVE>...</SAVE>`
# 2. В папку, указанную в значении тега `<SAVE>...</SAVE>` (могут быть разными для каждого файла).


from pathlib import *
import argparse
from collections import deque
import re
import shutil


def copy_files(src: str | Path, ext: str = '.xml') -> None:
    dst = None
    queue = deque([src])
    pat = r'<save>(.*?)<'

    while queue:
        p = Path(queue.popleft())

        if p.is_file():

            if p.suffix == ext:
                text = p.read_text()

                if '<save>' in text or '<save>'.upper() in text:
                    dst = re.search(pat, text, flags=re.DOTALL).groups()[0]
                    dst = Path(dst)

                    if not dst.exists() or not dst.is_dir():
                        Path.mkdir(dst)

                    file_name = dst / p.parts[-1]
                    Path(file_name).touch()
                    shutil.copyfile(p, file_name)

        else:
            for elem in p.iterdir():
                queue.append(elem)


src = 'C:\\Users\\andre\\PycharmProjects\\Studying\\OS\\files\\test2'
copy_files(src)