# 🔐 SBoxCryptoAnalysis

Analiza kryptograficzna 8×8 S-boxów używanych w szyfrach blokowych.  
Projekt pozwala ocenić jakość S-boxa na podstawie jego właściwości logicznych i różnicowych:

- ✅ Ekstrakcja funkcji boolowskich z bajtów wyjściowych
- ⚖️ Test balansu bitów (równa liczba 0 i 1)
- 🔍 Obliczenie nieliniowości (odległość od funkcji liniowych)
- 🌀 Sprawdzenie SAC (Strict Avalanche Criterion)
- ⚡ Profil XOR do analizy różnicowej

## 📁 Struktura projektu

SBoxCryptoAnalysis  
├── Sbox.py – analiza funkcji boolowskich (balans, nieliniowość, SAC)  
├── xor_profile.py – generowanie profilu XOR S-boxa  
├── sbox_analysis.txt – analiza przykładowego S-boxa  
└── README.md

## 🚀 Uruchomienie

1. Zainstaluj wymagane biblioteki:
pip install numpy

2. Umieść plik `.SBX` z danymi S-boxa w katalogu projektu.

3. W pliku `Sbox.py` zaktualizuj ścieżkę do pliku `.SBX`:
file_path = "ścieżka/do/pliku.SBX"

4. Uruchom analizę właściwości logicznych:
python Sbox.py

5. Uruchom analizę różnicową:
python xor_profile.py

## ✅ Funkcjonalności

**Sbox.py**
- Ekstrakcja 8 funkcji boolowskich z wyjść S-boxa
- Sprawdzenie balansu bitów (czy liczba 1 = liczbie 0)
- Obliczenie nieliniowości (minimalna odległość Hamminga od funkcji liniowych)
- Test SAC – analiza wpływu zmiany jednego bitu wejścia na wyjście
- Zapis wyników do pliku `sbox_analysis.txt`

**xor_profile.py**
- Generowanie profilu różnicowego (XOR Profile)
- Zliczanie wystąpień dla każdej pary różnica-wejściowa → różnica-wyjściowa

## 🔧 Technologie

- Python 3.8+
- numpy – szybkie operacje wektorowe
- Pliki wejściowe w formacie `.SBX` (binarnym)

## 📌 Autor

- Konrad Gajdziński