import random


class SetupYDKJ:
    def __init__(self):
        pass


def extend_parser(parser):
    parser_intro = parser.add_argument_group(
        'intro',
        'Mit den folgenden Option kann ein spezialles Intro des Spiles einstellt werden.'
    )
    parser_intro = parser_intro.add_mutually_exclusive_group()

    intros = [
        'm9',
        'm10',
        'm24',
        'm25',
        'm26',
        'm28',
        'm22',
        'm23',
        'm02',
        'm03',
        'm04',
        'm01',
        'm05',
        'm06',
        'm08',
        'm11',
        'm13',
        'm14',
        'm30',
        'm31',
        'm35',
        'm36',
        'm33',
        'm60',
        'm61',
        'm62',
    ]

    parser_intro.add_argument(
        '-a', '--MothersDay',
        action='store_const',
        const=intros[0],
        dest='intro',
        help='Mother\'s Day (Muttertag)'
    )
    parser_intro.add_argument(
        '-b', '--FathersDay',
        action='store_const',
        const=intros[1],
        dest='intro',
        help='Fathe\'s Day (Vatertag)'
    )
    parser_intro.add_argument(
        '-c', '--1Advent',
        action='store_const',
        const=intros[2],
        dest='intro',
        help='1. Advent'
    )
    parser_intro.add_argument(
        '-d', '--2Advent',
        action='store_const',
        const=intros[3],
        dest='intro',
        help='2. Advent'
    )
    parser_intro.add_argument(
        '-e', '--3Advent',
        action='store_const',
        const=intros[4],
        dest='intro',
        help='3. Advent'
    )
    parser_intro.add_argument(
        '-f', '--4Advent',
        action='store_const',
        const=intros[5],
        dest='intro',
        help='4. Advent'
    )
    parser_intro.add_argument(
        '-g', '--EasterSunday',
        action='store_const',
        const=intros[6],
        dest='intro',
        help='Easter Sunday (Ostersonntag)'
    )
    parser_intro.add_argument(
        '-h', '--EasterMonday',
        action='store_const',
        const=intros[7],
        dest='intro',
        help='Easter Monday (Ostermontag)'
    )
    parser_intro.add_argument(
        '-i', '--AllSaintsDay',
        action='store_const',
        const=intros[8],
        dest='intro',
        help='All Saints\' Day (Allerheiligen)'
    )
    parser_intro.add_argument(
        '-j', '--CarnivalMonday',
        action='store_const',
        const=intros[9],
        dest='intro',
        help='Carnival Monday (Rosenmontag)'
    )
    parser_intro.add_argument(
        '-k', '--ShroveTuesday',
        action='store_const',
        const=intros[10],
        dest='intro',
        help='Shrove Tuesday (Fastnachtsdienstag)'
    )
    parser_intro.add_argument(
        '-l', '--AshWednesday',
        action='store_const',
        const=intros[11],
        dest='intro',
        help='Ash Wednesday (Aschermittwoch)'
    )
    parser_intro.add_argument(
        '-m', '--1April',
        action='store_const',
        const=intros[12],
        dest='intro',
        help=' (1. April)'
    )
    parser_intro.add_argument(
        '-n', '--BoxingDay',
        action='store_const',
        const=intros[13],
        dest='intro',
        help='Boxing Day (2. Weihnachtsfeiertag)'
    )
    parser_intro.add_argument(
        '-o', '--Carnivalbegin',
        action='store_const',
        const=intros[14],
        dest='intro',
        help='Carnival begin (Faschingsanfang)'
    )
    parser_intro.add_argument(
        '-p', '--LabourDay',
        action='store_const',
        const=intros[15],
        dest='intro',
        help='Labour Day (Tag der Arbeit)'
    )
    parser_intro.add_argument(
        '-q', '--Epiphany',
        action='store_const',
        const=intros[16],
        dest='intro',
        help='Epiphany (Heilige 3 Könige)'
    )
    parser_intro.add_argument(
        '-r', '--Nikolaus',
        action='store_const',
        const=intros[17],
        dest='intro',
        help='Nikolaus'
    )
    parser_intro.add_argument(
        '-s', '--GermanUnityDay',
        action='store_const',
        const=intros[18],
        dest='intro',
        help='German Unity Day (Tag der deutschen Einheit)'
    )
    parser_intro.add_argument(
        '-t', '--ValentinesDay',
        action='store_const',
        const=intros[19],
        dest='intro',
        help='Valentine\'s Day (Valentinstag)'
    )
    parser_intro.add_argument(
        '-u', '--NewYear',
        action='store_const',
        const=intros[20],
        dest='intro',
        help='New Year (Neujahr)'
    )
    parser_intro.add_argument(
        '-v', '--NewYearsEve',
        action='store_const',
        const=intros[21],
        dest='intro',
        help='New Year\'s Eve (Silvester)'
    )
    parser_intro.add_argument(
        '-w', '--Christmas',
        action='store_const',
        const=intros[22],
        dest='intro',
        help='Christmas (Weihnachten)'
    )
    parser_intro.add_argument(
        '-x', '--after8pm',
        action='store_const',
        const=intros[23],
        dest='intro',
        help='playing after 8pm (Spielen nach 20 Uhr)'
    )
    parser_intro.add_argument(
        '-y', '--before9am',
        action='store_const',
        const=intros[24],
        dest='intro',
        help='playing before 9am (Spielen vor 9 Uhr)'
    )
    parser_intro.add_argument(
        '-z', '--before4m',
        action='store_const',
        const=intros[25],
        dest='intro',
        help='playing before 4am (Spielen vor 4 Uhr)'
    )
    parser_intro.add_argument(
        '--original',
        action='store_const',
        const='original',
        dest='intro',
        help='insert the original file'
    )
    parser_intro.add_argument(
        '--random',
        action='store_const',
        const=random.choice(intros),
        dest='intro',
        help='playing before 4am (Spielen vor 4 Uhr)'
    )
