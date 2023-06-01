# EM100-Reader
Application for converting Extech EM100 data files to CSV and Python library for reading them

## Requirements:
* Python 3.8
* Pandas
* Numpy

## Installation:
1. Clone this repository
2. Navigate to the repository
3. Install with `pip install .` 

## Usage:
```
extechread [-h] [-r] input output

Convert data from Extech EM100 to csv

positional arguments:
  input            Input .bin file to read
  output           Output CSV file to write

options:
  -h, --help       show this help message and exit
  -r, --recursive  NYI---Supply a directory of bin files instead of just one.
                   note that if you export more than once to the same
                   directory your CSV file will contain duplicate records
```

## Documentation:
`from em100 import *` gives you access to a couple of functions. Perhaps most useful are the `read_to_array` and `read_to_pandas` functions, which you can call with the path to a bin file to read. These will return a list or a DataFrame, respectively, containing all the records from the file.