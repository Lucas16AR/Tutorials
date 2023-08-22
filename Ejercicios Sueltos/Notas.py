nota = int(input("Ingrese una nota para saber la acreditacion: "))

if nota > 0:
    print("Desaprobado")
elif nota > 50:
    print("Aprobado")
elif nota > 80:
    print("Aprobado sobresaliente")