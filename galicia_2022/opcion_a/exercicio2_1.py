def cifra_v1(texto):
    DESPLAZAMIENTO = 5
    alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z")
    
    cifrado = ""
    for letra in texto:
        indice_cif = (alfabeto.index(letra) + DESPLAZAMIENTO) % len(alfabeto)
        cifrado += alfabeto[indice_cif]
        
    return cifrado

print(cifra_v1("marcex"))
        