#Universo (D)
DOMINIO = {
    "personas": { "Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul", "Prof_Lulu", "Prof_Guillermo", "Prof_Xenia" },
    "clases": { "Autómatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion", "Graficacion" },
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

#Información de las inscripciones (x,y) ESTA INFORMACIÓN NO IMPORTA EN ESTA CONSULTA
INSCRIPCIONES = {
    ("Irma", "Programacion"),
    ("Anette", "Programacion"),
    ("Jose", "Autómatas"),
    ("Jorge", "Investigacion_I"),
    ("Raul", "Investigacion_II"),
    ("Francisco", "Redes")
}

#Información de las asignaturas que imparte (z,y)
IMPARTE = {
    ("Prof_Lulu", "Programacion"),
    ("Prof_Guillermo", "Graficacion"),
    ("Prof_Xenia", "Automatas"),
}

def imparte(profesor: str, clases: str) -> bool:
    """Predicado binario: Imparte(z, y)"""
    if profesor not in DOMINIO["personas"] or clases not in DOMINIO["clases"]:
        raise ValueError("Argumentos fuera del dominio válido.")
    return (profesor, clases) in IMPARTE


if __name__ == "__main__":
    print("--- Predicado: Imparte(z, y) ---")
    
#Consulta Positiva, true para Prof_Lulu ya que ella imparte Programacion
    print(f"¿Imparte(Prof_Lulu, Programacion)?: {imparte('Prof_Lulu', 'Programacion')}")
    
#Consulta Negativa, false para Prof_Guillermo, ya que él imparte Graficacion
    print(f"¿Imparte(Prof_Guillermo, Automatas)?: {imparte('Prof_Guillermo', 'Autómatas')}")