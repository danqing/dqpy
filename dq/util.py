import os
import pathlib
import shutil


def safe_cast(value, to_type, default=None):
    """Cast a value to another type safely.

    :param value: The original value.
    :param type to_type: The destination type.
    :param default: The default value.
    """
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default


def mkdirp(path):
    """Safely mkdir, creating all parent folders if they don't yet exist.

    This doesn't raise an error if the folder already exists. However, it does
    raise ``FileExistsError`` if the path points to an existing file.

    :param string path: The path to the folder to be created.
    """
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def rmrf(path):
    """Remove a path like rm -rf.

    :param string path: The path to remove.
    """
    try:
        shutil.rmtree(path)
    except NotADirectoryError:
        os.remove(path)
    except FileNotFoundError:
        return


def traverse(path, callback):
    """Traverse a directory recursively, performing a task.

    :param string path: The path of the directory.
    :param func callback: A callback applied to each child file and directory.
        It takes 2 arguments, the relative path from the root, and whether the
        item is a directory.
    """
    if not os.path.isdir(path):
        raise (
            NotADirectoryError(20, 'Not a directory', path)
            if os.path.exists(path) else
            FileNotFoundError(2, 'No such file or directory', path)
        )

    path = os.path.join(path, '')
    pathlen = len(path)
    for cwd, dirs, files in os.walk(path):
        for d in dirs:
            callback(os.path.join(cwd, d)[pathlen:], True)
        for f in files:
            callback(os.path.join(cwd, f)[pathlen:], False)
