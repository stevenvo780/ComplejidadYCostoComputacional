import time
import matplotlib.pyplot as plt
import numpy as np
from importlib import import_module
import subprocess
from tkinter import filedialog
import tkinter as tk

# List of algorithms to evaluate, ordered by complexity
COMPLEXITIES = [
    'constant',
    'logarithmic',
    'linear',
    'linearithmic',
    'quadratic',
    'cubic',
    'exponential',
    'factorial'
]

def measure_time(func, n, repetitions=3):
    """Measures the average execution time of a function"""
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        func(n)
        times.append(time.perf_counter() - start)
    return np.mean(times)

def open_image(image_path):
    """Opens the image with the system's default viewer"""
    subprocess.call(('xdg-open', image_path))

def get_pictures_dir():
    """Gets the system's pictures directory path"""
    pictures_dir = os.path.expanduser('~/Pictures')
    if not os.path.exists(pictures_dir):
        pictures_dir = os.path.expanduser('~/Pictures')
    return pictures_dir

def main():
    # Generate input values in logarithmic scale
    n_values = np.logspace(0, 4, num=15, dtype=int)
    results = {}
    
    # Execute and measure each algorithm
    for complexity in COMPLEXITIES:
        print(f"Measuring complexity: {complexity}")
        module = import_module(f'complexities.{complexity}')
        times = []
        
        # Maximum n limits for costly algorithms
        n_max = {
            'factorial': 8,      # Low limit for O(n!)
            'exponential': 12,   # Limit for O(2^n)
            'cubic': 50,         # Limit for O(n³)
            'quadratic': 200     # Limit for O(n²)
        }.get(complexity, max(n_values))
            
        for n in n_values:
            if n <= n_max:
                times.append(measure_time(module.compute, n))
            else:
                times.append(None)
        results[complexity] = times

    # Graph configuration and generation
    plt.figure(figsize=(12, 8))
    for complexity, times in results.items():
        valid_times = [(n, t) for n, t in zip(n_values, times) if t is not None]
        if valid_times:
            x, y = zip(*valid_times)
            plt.plot(x, y, marker='o', label=f'O({complexity})')

    # Configure logarithmic scale graph
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Computational Complexities')
    plt.grid(True)
    plt.legend()
    
    # Save and display graph
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        initialfile='computational_complexity.png',
        initialdir='~/',
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'), ('All files', '*.*')]
    )
    
    if file_path:
        plt.savefig(file_path)
        print(f"Graph saved at: {file_path}")
        subprocess.call(('xdg-open', file_path))

if __name__ == "__main__":
    main()