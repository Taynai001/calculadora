
    #MEDIDOR DE TERMODINAMICA
import subprocess
subprocess.run(["clear"])

print("\n")
print("\t \t LA TERMODINAMICA ")
print("\n")
print(" -> RECUERDA QUE LA TERMODINAMICA ES LA RAMA DE LA FÍSICA QUE ESTUDIA LOS EFECTOS DE")
print(" -> LOS CAMBIOS DE TEMPERATURA, PRESIÓN Y VOLUMEN DE UN SISTEMA FÍSICO")
print("\n")
print(" PD: la temperatura siempre tienes que transformarlo en 'kelvin'")
print("\n")
print(" ELIJE UNA OPCIPÓN")
print("\n")
print(" 1. HALLAR EL VOLUMEN FINAL (1)")
print("\n")

n = float(input("introduca el numero: "))

if n == 1:
    print("<---------------------------------------------------->")
    print("\n")
    print(" -> K = 'kelvin'")
    print(" -> T = 'temperatura'")
    print(" -> C = 'celcius'")
    print(" -> i = 'inicial'")
    print(" -> f = 'final'")
    print("\n")
    print("\t -> Ley de Charles: Si la temperatura sube el volumen sube y viceversa")
    print("\n")
    
    ti = float(input("INTRODUSCA EL VALOR DE LA TEMPERATURA(i): "))
    print("\n")
    vi = float(input("INTRODUSCA EL VALOR DEL VOLUMEN(i): "))
    print("\n")
    tf = float(input("INTRODUSCA EL VALOR DE LA TEMPERATURA(f): "))
    print("\n")
    
        #FORMULA
    print(" vf = ", "(", tf, " x ",vi, ")", " ÷ ", ti)
    vf = (tf*vi)/ti
    print("\n")
    
    print(" RPTA: ", vf)