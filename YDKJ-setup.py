# \bin\python3
import argparse
import importlib
import os
import pkgutil

import setup

_package = 'setup'


class Arguments:
    def __init__(self):
        self.intro = None
        self.dir = None
        self.locale = None


if __name__ == '__main__':

    args = Arguments()

    parser_all = argparse.ArgumentParser(description='Setup your "You don\'t know Jack" game.',
                                         conflict_handler='resolve')
    subparsers = parser_all.add_subparsers(help='local help')
    locales = {}

    for _, name, _ in pkgutil.iter_modules([_package]):
        sub_parser = subparsers.add_parser(name, dest='locale', help=name + ' help', conflict_handler='resolve')
        locales[name] = importlib.import_module('.' + name, _package)
        locales[name].extend_parser(sub_parser)
    parser_all.add_argument('dir', nargs=1, help='directory of the YDKJ game')

    parser_all.parse_args(namespace=args)

    dir_error = ArithmeticError('this ist not a valid YDKJ game directory')

    if not os.path.isdir(args.dir):
        raise dir_error

    highscore = os.path.join(args.dir, 'AUTOBAHN/HISCORE.DKJ')
    USD = os.path.join(args.dir, 'AUTOBAHN/USD.TXT')

    if not os.path.isfile(highscore) or not os.path.isfile(USD):
        raise dir_error
