# f1stats
**f1stats** is using [Fast-F1](https://github.com/theOehrly/Fast-F1#fast-f1 ) core for race and driver analysys. The [Fast-F1](https://github.com/theOehrly/Fast-F1#fast-f1 ) core is a collection of functions and data objects for accessing
and analyzing F1 timing and telemetry data. 

## Setup

```bash
pip install fastf1
pip install matplotlib
pip install numpy
pip install pandas
```

## Usage
Which two drivers do you want to choose you can write as a **driver1** and **driver2**.

For example, we will choose _Bottas_ and _Hamilton_.
```bash
driver1 = 'BOT' 
driver2 = 'HAM'
```

You can also choose all other drivers.
```bash
D_LOOKUP = [[44, 'HAM', 'Mercedes'], [77, 'BOT', 'Mercedes'],
            [55, 'SAI', 'Ferrari'], [16, 'LEC', 'Ferrari'],
            [33, 'VER', 'Red Bull'], [11, 'PER', 'Red Bull'],
            [3, 'RIC', 'McLaren'], [4, 'NOR', 'McLaren'],
            [5, 'VET', 'Aston Martin'], [18, 'STR', 'Aston Martin'],
            [14, 'ALO', 'Alpine'], [31, 'OCO', 'Alpine'],
            [22, 'TSU', 'AlphaTauri'], [10, 'GAS', 'AlphaTauri'],
            [47, 'MSC', 'Haas F1 Team'], [9, 'MAZ', 'Haas F1 Team'],
            [7, 'RAI', 'Alfa Romeo'], [99, 'GIO', 'Alfa Romeo'],
            [6, 'LAT', 'Williams'], [63, 'RUS', 'Williams']]

```

The Fast-F1 developer recommends using **cache**. From his own [document](https://theoehrly.github.io/Fast-F1/examples/index.html#example-plot): 

> It is not necessary to enable the usage of the cache but it is **highly recommended**. Simply provide the path to some empty folder on **your** system. Using the cache will greatly speed up loading of the data.

```bash
ff1.Cache.enable_cache(r'path/to/folder/for/cache') # replace with your cache directory
```

A fuzzy match is performed to find the most likely event for the provided name (e.g. 'Bahrain').

```bash
race = ff1.get_session(2021, 'Zandvoort', 'R')  # 'R' <- 'FP1', 'FP2', 'FP3', 'Q', 'SQ' or 'R'
# FP1 : Free Practice 1
# FP2 : Free Practice 2
# FP3 : Free Practice 3
# Q   : Qualifying
# SQ  : Sprint Qualifying
# R   : Race

```

> 'SQ' stands for Sprint Qualifying which is only available in the 2021 season. Note that 'FP3' does not exist on these race weekends. 


## Functions
```bash
def track():  # Track layout - Fastest Lap Gear Shift Visualization
def gas(): # Car telemetry data ['RPM', 'Speed', 'Throttle', 'Brake', 'nGear', 'DRS']
def compare():  # Two drivers comparison
def qualifying():  # Fastest lap
```

## Compatibility

Data is applicable for the 2018 to 2021 seasons. Fast-F1 uses data from F1's live timing service.

## Screenshots


## Contributing
Pull requests are welcome. Before PR please open an issue what you would like to change.
Follow [PEP 8 Coding Style guidelines](https://www.python.org/dev/peps/pep-0008/).
