def check_vowels():
    # Código a implementar utilizando input.
    name = input("Ingrese un nombre:\n").lower()  # Pasamos todo a minúscula para simplificar

    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for vowel in vowels:
        print(f"Contiene {vowel}: {vowel in name}")
