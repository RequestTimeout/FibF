# <div align="center">FibF</div>
**Fibonacci, but faster.**

For more information, click [here](HowTo.md).

A small Fibonacci number generator with two calculation methods:
* **Normal** — calculates Fibonacci numbers sequentially.
* **Fast** — uses the fast-doubling algorithm for faster calculation of large Fibonacci numbers.
## Features
* Fast Fibonacci generation
* Normal and fast calculation modes
* Optional `output.txt` generation
* Execution time measurement
* Supports extremely large Fibonacci numbers
* No external Python dependencies
## Usage
```text
python fibf.py
```
Choose whether to generate `output.txt`, enter the Fibonacci index, then select `normal` or `fast`.

Example:
```text
Generate output.txt? (1 or 0): 0
Enter a number: 1000000
Normal or fast: fast
The process took 00:00:00.130 seconds.
```
## Requirements
* Python 3.x
## License
— All Rights Reserved [Request Timeout](https://github.com/RequestTimeout)

[LICENSE](LICENSE.md)
