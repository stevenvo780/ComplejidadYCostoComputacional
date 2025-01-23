import time
import matplotlib.pyplot as plt
import numpy as np
from importlib import import_module

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
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        func(n)
        times.append(time.perf_counter() - start)
    return np.mean(times)

def main():
    # Tamaños de entrada adaptados a cada complejidad
    n_values = np.logspace(0, 6, num=20, dtype=int)
    results = {}
    
    for complexity in COMPLEXITIES:
        print(f"Midiendo complejidad: {complexity}")
        module = import_module(f'complexities.{complexity}')
        times = []
        
        # Ajustar n_max según la complejidad
        if complexity in ['exponential', 'factorial']:
            n_max = 15
        elif complexity == 'cubic':
            n_max = 100
        else:
            n_max = max(n_values)
            
        for n in n_values:
            if n <= n_max:
                times.append(measure_time(module.compute, n))
            else:
                times.append(None)
        results[complexity] = times

    # Visualización
    plt.figure(figsize=(12, 8))
    for complexity, times in results.items():
        valid_times = [(n, t) for n, t in zip(n_values, times) if t is not None]
        if valid_times:
            x, y = zip(*valid_times)
            plt.plot(x, y, marker='o', label=f'O({complexity})')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Complejidades Computacionales')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()