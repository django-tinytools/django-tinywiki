from .. import settings

def run():
    for lcode,lname in settings.TINYWIKI_LANGUAGES:
        print("{}\t{}".format(lcode,lname))