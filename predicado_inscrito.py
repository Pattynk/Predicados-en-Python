#Universo (D)
DOMINIO = {
    "personas": { "Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul", "Prof_Lulu", "Prof_Guillermo" },
    "clases": { "Autómatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion" },
    "aulas": {"Aula_101", "Lab_C3"},
    "examenes": {"Parcial_1", "U1_Programacion"}
}

#Clasificación del dominio
#Estudiantes (x)
ESTUDIANTES = {"Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul"}
#Profesores (z)
PROFESORES = {"Prof_Lulu", "Prof_Guillermo", "Prof_Xenia"}
#Clases (y)
CLASES = {"Autómatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion", "Graficacion"}

#Información de las inscripciones (x,y)
INSCRIPCIONES = {
    ("Irma", "Programacion"),
    ("Anette", "Programacion"),
    ("Jose", "Autómatas"),
    ("Jorge", "Investigacion_I"),
    ("Raul", "Investigacion_II"),
    ("Francisco", "Redes")
}

def esta_inscrito(estudiante: str, clases: str) -> bool:
    """Predicado binario: Inscrito(x, y)"""
    if estudiante not in DOMINIO["personas"] or clases not in DOMINIO["clases"]:
        raise ValueError("Argumentos fuera del dominio válido.")
    return (estudiante, clases) in INSCRIPCIONES

if __name__ == "__main__":
    print("--- Predicado: Inscrito(x, y) ---")
    
#Consulta Positiva, true para Irma inscrita en Programacion
    print(f"¿Inscrito(Irma, Programacion)?: {esta_inscrito('Irma', 'Programacion')}")
    
#Consulta Negativa, false para Francisco inscrito en Programacion
    print(f"¿Inscrito(Francisco, Programacion)?: {esta_inscrito('Francisco', 'Programacion')}")