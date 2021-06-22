import os
import shutil
from os.path import exists
from os.path import join


# Comment from cloning repository
# Comment from first repository
# Second comment from repos
# Comment from clone repos in beta-branch
# Second comment from clone repos in beta
# Resolve merge conflict

def empty_func():
    pass


SORTED_DIRECTORY = 'A:\\Downloads'

VIDEOS_PATH = join(SORTED_DIRECTORY, 'Videos')
VIDEOS = ('.mkv', '.avi', '.mp4', '.mpeg', '.asf', '.f4v', '.flv',
          '.h264', '.h265', '.m4v', '.mod', '.mpg', '.moov', '.mov',
          '.mts', '.rm', '.rmvb', '.vcd', '.vid', '.vob', '.webm',
          '.wmv', '.yuv')

PICTURES_PATH = join(SORTED_DIRECTORY, 'Pictures')
PICTURES = ('.bmp', '.gif', '.jpg', '.jpeg', '.jpe', '.jfif',
            '.jp2', '.j2k', '.jpf', '.jpm', '.jpg2', '.j2c',
            '.jpc', '.png', '.tiff', '.tif', '.jxr', '.hdp',
            '.wdp', '.webp')

DOCUMENTS_PATH = join(SORTED_DIRECTORY, 'Documents')
DOCUMENTS = ('.doc', '.docx', '.xls', '.xlsx', '.pdf', '.rtf', 'odt',
             '.docm', '.dot', '.dotm', '.dotx', '.xls', '.xlsx,',
             '.xlsm', '.xlsb', '.csv', '.xltx', '.xltm', '.ppt',
             '.pptx', '.ods', '.odp')

MUSIC_PATH = join(SORTED_DIRECTORY, 'Music')
MUSIC = ('.mp3', '.aac', '.ac3', '.m4a', '.m4p', '.mid', '.midi',
         '.mpa', '.ogg', '.ra', '.wav', '.wma', '.flac', '.alac')

IMAGES_PATH = join(SORTED_DIRECTORY, 'Images')
IMAGES = ('.iso', '.img', '.wim')

TORRENTS_PATH = join(SORTED_DIRECTORY, 'Torrents')
TORRENTS = ('.torrent')

ARCHIVES_PATH = join(SORTED_DIRECTORY, 'Archives')
ARCHIVES = ('.zip', '.rar', '.7z', '.ace', '.arj', '.gz', '.gzip')

EXECUTABLE_FILES_PATH = join(SORTED_DIRECTORY, 'Programms')
EXECUTABLE_FILES = ('.exe', '.msi', '.vb', '.vbs', '.cmd', '.bat',
                    '.run', '.sh', '.tar', '.tar-gz', '.tgz', '.zipx')

file_format_list = [[VIDEOS, VIDEOS_PATH], [PICTURES, PICTURES_PATH],
                    [DOCUMENTS, DOCUMENTS_PATH], [MUSIC, MUSIC_PATH],
                    [IMAGES, IMAGES_PATH], [TORRENTS, TORRENTS_PATH],
                    [ARCHIVES, ARCHIVES_PATH],
                    [EXECUTABLE_FILES, EXECUTABLE_FILES_PATH]]


def sort(path, file_format, new_location):
    """
    Перемещает файл path в каталог new_location,
    если он имеет расширение из списка file_format
    """

    _, ext = os.path.splitext(path)
    _, file_name = os.path.split(path)
    postfix = 0

    if ext.lower() in file_format:

        new_path = os.path.join(new_location, file_name)
        tmp_path = new_path

        while os.path.exists(tmp_path):  # если файл с именем dst уже доступен
            postfix += 1
            root, ext = os.path.splitext(new_path)
            tmp_path = '%s_%d%s' % (root, postfix, ext)
            # print(tmp_path)

        new_path = tmp_path
        return shutil.move(path, new_path)


def checkDir(dir_path):
    """
    Проверяет, существует ли каталог dir_path,
    если нет, то создает его.
    """

    if not exists(dir_path):
        os.makedirs(dir_path)


def getFilesToSort(sorted_directory):
    """
    Возвращает список путей всех файлов из сортируемого каталога
    """

    files_list = []
    dir_items = os.listdir(sorted_directory)

    for item in dir_items:
        item_path = os.path.join(sorted_directory, item)

        if os.path.isdir(item_path):
            continue
        else:
            files_list.append(item_path)

    return files_list


def main():
    count = 0
    files_list = getFilesToSort(SORTED_DIRECTORY)

    for sorted_file in files_list:

        new_path = None
        count += 1

        print(count, sorted_file, end=' ')

        for file_format, file_format_path in file_format_list:
            checkDir(file_format_path)
            new_path = sort(sorted_file, file_format, file_format_path)

            if new_path is not None:
                print('moved in', file_format_path)
                break

        if new_path is None:
            print('have unknown format.')


if __name__ == '__main__':
    main()
    input('Press any key to close the programm.')
