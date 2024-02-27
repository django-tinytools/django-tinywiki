from ..functions.utils import get_codehilite_styles

def run():
    for style in get_codehilite_styles():
        print(style)