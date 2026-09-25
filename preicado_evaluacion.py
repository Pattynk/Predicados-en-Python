# Universo (D)
DOMINIO = {
    "personas": { "Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul", "Prof_Lulu", "Prof_Guillermo", "Prof_Xenia" },
    "clases": { "Automatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion", "Graficacion" },
    "aulas": {"Aula_101", "Lab_C3"},
    "examenes": {"Parcial_1", "U1_Programacion"}  }

#Clasificación
ESTUDIANTES = {"Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul"}
EXAMENES = {"Parcial_1", "U1_Programacion"}
CLASES = {"Automatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion", "Graficacion"}

#Evaluación (x: estudiante, e: examen, y: clase)
EVALUACION = {
    ("Irma", "U1_Programacion", "Programacion"),
    ("Jose", "Parcial_1", "Automatas"), 
    ("Jorge", "Parcial_1", "Investigacion_I"),
    ("Raul", "Parcial_1", "Investigacion_II"),
    ("Francisco", "Parcial_1", "Redes")}


def evaluacion(estudiante: str, examen: str, clase: str) -> bool:
    """Predicado ternario: Rindio(x, e, y)"""
    if (
        estudiante not in DOMINIO["personas"]
        or examen not in DOMINIO["examenes"]
        or clase not in DOMINIO["clases"]
    ):
        raise ValueError("Uno o más argumentos no pertenecen al dominio válido.")
    
    return (estudiante, examen, clase) in EVALUACION


if __name__ == "__main__":
    print("--- Predicado: Rindio(x, e, y) ---")
    
#Consulta Positiva
    print(f"¿Evaluacion(Irma, U1_Programacion, Programacion)?: {evaluacion('Irma', 'U1_Programacion', 'Programacion')}")
    
#Consulta Negativa
    print(f"¿Evaluacion(Francisco, Parcial_1, Automatas)?: {evaluacion('Francisco', 'Parcial_1', 'Automatas')}")