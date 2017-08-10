# \bin\python3

if __name__ == '__main__':
    import argparse
    import pkgutil
    import sys

    languages = [name for _, name, _ in pkgutil.iter_modules(['logic'])]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('lang', choices=languages, help='Choose the language/version of the game.')

    if len(sys.argv) == 1:

        exit()

    del sys.argv[1]
    print(sys.argv)
