menu = """
🛹🛹
Bienvenidos al conversor de monedas 💰

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: 

"""
def conversor(tipo_moneda, valor_cambio):
    valor = int(input("Digite la cantidad a convertir: "))
    print("los pesos",t1, " equivalen a: ", round(valor/valor_dolar,2), " Dolares")





opcion = int(input(menu))


if opcion == 1:
    valor_dolar = 3400
    t1= "colombianos"
elif opcion == 2:
    valor_dolar = 65
    t1= "argentinos"
elif opcion == 3:
    valor_dolar = 24
    t1= "mexicanos"
else:
    valor_dolar = -1
       

if valor_dolar>0 :
    conversor(t1,valor_dolar)
    
else:
    print("La opción no es válida")