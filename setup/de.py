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
            '-a', '--MothersDay',
            action='store_const',
            const='m9',
            dest='intro',
            help='Mother\'s Day (Muttertag)'
        )
        parser_intro.add_argument(
            '-b', '--FathersDay',
            action='store_const',
            const='m10',
            dest='intro',
            help='Fathe\'s Day (Vatertag)'
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
            '-g', '--EasterSunday',
            action='store_const',
            const='m22',
            dest='intro',
            help='Easter Sunday (Ostersonntag)'
        )
        parser_intro.add_argument(
            '-h', '--EasterMonday',
            action='store_const',
            const='m23',
            dest='intro',
            help='Easter Monday (Ostermontag)'
        )
        parser_intro.add_argument(
            '-i', '--AllSaintsDay',
            action='store_const',
            const='m02',
            dest='intro',
            help='All Saints\' Day (Allerheiligen)'
        )
        parser_intro.add_argument(
            '-j', '--CarnivalMonday',
            action='store_const',
            const='m03',
            dest='intro',
            help='Carnival Monday (Rosenmontag)'
        )
        parser_intro.add_argument(
            '-k', '--ShroveTuesday',
            action='store_const',
            const='m04',
            dest='intro',
            help='Shrove Tuesday (Fastnachtsdienstag)'
        )
        parser_intro.add_argument(
            '-l', '--AshWednesday',
            action='store_const',
            const='m01',
            dest='intro',
            help='Ash Wednesday (Aschermittwoch)'
        )
        parser_intro.add_argument(
            '-m', '--1April',
            action='store_const',
            const='m05',
            dest='intro',
            help=' (1. April)'
        )
        parser_intro.add_argument(
            '-n', '--BoxingDay',
            action='store_const',
            const='m06',
            dest='intro',
            help='Boxing Day (2. Weihnachtsfeiertag)'
        )
        parser_intro.add_argument(
            '-o', '--Carnivalbegin',
            action='store_const',
            const='m08',
            dest='intro',
            help='Carnival begin (Faschingsanfang)'
        )
        parser_intro.add_argument(
            '-p', '--LabourDay',
            action='store_const',
            const='m11',
            dest='intro',
            help='Labour Day (Tag der Arbeit)'
        )
        parser_intro.add_argument(
            '-q', '--Epiphany',
            action='store_const',
            const='m13',
            dest='intro',
            help='Epiphany (Heilige 3 Könige)'
        )
        parser_intro.add_argument(
            '-r', '--Nikolaus',
            action='store_const',
            const='m14',
            dest='intro',
            help='Nikolaus'
        )
        parser_intro.add_argument(
            '-s', '--GermanUnityDay',
            action='store_const',
            const='m30',
            dest='intro',
            help='German Unity Day (Tag der deutschen Einheit)'
        )
        parser_intro.add_argument(
            '-t', '--ValentinesDay',
            action='store_const',
            const='m31',
            dest='intro',
            help='Valentine\'s Day (Valentinstag)'
        )
        parser_intro.add_argument(
            '-u', '--NewYear',
            action='store_const',
            const='m35',
            dest='intro',
            help='New Year (Neujahr)'
        )
        parser_intro.add_argument(
            '-v', '--NewYearsEve',
            action='store_const',
            const='m36',
            dest='intro',
            help='New Year\'s Eve (Silvester)'
        )
        parser_intro.add_argument(
            '-w', '--Christmas',
            action='store_const',
            const='m33',
            dest='intro',
            help='Christmas (Weihnachten)'
        )
        parser_intro.add_argument(
            '-x', '--after8pm',
            action='store_const',
            const='m60',
            dest='intro',
            help='playing after 8pm (Spielen nach 20 Uhr)'
        )
        parser_intro.add_argument(
            '-y', '--before9am',
            action='store_const',
            const='m61',
            dest='intro',
            help='playing before 9am (Spielen vor 9 Uhr)'
        )
        parser_intro.add_argument(
            '-z', '--before4m',
            action='store_const',
            const='m62',
            dest='intro',
            help='playing before 4am (Spielen vor 4 Uhr)'
        )
