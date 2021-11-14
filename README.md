<h1>Datashredder</h1>
<img src="https://github.com/awesomelewis2007/Datashredder/blob/main/Logos/logo_dark.png?raw=true" width="150"></img>

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/awesomelewis2007/Datashredder)
[![GitHub license](https://badgen.net/github/license/awesomelewis2007/Datashredder)](https://github.com/awesomelewis2007/Datashredder/blob/master/LICENSE)
[![Github tag](https://badgen.net/github/tag/awesomelewis2007/Datashredder)](https://github.com/awesomelewis2007/Datashredder/tags/)
[![C](https://img.shields.io/badge/--1177AA?logo=c&logoColor=FFFFFF)]()
[![Python](https://img.shields.io/badge/--1177AA?logo=python&logoColor=FFFFFF)]()



Datashredder is a simple data corruption engine written in python. You can corrupt anything text, images and video.


You can choose the chance of corruption e.g I have a chance of 100 therefore there is a 1 in 100 chance of the next piece of data to be corrupted this allows you to control how much corruption you want.

You can also choose to have a random piece of corruption data or random
e.g
Corruption data is FF

Not Corrupted: 30 32 35 53 f0 72

Corrupted: 30 **FF** 35 53 **FF** 72

A random corruption would choose a random corruption data each iteration
## Installing
You can install datashredder using pip
`pip install Datashredder`

[Pypi Project link](https://pypi.org/project/Datashredder/)

## Privacy
![](https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Privacy.png)
## Examples
### Cats
Each image has a corruption data of `00`

There is `206824` iterations on this image
#### Not corrupted image
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Test%20images/cat.jpg" width="200"></img>
#### Corrupted images
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_39_corruptions.jpg" width="150"></img>
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_133_corruptions.jpg" width="150"></img>
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_200_corruptions.jpg" width="150"></img>
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_432_corruptions.jpg" width="150"></img>
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_1020_corruptions.jpg" width="150"></img>
<img src="https://raw.githubusercontent.com/awesomelewis2007/Datashredder/main/Documentation/Corrupted%20images/Cat_2069_corruptions.jpg" width="150"></img>

| Image # | Chance | Corruptions |
|---------|--------|-------------|
| 1       | 2000   | 39          |
| 2       | 1500   | 133         |
| 3       | 1000   | 200         |
| 4       | 500    | 432         |
| 5       | 200    | 1020        |
| 6       | 100    | 2069        |
