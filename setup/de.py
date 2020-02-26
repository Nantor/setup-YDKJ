import argparse
from datetime import datetime, timedelta
from random import choice

from util.util import first_advent, spencer_easter_formula

INTROS = ['m9', 'm10', 'm24', 'm25', 'm26', 'm28', 'm22', 'm23', 'm02', 'm03', 'm04', 'm01', 'm05', 'm06', 'm08',
          'm11', 'm13', 'm14', 'm30', 'm31', 'm35', 'm36', 'm33', 'm60', 'm61', 'm62', ]


def set_intro_for_today():
    val_dt = datetime.now()
    val_d = val_dt.date()

    # Mother\'s Day (Muttertag)
    if val_d.month == 5 and val_d.weekday() == 6 and 7 < val_d.day < 15:
        return INTROS[0]

    easter_sunday = spencer_easter_formula(val_d.year)

    # Fathe\'s Day (Vatertag)
    if easter_sunday + timedelta(days=39) == val_d:
        return INTROS[1]

    advent_first = first_advent(val_d.year)

    # 1. Advent
    if advent_first == val_d:
        return INTROS[2]

    # 2. Advent
    if advent_first + timedelta(weeks=1) == val_d:
        return INTROS[3]

    # 3. Advent
    if advent_first + timedelta(weeks=2) == val_d:
        return INTROS[4]

    # 4. Advent
    if advent_first + timedelta(weeks=3) == val_d:
        return INTROS[5]

    # Easter Sunday (Ostersonntag)
    if easter_sunday == val_d:
        return INTROS[6]

    # Easter Monday (Ostermontag)
    if easter_sunday + timedelta(days=1) == val_d:
        return INTROS[7]

    # All Saints\' Day (Allerheiligen)
    if val_d.month == 11 and val_d.day == 1:
        return INTROS[8]

    # Carnival Monday (Rosenmontag)
    if easter_sunday - timedelta(days=48) == val_d:
        return INTROS[9]

    # Shrove Tuesday (Fastnachtsdienstag)
    if easter_sunday - timedelta(days=47) == val_d:
        return INTROS[10]

    # Ash Wednesday (Aschermittwoch)
    if easter_sunday - timedelta(days=46) == val_d:
        return INTROS[11]

    # April Fool\'s Day (1. April)
    if val_d.month == 4 and val_d.day == 1:
        return INTROS[12]

    # Boxing Day (2. Weihnachtsfeiertag)
    if val_d.month == 12 and val_d.day == 26:
        return INTROS[13]

    # Carnival begin (Faschingsanfang)
    if val_d.month == 11 and val_d.day == 11:
        return INTROS[14]

    # Labour Day (Tag der Arbeit)
    if val_d.month == 5 and val_d.day == 1:
        return INTROS[15]

    # Epiphany (Heilige 3 Könige)
    if val_d.month == 1 and val_d.day == 5:
        return INTROS[16]

    # Nikolaus
    if val_d.month == 12 and val_d.day == 6:
        return INTROS[17]

    # German Unity Day (Tag der deutschen Einheit)
    if val_d.month == 10 and val_d.day == 3:
        return INTROS[18]

    # Valentine\'s Day (Valentinstag)
    if val_d.month == 2 and val_d.day == 14:
        return INTROS[19]

    # New Year (Neujahr)
    if val_d.month == 1 and val_d.day == 1:
        return INTROS[20]

    # New Year\'s Eve (Silvester)
    if val_d.month == 12 and val_d.day == 31:
        return INTROS[21]

    # Christmas (Weihnachten)
    if val_d.month == 12 and val_d.day == 24:
        return INTROS[22]

    # playing after 8pm (Spielen nach 20 Uhr)
    if val_dt.hour >= 20:
        return INTROS[23]

    # playing before 9am (Spielen vor 9 Uhr)
    if val_dt.hour <= 9:
        return INTROS[24]

    # playing before 4am (Spielen vor 4 Uhr)
    if val_dt.hour <= 4:
        return INTROS[25]


