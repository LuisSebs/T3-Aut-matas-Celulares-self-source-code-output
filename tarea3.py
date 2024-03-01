if __name__ == "__main__":
    # Programa cuya salida es el codigo fuente del programa
    with open('codigo_fuente.txt', 'w') as salida_codigo_fuente:
        nombre_del_archivo_fuente = __file__ # Este archivo
        with open(f'{nombre_del_archivo_fuente}', 'r') as codigo_fuente:
            str_codigo_fuente = codigo_fuente.read()
            salida_codigo_fuente.write(str_codigo_fuente)
            print(str_codigo_fuente)