class SetupYDKJ:
    def __init__(self, parser):
        self._parser_ = parser
        self.set_script_help()

    def set_script_help(self):
        parser_intro = self._parser_.add_argument_group(
            'intro',
            'Mit den folgenden Option kann ein spezialles Intro des Spiles einstellt werden.'
        )
        parser_intro = parser_intro.add_mutually_exclusive_group()

        parser_intro.add_argument(
            '-a', '--Muttertag',
            action='store_const',
            const='m9',
            dest='intro',
            help='Muttertag'
        )
        parser_intro.add_argument(
            '-b', '--Vatertag',
            action='store_const',
            const='m10',
            dest='intro',
            help='Vatertag'
        )
        parser_intro.add_argument(
            '-c', '--1Advent',
            action='store_const',
            const='m24',
            dest='intro',
            help='1. Advent'
        )
        parser_intro.add_argument(
            '-d', '--2Advent',
            action='store_const',
            const='m25',
            dest='intro',
            help='2. Advent'
        )
        parser_intro.add_argument(
            '-e', '--3Advent',
            action='store_const',
            const='m26',
            dest='intro',
            help='3. Advent'
        )
        parser_intro.add_argument(
            '-f', '--4Advent',
            action='store_const',
            const='m28',
            dest='intro',
            help='4. Advent'
        )
        parser_intro.add_argument(
            '-g', '--Ostersonntag',
            action='store_const',
            const='m22',
            dest='intro',
            help='Ostersonntag'
        )
        parser_intro.add_argument(
            '-h', '--Ostermontag',
            action='store_const',
            const='m23',
            dest='intro',
            help='Ostermontag'
        )
        parser_intro.add_argument(
            '-i', '--Allerheiligen',
            action='store_const',
            const='m02',
            dest='intro',
            help='Allerheiligen'
        )
        parser_intro.add_argument(
            '-j', '--Rosenmontag',
            action='store_const',
            const='m03',
            dest='intro',
            help='Rosenmontag'
        )
        parser_intro.add_argument(
            '-k', '--Fastnachtsdienstag',
            action='store_const',
            const='m04',
            dest='intro',
            help='Fastnachtsdienstag'
        )
        parser_intro.add_argument(
            '-l', '--Aschermittwoch',
            action='store_const',
            const='m01',
            dest='intro',
            help='Aschermittwoch'
        )
        parser_intro.add_argument(
            '-m', '--1April',
            action='store_const',
            const='m05',
            dest='intro',
            help='1. April'
        )
        parser_intro.add_argument(
            '-n', '--Wheinachtsfeiertag',
            action='store_const',
            const='m06',
            dest='intro',
            help='2. Wheinachtsfeiertag'
        )
        parser_intro.add_argument(
            '-o', '--Faschingsanfang',
            action='store_const',
            const='m08',
            dest='intro',
            help='Faschingsanfang'
        )
        parser_intro.add_argument(
            '-p', '--TagDerArbeit',
            action='store_const',
            const='m11',
            dest='intro',
            help='Tag der Arbeit'
        )
        parser_intro.add_argument(
            '-q', '--Epiphanie',
            action='store_const',
            const='m13',
            dest='intro',
            help='Epiphanie (Heilige 3 Könige)'
        )
        parser_intro.add_argument(
            '-r', '--Nikolaus',
            action='store_const',
            const='m14',
            dest='intro',
            help='Nikolaus'
        )
        parser_intro.add_argument(
            '-s', '--TagDerDeutschenEinheit',
            action='store_const',
            const='m30',
            dest='intro',
            help='Tag der deutschen Einheit'
        )
        parser_intro.add_argument(
            '-t', '--Valentinstag',
            action='store_const',
            const='m31',
            dest='intro',
            help='Valentinstag'
        )
        parser_intro.add_argument(
            '-u', '--Neujahr',
            action='store_const',
            const='m35',
            dest='intro',
            help='Neujahr'
        )
        parser_intro.add_argument(
            '-v', '--Silvester',
            action='store_const',
            const='m36',
            dest='intro',
            help='Silvester'
        )
        parser_intro.add_argument(
            '-w', '--Weihnachten',
            action='store_const',
            const='m33',
            dest='intro',
            help='Weihnachten'
        )
        parser_intro.add_argument(
            '-x', '--nach20Uhr',
            action='store_const',
            const='m60',
            dest='intro',
            help='Spielen nach 20 Uhr'
        )
        parser_intro.add_argument(
            '-y', '--vor9Uhr',
            action='store_const',
            const='m61',
            dest='intro',
            help='Spielen vor 9 Uhr'
        )
        parser_intro.add_argument(
            '-z', '--vor4Uhr',
            action='store_const',
            const='m62',
            dest='intro',
            help='Spielen vor 4 Uhr'
        )
