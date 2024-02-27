from .. import settings

import os

def get_styles():
    css_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","django_tinywiki","styles")
    styles = [os.path.splitext(i)[0] for i in os.listdir(css_dir) 
                if (os.path.isfile(os.path.join(css_dir,i)) and i.endswith('.css'))]
    styles.sort(reverse=False)
    return styles

def get_codehilite_styles():
    css_dir =  os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","django_tinywiki","styles","codehilite")
    styles = [os.path.splitext(i)[0] for i in os.listdir(css_dir) 
                if (os.path.isfile(os.path.join(css_dir,i)) and i.endswith('.css'))]
    styles.sort(reverse=False)
    return styles
