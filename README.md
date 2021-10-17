<h1>Datashredder</h1>
<img src="https://github.com/awesomelewis2007/Datashredder/blob/main/Logos/logo_dark.png?raw=true" width="150"></img>

Datashredder is a simple data corruption engine written in python. You can corrupt anything text, images and video.


You can chose the chance of corruption e.g i have a chance of 100 therfore there is a 1 in 100 chance of the next peice of data to be corrupted this allows you to controll how much corruption you want.

You can also chose to have a random peice of corruption data or random
e.g
Corruption data is FF

Not Corrupted: 30 32 35 53 f0 72

Corrupted: 30 **FF** 35 53 **FF** 72

A random corruption would chose a random corruption data each iteration
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
