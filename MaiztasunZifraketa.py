import collections

criptograma = "JIYQ WQIEtYLP YtXLLW OPLP! CWXYM SPMQPLtP YEYQWtP CPOX PLZP SBPJPQX bPBQXWYtPQX bPtYPM. JYLYM bPW, XLPWM HYMCY PEQX PtYLPtJYM CP HPWJQWbYB WQIEtYLP; tRPBXPQ YtP tRPBXPQ, YtP «PISP, HPWJQWbYB!» XWFIPQ WJPM CWLP MPOIEW WbWBbWCY XEXPM. QPBY MPOIEWP YLY HPCP YJ CP BYFYM bYJPWM OPtPJQPtEIP, bPWMP, XLPWMCWQ YLY, JYMbPWt YZPQIZY OPJtYQ SPEPYLPM bWJQPLLP YZPM CWXtY HPWJQWbYBW, SPLtY FPLtJYP bPWZYMtJYM CWYM QXMSPWMWP bPQPLLPLW."

# Contar y mostrar la frecuencia de las letras en el texto
frecuencias = collections.Counter(c for c in criptograma if c.isalpha())

print("Frecuencia de letras en el criptograma (mayor a menor):")
for letra, cantidad in frecuencias.most_common():
    print(f"{letra}: {cantidad} veces")

print("\n--- MODO INTERACTIVO DE REEMPLAZO ---")

# Diccionario para almacenar sustituciones
sustituciones = {}

while True:
    # Generar el texto actual aplicando las sustituciones guardadas
    texto_actual = "".join(sustituciones.get(c, c) for c in criptograma)
    print("\nTexto actual:")
    print(texto_actual)

    entrada = input("\nIndica la letra cifrada y su reemplazo real separados por espacio (ej. 'P a'), o escribe 'salir': ").strip()

    if entrada.lower() == 'salir':
        break

    partes = entrada.split()
    if len(partes) == 2:
        letra_cifrada = partes[0]
        letra_real = partes[1].lower() # Forzamos minúscula para diferenciar qué hemos descifrado

        # Guardamos el reemplazo
        sustituciones[letra_cifrada] = letra_real
    else:
        print("Formato incorrecto. Por favor, usa una letra cifrada, un espacio, y la letra real.")
