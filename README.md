# Magyar posta tracker tool - Unofficial
Unofficial Magyar Posta tracker tool, loosely based on https://github.com/dnet/mptr.py

## CLI Usage

Simple mode:
```console
foo@bar:~$ python postatracker.py RV123456789CN
Wed Aug  7 18:04:29 2019	Budapest - 1 posta	Sikeres kézbesítés
```

Verbose mode:
```console
foo@bar:~$ python postatracker.py -v RL987654321
Wed Dec 11 19:51:37 2019	Budapest - 1 posta	Sikeres kézbesítés
Mon Dec  9 17:12:33 2019	Budapest - 1 posta	Postán átvehető
Mon Dec  9 10:37:27 2019	Budapest - 1 posta	Sikertelen kézbesítés (értesítő bedobva)
Mon Dec  9 07:36:51 2019	Budapest - 1 posta	A küldemény a kézbesítőnél van
Thu Dec  5 19:38:53 2019	Országos Logisztikai Központ	Küldemény felvéve
```

Useful error message:
```console
foo@bar:~$ python postatracker.py RV111111111CN
The given tracking number does not exist.
```


## Dependencies
- Python (tested with 2.7.17 & 3.7.5)
- requests
- pyjq
- json
- time
- argparse
