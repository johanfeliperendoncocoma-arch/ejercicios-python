texto = input("Escribe un párrafo: ")
palabras = texto.split()
print("Número de palabras:", len(palabras))
mas_larga = ""
for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra
print("Palabra más larga:", mas_larga)
letras = {}
total_letras = 0
for letra in texto:
    letra = letra.lower()
    if letra.isalpha():
        total_letras += 1
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
print("Número total de letras en el párrafo:", total_letras)
