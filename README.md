# Presentation

# Usage

```shell
python Main.py &
tail -f out.log
```

# Result exemple

Results are possible results, not always the same due to the random nature of
evolution.

## Baseline, both strategies mixed
```
          NAME    FORM   TYPE 1    TYPE 2   HP  ATK  DEF  SP.ATK  SP.DEF  SPEED
272    Shuckle   -----      Bug      Rock   20   10  230      10     230      5
142    Blissey   -----   Normal     -----  255   10   10      75     135     55
210     Mewtwo  Mega Y  Psychic     -----  106  150   70     194     120    140
282  Piloswine   -----      Ice    Ground  100  100   80      60      60     50
479     Deoxys   Speed  Psychic     -----   50   95   90      95      90    180
209     Mewtwo  Mega X  Psychic  Fighting  106  190  100     154     100    130
```
## Only type methode used
```
         NAME   FORM  TYPE 1    TYPE 2   HP  ATK  DEF  SP.ATK  SP.DEF  SPEED
233  Togekiss  -----   Fairy    Flying   85   50   95     120     115     80
173    Lapras  -----   Water       Ice  130   85   80      85      95     60
633  Krokorok  -----  Ground      Dark   60   82   45      45      45     74
423   Armaldo  -----    Rock       Bug   75  125  100      70      80     45
2    Venusaur  -----   Grass    Poison   80   82   83     100     100     80
578   Pignite  -----    Fire  Fighting   90   93   55      70      55     55
```
## Only stats methode used
```
        NAME    FORM   TYPE 1    TYPE 2   HP  ATK  DEF  SP.ATK  SP.DEF  SPEED
210   Mewtwo  Mega Y  Psychic     -----  106  150   70     194     120    140
142  Blissey   -----   Normal     -----  255   10   10      75     135     55
479   Deoxys   Speed  Psychic     -----   50   95   90      95      90    180
272  Shuckle   -----      Bug      Rock   20   10  230      10     230      5
77   Kadabra   -----  Psychic     -----   40   35   30     120      70    105
209   Mewtwo  Mega X  Psychic  Fighting  106  190  100     154     100    130
```

# Sources
pokedex remixed from https://gist.github.com/leimd/b3d5df0af2ccd6f4a09c443c96b68176#file-pokedex-csv
