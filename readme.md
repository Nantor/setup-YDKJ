# Setup your "You don't know Jack" (WIP)

The goal with this python script ist to setup and customise the game "You don't know Jack" install under RetroPi.

The following Versions _will_/are implemented:

- German

## Usage

### General

```bash
usage: YDKJ-setup.py [-h] [--resetHighscore] {de} ... dir

Setup your "You don't know Jack" game.

positional arguments:
  {de}              Manipulation of the localized intros at the start of the game.
    de              Options to set intors for the locale de
  dir               directory of the YDKJ game

optional arguments:
  -h, --help        show this help message and exit
  --resetHighscore  resetting the highscore list
```

### Options for german local

```bash
usage: YDKJ-setup.py de [--help] [-a] [-b] [-c] [-d] [-e] [-f] [-g] [-h] [-i] [-j] [-k] [-l] [-m] [-n] [-o] [-p] [-q] [-r] [-s] [-t] [-u] [-v] [-w] [-x] [-y] [-z] [--original]
                        [--random] [--today]

optional arguments:
  --help                show this help message and exit
  -a, --MothersDay      Mother's Day (Muttertag)
  -b, --FathersDay      Fathe's Day (Vatertag)
  -c, --1Advent         1. Advent
  -d, --2Advent         2. Advent
  -e, --3Advent         3. Advent
  -f, --4Advent         4. Advent
  -g, --EasterSunday    Easter Sunday (Ostersonntag)
  -h, --EasterMonday    Easter Monday (Ostermontag)
  -i, --AllSaintsDay    All Saints' Day (Allerheiligen)
  -j, --CarnivalMonday  Carnival Monday (Rosenmontag)
  -k, --ShroveTuesday   Shrove Tuesday (Fastnachtsdienstag)
  -l, --AshWednesday    Ash Wednesday (Aschermittwoch)
  -m, --1April          April Fool's Day (1. April)
  -n, --BoxingDay       Boxing Day (2. Weihnachtsfeiertag)
  -o, --Carnivalbegin   Carnival begin (Faschingsanfang)
  -p, --LabourDay       Labour Day (Tag der Arbeit)
  -q, --Epiphany        Epiphany (Heilige 3 Könige)
  -r, --Nikolaus        Nikolaus
  -s, --GermanUnityDay  German Unity Day (Tag der deutschen Einheit)
  -t, --ValentinesDay   Valentine's Day (Valentinstag)
  -u, --NewYear         New Year (Neujahr)
  -v, --NewYearsEve     New Year's Eve (Silvester)
  -w, --Christmas       Christmas (Weihnachten)
  -x, --after8pm        playing after 8pm (Spielen nach 20 Uhr)
  -y, --before9am       playing before 9am (Spielen vor 9 Uhr)
  -z, --before4m        playing before 4am (Spielen vor 4 Uhr)
  --original            insert the original file
  --random              set a random intro
  --today               get the intro for the current date and time.
```

## Your version is missing

At the moment I have only access to the versions above.
So if you want, that your version also work, open an issue or an pull request.
I will try my best to get ot work.