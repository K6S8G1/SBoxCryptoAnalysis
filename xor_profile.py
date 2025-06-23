import numpy as np
from itertools import product

# Ścieżka do pliku S-box
file_path = ""


# Wczytywanie S-boxa z pliku binarnego
def read_sbox_file(file_path):
    """Odczytuje plik .SBX i zwraca listę 256 niezerowych bajtów."""
    with open(file_path, "rb") as f:
        sbox_data = f.read()
    return sbox_data[0::2]  # Pobieramy tylko niezerowe bajty

# Generowanie profilu XOR
def get_xor_profile(sbox, num_vars: int = 8):
    xor_matrix = np.zeros((2**num_vars, 2**num_vars), dtype=np.int64)
    for x1 in range(256):
        for x2 in range(256):
            x_diff = x1 ^ x2
            y1 = sbox[x1]
            y2 = sbox[x2]
            y_diff = y1 ^ y2
            xor_matrix[x_diff, y_diff] += 1
    return xor_matrix

# Sortowanie profilu XOR
def sort_xor_matrix_by_counts(xor_matrix):
    xor_dict = {}
    x_diff, y_diff = np.indices(xor_matrix.shape)
    x_diff = x_diff.flatten()
    y_diff = y_diff.flatten()
    counts = xor_matrix.flatten()

    for x, y, count in zip(x_diff, y_diff, counts):
        if x not in xor_dict or xor_dict[x][1] < count:
            xor_dict[x] = [y, count]

    sorted_xor_dict = dict(sorted(xor_dict.items(), key=lambda item: item[1][1], reverse=True))
    return sorted_xor_dict

# Główna część programu
if __name__ == "__main__":
    sbox = read_sbox_file(file_path)
    xor_matrix = get_xor_profile(sbox)
    xor_profile_counts = sort_xor_matrix_by_counts(xor_matrix)

    # Wyświetlenie wyników
    print("Najczęstsze pary różnic wejście-wyjście:")
    for x_diff, (y_diff, count) in xor_profile_counts.items():
        print(f"x_diff: {x_diff:02X}, y_diff: {y_diff:02X}, count: {count}")
