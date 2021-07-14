# RickDate
Python package to display full date as 3 characters. like this: `57e` _(2021-07-14)_

> It just encodes the 3 parts (year, month and day) as base36 strings.
<br> The output is only 3 characters long:- `"Y-M-D"`

Represents the date as a [RickDate][1] string. 

__Use case A:__

I use it to date my timesheets eg: `574.txt`

__Use case B:__

I use it to datestamp file uploads... eg: `574_filename.png`

__Use case C:__

I use it to date script versions... eg: `574_file_scripts.sh`

## Comparison of other systems:

Which column of files is nicer to read?:

| [RickDate][1] NICE | long/non-sortable NOT NICE |
| --- | --- |
574_filename.png | 4_July_2021_filename.png
575_filename.png | 20210705_filename.png
576_filename.png | 06_07_2021_filename.png
584_filename.png | 4_August_2021_filename.png
594_filename.png | 04_September_2021_filename.png
674_filename.png | July_04_2022_filename.png
774_filename.png | 4_July_2022_filename.png
774_filename.png | 2022-07-04_filename.png*


## Examples of different dates
Here are examples of how a [RickDate][1] would changes over time:

| Change of years | year |
| --- | --- |
| 4th of July `2021` | `5`74
| 4th of July `2022` | `6`74
| 4th of June `2023` | `7`74

| Change of months | month |
| --- | --- |
| 4th of `July` 2021 | 5`7`4
| 4th of `Aug` 2021 | 5`8`4
| 4th of `Sept` 2021 | 5`9`4

| Change of days | day |
| --- | --- |
| `4th` of July 2021 | 57`4`
| `5th` of July 2021 | 57`5`
| `6th` of July 2021 | 57`6`

## Usage
```python
import rickdate
print(rickdate())
```
If the current date was the `12th August 2021` then the output should be `"58C"`

## Base36
> "Any number larger than nine gets a letter of the alphabet..."

| part | range |
| --- | --- |
| day (1-31)  | 1,2,3,4,5,....9,A,B,C...T,U,V |
| month(1-12)  | 1,2,3,4,5,6,7,8,9,A,B,C |
| year(eg 2021)  | 1K5,1K6,1K7... last digit repeats every 36 years |


> You can test the number base conversion with this tool:<br>
http://extraconversion.com/base-number/base-36

I have also made a tool in javascript (on [codepen][2]) to convert to and from [RickDate][1]

The results are sortable alphabetically (and by date)

## Limitations
I only use the last digit of the year as I'll be to busy in my flying car in 36 years to care about repeats!

Use the full 3 digit year if you see the use of this being a problem

```python
print(rickdate.withFullYear())
```
The output of this should look like: `"1k579"` for the 9th July 2021

## Build
```python
python3 -m build
```
## Distribute on PyPi
```
python3 -m twine upload --repository testpypi dist/*
```


_last updated: **57E**_

# todo:
- [x] create readme
- [x] output 3 letter rickdate
- [x] submit package to pypi
- [ ] output full year
- [ ] accept date object input
- [ ] accept iso3601 dates string input


[1]: http://www.yak.net/kablooey/RickDate.html
[2]: https://codepen.io/emrys/full/MQwpgN