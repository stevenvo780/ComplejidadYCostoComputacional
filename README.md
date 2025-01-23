# Computational Complexity Visualization

This project demonstrates different computational complexity classes through practical implementation and visualization. It includes implementations of various time complexity algorithms from O(1) to O(n!) and generates a comparative graph of their execution times.

## Implemented Complexities

- O(1) - Constant Time
- O(log n) - Logarithmic Time
- O(n) - Linear Time
- O(n log n) - Linearithmic Time
- O(n²) - Quadratic Time
- O(n³) - Cubic Time
- O(2ⁿ) - Exponential Time
- O(n!) - Factorial Time

## Requirements

- Python 3.6 or higher
- Required packages:
  - numpy >= 1.20.0
  - matplotlib >= 3.4.0

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/complejidadComputacional.git
cd complejidadComputacional
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Execute algorithms of different complexity classes
2. Measure their execution times for various input sizes
3. Generate a logarithmic scale plot comparing their performance

## How it Works

- Each complexity class is implemented in a separate module under the `complexities/` directory
- The main script measures execution time for each algorithm with different input sizes
- Input sizes are adjusted automatically for more complex algorithms (exponential and factorial)
- Results are plotted on a logarithmic scale for clear visualization

## Note

Exponential and factorial complexities are limited to smaller input sizes due to their intensive computational nature. The program automatically adjusts the maximum input size for these algorithms to prevent excessive execution times.
