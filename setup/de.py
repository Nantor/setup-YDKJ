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

    # Fathe\'s Day (Vatertag)
    if spencer_easter_formula(val_d.year) + timedelta(days=39) is val_d:
        return INTROS[1]

    # 1. Advent
    if first_advent(val_d.year) is val_d:
        return INTROS[2]

    # 2. Advent
    if first_advent(val_d.year) + timedelta(weeks=1) is val_d:
        return INTROS[3]

    # 3. Advent
    if first_advent(val_d.year) + timedelta(weeks=2) is val_d:
        return INTROS[4]

    # 4. Advent
    if first_advent(val_d.year) + timedelta(weeks=3) is val_d:
        return INTROS[5]

    # Easter Sunday (Ostersonntag)
    if spencer_easter_formula(val_d.year) is val_d:
        return INTROS[6]

    # Easter Monday (Ostermontag)
    if spencer_easter_formula(val_d.year) + timedelta(days=1) is val_d:
        return INTROS[7]

    # All Saints\' Day (Allerheiligen)
    if val_d.month == 11 and val_d.day == 1:
        return INTROS[8]

    # Carnival Monday (Rosenmontag)
    if spencer_easter_formula(val_d.year) - timedelta(days=48) is val_d:
        return INTROS[9]

    # Shrove Tuesday (Fastnachtsdienstag)
    if spencer_easter_formula(val_d.year) - timedelta(days=47) is val_d:
        return INTROS[10]

    # Ash Wednesday (Aschermittwoch)
    if spencer_easter_formula(val_d.year) - timedelta(days=46) is val_d:
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
    parser.add_argument(
        '-a', '--MothersDay',
        action='append_const',
        const=INTROS[0],
        dest='intro',
        help='Mother\'s Day (Muttertag)'
    )
    parser.add_argument(
        '-b', '--FathersDay',
        action='append_const',
        const=INTROS[1],
        dest='intro',
        help='Fathe\'s Day (Vatertag)'
    )
    parser.add_argument(
        '-c', '--1Advent',
        action='append_const',
        const=INTROS[2],
        dest='intro',
        help='1. Advent'
    )
    parser.add_argument(
        '-d', '--2Advent',
        action='append_const',
        const=INTROS[3],
        dest='intro',
        help='2. Advent'
    )
    parser.add_argument(
        '-e', '--3Advent',
        action='append_const',
        const=INTROS[4],
        dest='intro',
        help='3. Advent'
    )
    parser.add_argument(
        '-f', '--4Advent',
        action='append_const',
        const=INTROS[5],
        dest='intro',
        help='4. Advent'
    )
    parser.add_argument(
        '-g', '--EasterSunday',
        action='append_const',
        const=INTROS[6],
        dest='intro',
        help='Easter Sunday (Ostersonntag)'
    )
    parser.add_argument(
        '-h', '--EasterMonday',
        action='append_const',
        const=INTROS[7],
        dest='intro',
        help='Easter Monday (Ostermontag)'
    )
    parser.add_argument(
        '-i', '--AllSaintsDay',
        action='append_const',
        const=INTROS[8],
        dest='intro',
        help='All Saints\' Day (Allerheiligen)'
    )
    parser.add_argument(
        '-j', '--CarnivalMonday',
        action='append_const',
        const=INTROS[9],
        dest='intro',
        help='Carnival Monday (Rosenmontag)'
    )
    parser.add_argument(
        '-k', '--ShroveTuesday',
        action='append_const',
        const=INTROS[10],
        dest='intro',
        help='Shrove Tuesday (Fastnachtsdienstag)'
    )
    parser.add_argument(
        '-l', '--AshWednesday',
        action='append_const',
        const=INTROS[11],
        dest='intro',
        help='Ash Wednesday (Aschermittwoch)'
    )
    parser.add_argument(
        '-m', '--1April',
        action='append_const',
        const=INTROS[12],
        dest='intro',
        help='April Fool\'s Day (1. April)'
    )
    parser.add_argument(
        '-n', '--BoxingDay',
        action='append_const',
        const=INTROS[13],
        dest='intro',
        help='Boxing Day (2. Weihnachtsfeiertag)'
    )
    parser.add_argument(
        '-o', '--Carnivalbegin',
        action='append_const',
        const=INTROS[14],
        dest='intro',
        help='Carnival begin (Faschingsanfang)'
    )
    parser.add_argument(
        '-p', '--LabourDay',
        action='append_const',
        const=INTROS[15],
        dest='intro',
        help='Labour Day (Tag der Arbeit)'
    )
    parser.add_argument(
        '-q', '--Epiphany',
        action='append_const',
        const=INTROS[16],
        dest='intro',
        help='Epiphany (Heilige 3 Könige)'
    )
    parser.add_argument(
        '-r', '--Nikolaus',
        action='append_const',
        const=INTROS[17],
        dest='intro',
        help='Nikolaus'
    )
    parser.add_argument(
        '-s', '--GermanUnityDay',
        action='append_const',
        const=INTROS[18],
        dest='intro',
        help='German Unity Day (Tag der deutschen Einheit)'
    )
    parser.add_argument(
        '-t', '--ValentinesDay',
        action='append_const',
        const=INTROS[19],
        dest='intro',
        help='Valentine\'s Day (Valentinstag)'
    )
    parser.add_argument(
        '-u', '--NewYear',
        action='append_const',
        const=INTROS[20],
        dest='intro',
        help='New Year (Neujahr)'
    )
    parser.add_argument(
        '-v', '--NewYearsEve',
        action='append_const',
        const=INTROS[21],
        dest='intro',
        help='New Year\'s Eve (Silvester)'
    )
    parser.add_argument(
        '-w', '--Christmas',
        action='append_const',
        const=INTROS[22],
        dest='intro',
        help='Christmas (Weihnachten)'
    )
    parser.add_argument(
        '-x', '--after8pm',
        action='append_const',
        const=INTROS[23],
        dest='intro',
        help='playing after 8pm (Spielen nach 20 Uhr)'
    )
    parser.add_argument(
        '-y', '--before9am',
        action='append_const',
        const=INTROS[24],
        dest='intro',
        help='playing before 9am (Spielen vor 9 Uhr)'
    )
    parser.add_argument(
        '-z', '--before4m',
        action='append_const',
        const=INTROS[25],
        dest='intro',
        help='playing before 4am (Spielen vor 4 Uhr)'
    )
    parser.add_argument(
        '--original',
        action='append_const',
        const='original',
        dest='intro',
        help='insert the original file'
    )
    parser.add_argument(
        '--random',
        action='append_const',
        const=[choice(INTROS)],
        dest='intro',
        help='set a random intro'
    )
    parser.add_argument(
        '--today',
        action='append_const',
        const=set_intro_for_today(),
        dest='intro',
        help='get the intro for the current date and time.'
    )
