import random

palavras = ["php", "java", "python", "C#"]

texto = ''.join(palavras)

letras = list(texto)
random.shuffle(letras)
anagrama = ''.join(letras)

print(f"Palavras utilizadas: {palavras}")
print(f"Anagrama: {anagrama}")
