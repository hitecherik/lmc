# Little Man Computer

A python interpreter for the [Little Man Computer](https://en.wikipedia.org/wiki/Little_man_computer). Created as an experiment and currently works with all the commands listed [here](http://peterhigginson.co.uk/LMC/help.html), except:

- BRA
- BRZ
- BRP
- OTC

When run, these currently don't generate errors/warnings - they're ignored instead. These commands will be added in later versions.

## Instructions

Just type in your assembly code into the `lmc.txt` file, with the labels, operators and operands *seperated by spaces only*. Then just run the `main.py` file from the console.

## Licence

**Copyright (c) 2015 Alexander Nielsen**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.