# \bin\python3
import argparse
import importlib
import pkgutil
import setup


class Local:
    package = 'setup'

    def __init__(self, name, parser):
        self.name = name
        tmp = importlib.import_module('.' + name, self.package)
        self.setup = tmp.SetupYDKJ(parser)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup your "You don\'t know Jack" game.', conflict_handler='resolve')
    subparsers = parser.add_subparsers(help='local help')
    locales = {}

    for _, name, _ in pkgutil.iter_modules([Local.package]):
        sub_parser = subparsers.add_parser(name, help=name + ' help', conflict_handler='resolve')
        locales[name] = Local(name, sub_parser)

    parser.parse_args()
# del sys.argv[1]
