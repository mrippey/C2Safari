
<div align="center">
    <img src="https://github.com/msec1203/C2Safari/blob/master/header.png" width="800px"/>
</div>

![GitHub](https://img.shields.io/github/license/msec1203/c2safari?color=orange)

# C2-Safari Tool

Search queries can be cumbersome to write. This tool seeks to ease some of that burden by providing<br>
a user with a CLI menu of pre-selected queries to search Shodan for possible adversary C2 infrastructure.<br>
Inspiration for this project came from Aaron Stephens presentation [Scan't Touch This](https://github.com/aaronst/talks).
 
## TODO
- [ ] Add unit tests.
- [ ] Get rid of redundant functions in c2safari_queries.py with a class.
- [ ] Option to write output to file.
- [ ] Provide user option to check IP address against GreyNoise API by index number.

## Prerequisites
Python3.9<br>
[Poetry](https://python-poetry.org)

## Getting Started
$ git clone https://github.com/msec1203/c2safari.git<br>
$ cd c2safari/c2safari<br>
$ poetry shell<br>
$ poetry install<br>
$ poetry run 


## Usage
Simply run the script, select a number from the menu and receive the first five results from Shodan. 


## More info on the Shodan queries that inspired this project:
[FireEye Article](https://www.fireeye.com/blog/threat-research/2020/07/scandalous-external-detection-using-network-scan-data-and-automation.html)


## Finally
Michael Rippey - [MyTwitter](https://twitter.com/nahamike01)<br>
This project is licensed under GNU General Public License v3.0. See [LICENSE](https://github.com/msec1203/C2Safari/blob/master/LICENSE)
