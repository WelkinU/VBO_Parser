# VBO Parser

This is a quick Python parser for Racelogic .vbo files produced via DGPS VBOX.

## Example Usage

```Python
from vbo_parser import VBO_Parser

vbo = VBO_Parser('path/to/file.vbo')

# Get VBO data as a Pandas dataframe
pandas_dataframe = vbo.data

# Get dict containing channel variables and their associated units
channel_units_dict = vbo.channel_units_map

# Get string containing file comments
comments = vbo.comments
```

## Environment

Make sure to have Python >= 3.6 and Pandas installed.

## Example VBO data

https://github.com/Lumbrer/Racelogic-VBO-Converter/blob/master/Example_File.VBO