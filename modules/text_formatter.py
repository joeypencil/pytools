from termcolor import colored


_INFO_COLOR = 'cyan'
_SUCCESS_COLOR = 'green'
_ERROR_COLOR = 'red'


def info( phrase: str ) -> str:
    return colored( phrase, _INFO_COLOR )

def success( phrase: str ) -> str:
    return colored( phrase, _SUCCESS_COLOR )

def error( phrase: str ) -> str:
    return colored( phrase, _ERROR_COLOR )