"""Contains and enumerates all company data modules."""
import enum
import glob
from os import path

_python_filepaths = glob.glob(path.join(path.dirname(__file__), "*.py"))
MODULE_NAMES = [
    path.basename(filepath)[:-3]
    for filepath in _python_filepaths
    if path.isfile(filepath) and not
    filepath.endswith('__init__.py')
]
__all__ = MODULE_NAMES


@enum.unique
class RemotePolicy(str, enum.Enum):
    REMOTE_FIRST = "remote-first"
    REMOTE_FRIENDLY = "remote-friendly"
