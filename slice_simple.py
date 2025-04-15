def slice_simple():
    texto = "Awesome"
    texto = texto.lower()  # Aseguramos que todo esté en minúscula

    # Primeras 3 letras
    primeras_tres = texto[0:3]

    # Tres letras del medio (índices positivos)
    # En "awesome", índice de 'e' (posición 2), 's' (3), 'o' (4) → texto[2:5]
    tres_del_medio = texto[2:5]

    # De la primera a la cuarta letra (0 a 4 incluído = 0:5)
    # De la antepenúltima a la última: texto[-3:] pero con índices positivos → len(texto) = 7 → texto[4:]
    primeras_y_finales = texto[0:5] + texto[4:]

    print(primeras_tres)
    print(tres_del_medio)
    print(primeras_y_finales)
