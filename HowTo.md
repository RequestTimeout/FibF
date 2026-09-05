# <div align="center">FibF</div>
## How to download and use FibF
### Installation (Python 3.X required)
First download `fibF.py` from /RequestTimeout/FibF/src/fibF.py

Then place the Python file somewhere accessible, for example:
```text
C:\fibF\fibF.py
```
Then whenever you need a Fibonacci number, open a terminal and run:
```bash
python "C:\fibF\fibF.py"
```
FibF will ask:
```text
Generate output.txt? (1 or 0):
```
Enter `1` if you want the generated Fibonacci number saved to `output.txt`

or enter `0` if you don't want ANY kind of output.

Then, FibF will ask for the Fibonacci index and calculation method:
```text
Enter a number: <index>
Normal or fast: <method>
```
### Calculation methods
**Normal**

Calculates Fibonacci numbers sequentially.

**Fast**

Uses the fast-doubling algorithm, allowing extremely large Fibonacci numbers to be calculated much faster.

### Output
If `output.txt` was enabled, FibF will generate `output.txt` in the directory that the terminal was opened.

FibF will also display how long the calculation took; for example:
```text
The process took 00:00:00.130 seconds.
```
## Requirements
* Python 3.x
* No external Python dependencies
