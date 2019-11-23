# Jupyter notebook cleanup

Working with PyCharm and your Jupyter notebooks becoming quite heavy and slow down your system? This project contains
 some tools to cleanup you Jupyter notebooks.

## Usage

You may want to remove the output of all cells since loading the notebook takes ages. 

Load a jupyter notebook 

```python
import jpcleanup as jpc

path, content = jpc.load('test-notebook') # or with .ipynb
```

reset the output of all cells

```
content = jpc.clear_field(content)
```

and write the result back to either the same file
```
jpc.save(content, path) 
```
or a new file

```python
jpc.save(content, 'test-result') # or with .ipynb
```

## Installation

Either clone this project with

```bash
git clone https://github.com/larsklitzke/jp-cleanup
```

to extend the functionality of the project or, since the the project is hosted on PyPi, install it with

```bash
pip install jp-cleanup
```

## License

Copyright (C) 2019  Lars Klitzke, Lars.Klitzke@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.