def extend_parser(parser: argparse.ArgumentParser):
    mutually_exclusive_group = parser.add_mutually_exclusive_group()
    mutually_exclusive_group.add_argument(
        '-a', '--MothersDay',
        action='store_const',
        const=INTROS[0],
        dest='intro',
        help='Mother\'s Day (Muttertag)'
    )
    mutually_exclusive_group.add_argument(
        '-b', '--FathersDay',
        action='store_const',
        const=INTROS[1],
        dest='intro',
        help='Fathe\'s Day (Vatertag)'
    )
    mutually_exclusive_group.add_argument(
        '-c', '--1Advent',
        action='store_const',
        const=INTROS[2],
        dest='intro',
        help='1. Advent'
    )
    mutually_exclusive_group.add_argument(
        '-d', '--2Advent',
        action='store_const',
        const=INTROS[3],
        dest='intro',
        help='2. Advent'
    )
    mutually_exclusive_group.add_argument(
        '-e', '--3Advent',
        action='store_const',
        const=INTROS[4],
        dest='intro',
        help='3. Advent'
    )
    mutually_exclusive_group.add_argument(
        '-f', '--4Advent',
        action='store_const',
        const=INTROS[5],
        dest='intro',
        help='4. Advent'
    )
    mutually_exclusive_group.add_argument(
        '-g', '--EasterSunday',
        action='store_const',
        const=INTROS[6],
        dest='intro',
        help='Easter Sunday (Ostersonntag)'
    )
    mutually_exclusive_group.add_argument(
        '-h', '--EasterMonday',
        action='store_const',
        const=INTROS[7],
        dest='intro',
        help='Easter Monday (Ostermontag)'
    )
    mutually_exclusive_group.add_argument(
        '-i', '--AllSaintsDay',
        action='store_const',
        const=INTROS[8],
        dest='intro',
        help='All Saints\' Day (Allerheiligen)'
    )
    mutually_exclusive_group.add_argument(
        '-j', '--CarnivalMonday',
        action='store_const',
        const=INTROS[9],
        dest='intro',
        help='Carnival Monday (Rosenmontag)'
    )
    mutually_exclusive_group.add_argument(
        '-k', '--ShroveTuesday',
        action='store_const',
        const=INTROS[10],
        dest='intro',
        help='Shrove Tuesday (Fastnachtsdienstag)'
    )
    mutually_exclusive_group.add_argument(
        '-l', '--AshWednesday',
        action='store_const',
        const=INTROS[11],
        dest='intro',
        help='Ash Wednesday (Aschermittwoch)'
    )
    mutually_exclusive_group.add_argument(
        '-m', '--1April',
        action='store_const',
        const=INTROS[12],
        dest='intro',
        help='April Fool\'s Day (1. April)'
    )
    mutually_exclusive_group.add_argument(
        '-n', '--BoxingDay',
        action='store_const',
        const=INTROS[13],
        dest='intro',
        help='Boxing Day (2. Weihnachtsfeiertag)'
    )
    mutually_exclusive_group.add_argument(
        '-o', '--Carnivalbegin',
        action='store_const',
        const=INTROS[14],
        dest='intro',
        help='Carnival begin (Faschingsanfang)'
    )
    mutually_exclusive_group.add_argument(
        '-p', '--LabourDay',
        action='store_const',
        const=INTROS[15],
        dest='intro',
        help='Labour Day (Tag der Arbeit)'
    )
    mutually_exclusive_group.add_argument(
        '-q', '--Epiphany',
        action='store_const',
        const=INTROS[16],
        dest='intro',
        help='Epiphany (Heilige 3 Könige)'
    )
    mutually_exclusive_group.add_argument(
        '-r', '--Nikolaus',
        action='store_const',
        const=INTROS[17],
        dest='intro',
        help='Nikolaus'
    )
    mutually_exclusive_group.add_argument(
        '-s', '--GermanUnityDay',
        action='store_const',
        const=INTROS[18],
        dest='intro',
        help='German Unity Day (Tag der deutschen Einheit)'
    )
    mutually_exclusive_group.add_argument(
        '-t', '--ValentinesDay',
        action='store_const',
        const=INTROS[19],
        dest='intro',
        help='Valentine\'s Day (Valentinstag)'
    )
    mutually_exclusive_group.add_argument(
        '-u', '--NewYear',
        action='store_const',
        const=INTROS[20],
        dest='intro',
        help='New Year (Neujahr)'
    )
    mutually_exclusive_group.add_argument(
        '-v', '--NewYearsEve',
        action='store_const',
        const=INTROS[21],
        dest='intro',
        help='New Year\'s Eve (Silvester)'
    )
    mutually_exclusive_group.add_argument(
        '-w', '--Christmas',
        action='store_const',
        const=INTROS[22],
        dest='intro',
        help='Christmas (Weihnachten)'
    )
    mutually_exclusive_group.add_argument(
        '-x', '--after8pm',
        action='store_const',
        const=INTROS[23],
        dest='intro',
        help='playing after 8pm (Spielen nach 20 Uhr)'
    )
    mutually_exclusive_group.add_argument(
        '-y', '--before9am',
        action='store_const',
        const=INTROS[24],
        dest='intro',
        help='playing before 9am (Spielen vor 9 Uhr)'
    )
    mutually_exclusive_group.add_argument(
        '-z', '--before4m',
        action='store_const',
        const=INTROS[25],
        dest='intro',
        help='playing before 4am (Spielen vor 4 Uhr)'
    )
    mutually_exclusive_group.add_argument(
        '--original',
        action='store_const',
        const='original',
        dest='intro',
        help='insert the original file'
    )
    mutually_exclusive_group.add_argument(
        '--random',
        action='store_const',
        const=choice(INTROS),
        dest='intro',
        help='set a random intro'
    )
    mutually_exclusive_group.add_argument(
        '--today',
        action='store_const',
        const=set_intro_for_today(),
        dest='intro',
        help='get the intro for the current date and time.'
    )
