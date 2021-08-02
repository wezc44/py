

def palindromo(palabra):
    palabra_invertida = palabra[::-1]
    if palabra==palabra_invertida:
        return True
    else:
        return False
    
    
    


def run():
    palabra = input (" Digite la palabra: ").replace(" ","").lower()
    es_palabra_palindromo = palindromo(palabra)
    
    if es_palabra_palindromo :
        print (palabra, " es palindromo")
    else:
        print (palabra, "no es palindromo")
    
    




if __name__ == "__main__":
    run()