# Jupyter notebook cleanup

Working with PyCharm and your Jupyter notebooks becoming quite heavy and slow down your system? This project contains
 some tools to cleanup you Jupyter notebooks.

## Usage

You may want to remove the output of all cells since loading the notebook takes ages. You can either use jp-cleanup
 on the command line or programmatically. 
 
### Command-line
At first, install jp-cleanup with pip using the version on GitHub

```bash
pip install git+https://github.com/larsklitzke/jp-cleanup.git
```
or on PyPi
```bash
pip install jp-cleanup
```

After installation, you can clear the output fields of a notebook `testing` with
```bash
jp-cleanup --file testing.ipynb --clear
```
with `--clear` being an extra flag to not remove the output of a notebook accidentally. 

To list all available parameters or view the current version, run `jp-cleanup` with the `--help` flag.

```bash
jp-cleanup --help
```

### Python

Instead of running `jp-cleanup` on the command-line, you can also use the package in Python. To remove the outputs of
 a certain jupyter notebook `testing`, load the file 

```python
import jpcleanup as jpc

path, content = jpc.load('testing') # or with .ipynb
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
or

```bash
pip install git+https://github.com/larsklitzke/jp-cleanup.git
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