# Turing Machine Simulator
A basic implementation of a Turing machine simulator in Python

## What it does

This project is a simple simulator for single-tape Turing machines. It allows you to define a machine with a set of states and transitions, and then execute it step-by-step on a given input string. The simulator provides basic input/output operations and can be used as a tool for experimenting with Turing machine concepts.

## Install

You can install the simulator using pip:

```bash
pip install git+https://github.com/your-username/turing-machine-simulator.git
```

Alternatively, you can clone the repository and run the simulator directly:

```bash
git clone https://github.com/your-username/turing-machine-simulator.git
cd turing-machine-simulator
python -m simulator
```

## Usage

To use the simulator, simply run the `python -m simulator` command and follow the prompts. You can define a machine by specifying its states, transitions, and initial state. Then, you can execute the machine on a given input string and see the step-by-step execution.

## Build from source

To build the simulator from source, simply clone the repository and run the `python setup.py install` command.

## Tests

The simulator has a basic test suite that can be run using the `python -m unittest test_suite` command.

## Project structure

The project consists of the following files:

* `simulator.py`: the main simulator module
* `machine.py`: a module for defining Turing machines
* `test_suite.py`: a test suite for the simulator

## License

Copyright (c) 2026 SamyAlderson

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