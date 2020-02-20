# \bin\python3
import argparse
from os.path import isdir, isfile, join
from pathlib import Path
from pkgutil import iter_modules
from shutil import copyfile

_package = 'setup'


class Arguments:
    def __init__(self):
        self.intro = None
        self.dir = None
        self.locale = None
        self.reset_highscore = False


if __name__ == '__main__':

    args = Arguments()

    parser_all = argparse.ArgumentParser(description='Setup your "You don\'t know Jack" game.',
                                         conflict_handler='resolve')
    parser_all.add_argument(
        '--resetHighscore',
        dest='reset_highscore',
        action='store_true',
        help='resetting the highscore list'
    )
    subparsers = parser_all.add_subparsers(help='Manipulation of the localized intros at the start of the game.',
                                           dest="locale")
    locales = {}

    for _, name, _ in iter_modules([_package]):
        sub_parser = subparsers.add_parser(name, help='Options to set intors for the locale ' + name,
                                           conflict_handler='resolve')
        locales[name] = __import__(_package + '.' + name, globals(), locals(), ['extend_parser'], 0)
        # locales[name] = import_module('.' + name, _package)
        locales[name].extend_parser(sub_parser)
    parser_all.add_argument('dir', help='directory of the YDKJ game')

    parser_all.parse_args(namespace=args)

    dir_error = ArithmeticError('this ist not a valid YDKJ game directory')

    if not isdir(args.dir):
        raise dir_error

    highscore = join(args.dir, 'AUTOBAHN/HISCORE.DKJ')
    USD = join(args.dir, 'AUTOBAHN/USD.TXT')
    USD_BAK = join(args.dir, 'AUTOBAHN/USD.TXT.BAK')

    if not isfile(highscore) or not isfile(USD):
        raise dir_error

    if args.reset_highscore:
        highscore_path = Path(highscore)
        highscore_path.unlink()
        highscore_path.touch()

    if args.intro is None:
        pass
    elif 'original' in args.intro:
        if isfile(USD_BAK):
            copyfile(USD_BAK, USD)
        else:
            copyfile(USD, USD_BAK)
    else:
        if not isfile(USD_BAK):
            copyfile(USD, USD_BAK)

        with open(USD, 'w') as usd:
            usd.write('WHEN=INTRO // custom intro file \r\n')
            usd.write('\r\n')
            for intro in set(args.intro):
                if intro:
                    usd.write(
                        'TYPE=TIME TIME=0:00 WHEN=AFTER SOUND={intro}\r\n'.format(intro=intro))
