import pathlib
import sys


def get_running_module_path() -> pathlib.Path:
    """
    gives the running python module path
    ex.: if `python -m bot` was run, gives 'bot' directory path
    ex.: if `python bot.py` was run, gives 'bot.py' script path
    :return:
    """
    path = pathlib.Path(sys.modules['__main__'].__file__)
    if path.name == "__main__.py":
        path = path.parent
    return path
