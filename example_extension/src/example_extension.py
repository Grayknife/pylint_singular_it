# Inside hello_plugin.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.
    :param linter: The linter to register the checker to.
    """
    pass


def load_configuration(linter):
    """"""
    # Specify the configuration here.
    # As example
    # linter.config.line_length = 120
