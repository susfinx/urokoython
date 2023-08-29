# Задание No6
# 📌 Напишите код, который запускается из командной строки и получает на вход путь до
# директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import argparse
from pathlib import Path
from collections import namedtuple

logging.basicConfig(filename='task15_04.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', ['имя', 'расширение', 'это_каталог', 'родительский_каталог'])

def read_dir(путь):
    путь = Path(путь)
    for файл in путь.iterdir():
        это_каталог = файл.is_dir()
        имя = файл.stem if это_каталог else файл.name
        расширение = файл.suffix if not это_каталог else ""
        родительский_каталог = файл.parent.name if это_каталог else файл.parent.stem

        f = File(имя, расширение, это_каталог, родительский_каталог)
        logger.info(f)

        if f.это_каталог:
            read_dir(файл)

def parse():
    parser = argparse.ArgumentParser(prog='get_path', description='Получает на вход путь до директории', epilog='Пример: get_path /urok2')
    parser.add_argument('путь', type=str, help='Путь до директории')

    args = parser.parse_args()
    read_dir(args.путь)

if __name__ == "__main__":
    parse()


