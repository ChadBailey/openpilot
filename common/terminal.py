from string import Template

from common.constants import TERM_TEMPLATES, TERM_THEMES

class TerminalString:
    """
    Terminal String

    String formatter which applies the selected terminal theme to the supplied 
    text.

    Default Theme: NONE
    Themes: NONE, RUNNING, STOPPED

    Example usage:

    ```ipython
    >>> from common.terminal import TerminalString, TERM_THEMES
    >>> test = TerminalString("This is a string",TERM_THEMES.RUNNING)
    >>> print(test)
    This is a string
    >>> test.raw
    '\x1b[32mThis is a string\x1b[0m'
    >>> test
    <common.terminal.TerminalString: "This is a string" with theme TERM_THEMES.RUNNING at 0x7fc7fe45dd00>
    ```
    """
    def __init__(
        self,
        text: str = "",
        theme: TERM_THEMES = TERM_THEMES.NONE
    ):
        self.text = text
        self.theme = theme
        if self.theme == TERM_THEMES.NONE:
            self.themed_text = self.text
        elif self.theme == TERM_THEMES.RUNNING:
            self.themed_text = TERM_TEMPLATES.RUNNING.substitute(process_name=self.text)
        elif self.theme == TERM_THEMES.STOPPED:
            self.themed_text = TERM_TEMPLATES.RUNNING.substitute(process_name=self.text)
        else:
            raise NotImplementedError(f"Theme {self.theme} not yet supported")

    @property
    def raw(self):
        return self.themed_text

    def __str__(self) -> str:
        return self.text

    def __repr__(self):
        return f'<{self.__module__}.{type(self).__name__}: "{self.text}" with theme {self.theme} at {hex(id(self))}>'
