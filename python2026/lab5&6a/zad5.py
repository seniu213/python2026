##### Zadanie 5
## Krok 1: wygeneruj dane testowe.
## Utworz folder i dodaj 5 plikow tekstowych, kazdy z > 5 zdaniami.
## Nazwy plikow: Text1ID_ABC.txt, Text2ID_405.txt, Text3ID_607.txt,
## Text4ID_ABC5.txt, Text5ID_DEF.txt.
## Utworz funkcje z wieloma argumentami, ktora:
## a) wypisuje wszystkie pliki z folderu,
## b) jesli nazwa zawiera 'ABC', zlicza slowa o dlugosci > 3.
## Dla Lab6: udekoruj funkcje i dodaj:
## a) policz, ile plikow ma '0' w nazwie,
## b) jesli plik ma '0' w nazwie, policz slowa w tresci,
## c) jesli nazwa zawiera 'EF.txt', skopiuj plik do 'DocumentLab5copy'.

from pathlib import Path
from shutil import copy2


def create_test_files(folder):
    """Tworzy pliki testowe."""
    text = (
        'Python is very popular language. '
        'Students write many small scripts. '
        'This file has enough example sentences. '
        'Data processing can be simple and fast. '
        'Practice helps to understand programming better. '
        'Learning by tasks is effective every week.'
    )

    filenames = [
        'Text1ID_ABC.txt',
        'Text2ID_405.txt',
        'Text3ID_607.txt',
        'Text4ID_ABC5.txt',
        'Text5ID_DEF.txt',
    ]

    folder.mkdir(parents=True, exist_ok=True)
    for name in filenames:
        (folder / name).write_text(text, encoding='utf-8')

    return filenames


def extra_actions_decorator(func):
    def wrapper(folder, *filenames):
        result = func(folder, *filenames)

        zero_count = 0
        copy_folder = folder.parent / 'DocumentLab5copy'
        copy_folder.mkdir(parents=True, exist_ok=True)

        for filename in filenames:
            path = folder / filename
            if '0' in filename:
                zero_count += 1
                words = path.read_text(encoding='utf-8').split()
                print(f'{filename} -> liczba slow (ma 0): {len(words)}')

            if 'EF.txt' in filename:
                copy2(path, copy_folder / filename)
                print(f'Skopiowano: {filename} -> {copy_folder}')

        print('Pliki z 0 w nazwie:', zero_count)
        return result

    return wrapper


@extra_actions_decorator
def analyze_files(folder, *filenames):
    print('Pliki w folderze:')
    for filename in filenames:
        print(filename)

    for filename in filenames:
        path = folder / filename
        if 'ABC' in filename:
            words = path.read_text(encoding='utf-8').split()
            count_gt3 = len([w for w in words if len(w.strip('.,!?')) > 3])
            print(f'{filename} -> slowa > 3 znaki: {count_gt3}')


base_folder = Path('DocumentLab5')
created_files = create_test_files(base_folder)
analyze_files(base_folder, *created_files)
