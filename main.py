import time
import matplotlib.pyplot as plt
import numpy as np
from importlib import import_module
import subprocess
from tkinter import filedialog
import tkinter as tk

# Lista de algoritmos a evaluar, ordenados por complejidad
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
    """Mide el tiempo promedio de ejecución de una función"""
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        func(n)
        times.append(time.perf_counter() - start)
    return np.mean(times)

def open_image(image_path):
    """Abre la imagen con el visor predeterminado del sistema"""
    subprocess.call(('xdg-open', image_path))

def get_pictures_dir():
    """Obtiene la ruta de la carpeta de imágenes del sistema"""
    pictures_dir = os.path.expanduser('~/Imágenes')  # Para sistemas en español
    if not os.path.exists(pictures_dir):
        pictures_dir = os.path.expanduser('~/Pictures')  # Para sistemas en inglés
    return pictures_dir

def main():
    # Genera valores de entrada en escala logarítmica
    n_values = np.logspace(0, 4, num=15, dtype=int)
    results = {}
    
    # Ejecuta y mide cada algoritmo
    for complexity in COMPLEXITIES:
        print(f"Midiendo complejidad: {complexity}")
        module = import_module(f'complexities.{complexity}')
        times = []
        
        # Límites máximos de n para algoritmos costosos
        n_max = {
            'factorial': 8,      # Límite bajo para O(n!)
            'exponential': 12,   # Límite para O(2^n)
            'cubic': 50,         # Límite para O(n³)
            'quadratic': 200     # Límite para O(n²)
        }.get(complexity, max(n_values))
            
        for n in n_values:
            if n <= n_max:
                times.append(measure_time(module.compute, n))
            else:
                times.append(None)
        results[complexity] = times

    # Configuración y generación del gráfico
    plt.figure(figsize=(12, 8))
    for complexity, times in results.items():
        valid_times = [(n, t) for n, t in zip(n_values, times) if t is not None]
        if valid_times:
            x, y = zip(*valid_times)
            plt.plot(x, y, marker='o', label=f'O({complexity})')

    # Configuración del gráfico en escala logarítmica
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Complejidades Computacionales')
    plt.grid(True)
    plt.legend()
    
    # Guardar y mostrar el gráfico
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        initialfile='complejidad_computacional.png',
        initialdir='~/',
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'), ('All files', '*.*')]
    )
    
    if file_path:
        plt.savefig(file_path)
        print(f"Gráfico guardado en: {file_path}")
        subprocess.call(('xdg-open', file_path))

if __name__ == "__main__":
    main()