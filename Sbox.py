import numpy as np
from itertools import product

def read_sbox_file(file_path):
    """Odczytuje plik .SBX i zwraca listę 256 niezerowych bajtów."""
    with open(file_path, "rb") as f:
        sbox_data = f.read()
    return sbox_data[0::2]  # Pobieramy tylko niezerowe bajty

def extract_boolean_functions(nonzero_bytes):
    """Przekształca bajty na 8 funkcji logicznych (tablice prawdy)."""
    binary_matrix = np.array([[int(b) >> i & 1 for i in range(8)] for b in nonzero_bytes], dtype=int)
    return binary_matrix.T  # Transpozycja macierzy, aby każdy wiersz był funkcją

def check_balance(boolean_functions):
    """Sprawdza balans każdej funkcji (czy ma po 128 zer i jedynek)."""
    return [np.sum(f) == 128 for f in boolean_functions]

def generate_linear_functions():
    """Generuje 512 funkcji liniowych dla 8-bitowych wejść."""
    input_space = np.array(list(product([0, 1], repeat=8)))
    linear_functions = []
    
    for coeffs in product([0, 1], repeat=8):
        for constant in [0, 1]:
            linear_func = (input_space @ np.array(coeffs) % 2) ^ constant
            linear_functions.append(linear_func)
    
    return np.array(linear_functions)

def hamming_distance(f, linear_functions):
    """Oblicza minimalną odległość Hamminga między funkcją a funkcjami liniowymi."""
    return np.min(np.sum(f != linear_functions, axis=1))

def check_sac(boolean_functions):
    """Oblicza średnie prawdopodobieństwo zmiany wyjścia po zmianie pojedynczego bitu."""
    input_space = np.array(list(product([0, 1], repeat=8)))
    sac_probabilities = []
    
    for f in boolean_functions:
        probabilities = []
        for i in range(8):
            flipped_inputs = input_space.copy()
            flipped_inputs[:, i] ^= 1  # Zmieniamy jeden bit
            
            original_outputs = f[np.sum(input_space * (2 ** np.arange(7, -1, -1)), axis=1)]
            flipped_outputs = f[np.sum(flipped_inputs * (2 ** np.arange(7, -1, -1)), axis=1)]
            
            probability = np.sum(flipped_outputs != original_outputs) / len(original_outputs)
            probabilities.append(probability)
        sac_probabilities.append(np.mean(probabilities))
    
    return sac_probabilities

if __name__ == "__main__":

    
    file_path = ""

    nonzero_bytes = read_sbox_file(file_path)
    boolean_functions = extract_boolean_functions(nonzero_bytes)
    balance_results = check_balance(boolean_functions)
    linear_functions = generate_linear_functions()
    nonlinearity = [hamming_distance(f, linear_functions) for f in boolean_functions]
    sac_probabilities = check_sac(boolean_functions)
    
    with open("sbox_analysis.txt", "w", encoding="utf-8") as f:
        f.write("Analiza S-boxa\n")
        f.write("------------------\n")
        for i, (balanced, nl, sac_prob) in enumerate(zip(balance_results, nonlinearity, sac_probabilities)):
            f.write(f"F{i+1}: {'Zbalansowana' if balanced else 'Niezbalansowana'}, ")
            f.write(f"Nieliniowość: {nl}, Średnie SAC: {sac_prob:.2f}\n")
        f.write(f"\nWygenerowano {linear_functions.shape[0]} funkcji liniowych dla 8-bitowych wejść.\n")
        f.write(f"Test SAC został przeprowadzony dla każdej funkcji.\n")
    
    print("Analiza zakończona. Wyniki zapisano w sbox_analysis.txt")
