# Nombre: Mónica Andrea Osorio Muñoz 
# Grupo: 213022_185
# Programa: Ingenieria en Sistemas
# Codigo Fuente: autoria propia
print ("\n" + "=" * 50)
print ("BIENBENIDO AL MENU DEL RESTAURANTE")
print ("=" * 50)
# definicion de la matriz 
menu = [ 
 
    ["BANDEJA PAISA", "plato principal", 17000],
    ["SANCOCHO TRIFASICO","plato principal", 12000],
    ["CHURRASCO", "plato principal", 20000],
    ["ARROZ ATOLLADO", "plato principal", 15000],
    ["SOPA DE PASTA", "plato principal", 9000],
    ["POSTRES", "--", 0],
    ["ARROZ CON LECHE", "postres", 5000],
    ["TORTA DE CHOCOLATE", "postres", 6000],
    ["TORTA DE TRES LECHES", "postres", 7000],
    ["ENSALADA DE ATUN", "ensaladas", 8000],
    ["ENSALADA DE POLLO", "ensaladas", 8000],
    ["ENSALADA VERDE", "ensaladas", 6000],
    ["LIMONADA", "bebidas", 3000],
    ["CAFE AMERICANO", "bebidas", 5000],
    ["JUGO DE MARACUYA", "bebidas", 6000]
]      
#configuracion de la promocion 
categoria_objetivo = "plato principal"
umbral_precio = 10000
descuento = 0.15  
def calcular_precio_final(precio, categoria): 
    #logica de negocio: 15% de descuento si cumple categoria y umbral
    if categoria == categoria_objetivo and precio > umbral_precio:
        return precio * (1- descuento)
    return precio
# salida de resultados
respuesta = input ("¿desea ver el listado de productos con sus precios finales? (s/n):")
if respuesta.lower()== 's':
 print (f"{'nombre':<20} | {'precio base':<12} | {'precio final':<12}")
print ("_" * 50) 
# encabezado color azul 
azul = "\033[94m"
reset = "\033[0m"
# platos principales
print (f"\n{azul} PLATOS PRINCIPALES:{reset}")
for item in menu:
   nombre, categoria, precio = item
   if categoria == "plato principal":
      precio_final = calcular_precio_final(precio, categoria)
      print (f"{nombre:<20} | {precio:<11} | {precio_final:11.0f}")
# postres
print (f"\n{azul} POSTRES:{reset}")
for item in menu:
   nombre, categoria, precio = item 
   if categoria == "postres":
      precio_final = calcular_precio_final(precio, categoria)
      print (f" {nombre:<20} | {precio:<11} | {precio_final:<11.0f}")
# ensaladas 
print (f"\n{azul} ENSALADAS:{reset}")
for item in menu:
   nombre, categoria, precio = item
   if categoria == "ensaladas":
      precio_final = calcular_precio_final(precio, categoria)
      print (f"{nombre:<20} | {precio:<11} | {precio_final:11.0f}")
# bebidas 
print (f"\n{azul} BEBIDAS:{reset}")
for item in menu: 
   nombre, categoria, precio = item 
   if categoria == "bebidas":
      precio_final = calcular_precio_final(precio, categoria)
      print (f"{nombre:<20} | {precio:<11} | {precio_final:11.0f}")
print ("¡GRACIAS POR USAR EL SISTEMA!")   