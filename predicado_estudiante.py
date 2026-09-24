#Universo (D)
DOMINIO = {
    "personas": {"Irma", "Anette", "Jose", "Jorge", "Sofia", "Elena", "Prof_Lulu", "Prof_Guillermo"},
    "clases": {"Autómatas", "Fisica_I", "Fisica_II", "Quimica", "Algebra", "Historia"},
    "aulas": {"Aula_101", "Lab_Bioquimica"},
    "examenes": {"Parcial_1", "Final_Algebra"}
}

#Alumno (x)
ESTUDIANTES = {"Irma", "Anette", "Jose", "Jorge", "Sofia", "Elena"}
#Profesor (y)
PROFESORES = {"Prof_Lulú", "Prof_Guillermo"}

#Función para revisar el predicado del estudiante
def es_estudiante(x: str) -> bool:
    """Predicado unario: Estudiante(x)"""
    todas_las_entidades = set().union(*DOMINIO.values())
    if x not in todas_las_entidades:
        raise ValueError(f"'{x}' no pertenece al dominio del discurso.")
    return x in ESTUDIANTES

if __name__ == "__main__":
    print("--- Predicado: Estudiante(x) ---")
    
#Consulta Positiva: True para Irma alumno
    consulta_pos = "Irma"
    print(f"¿Estudiante({consulta_pos})?: {es_estudiante(consulta_pos)}") 
    
#Consulta Negativa: False para Lulu alumno
    consulta_neg = "Prof_Lulu"
    print(f"¿Estudiante({consulta_neg})?: {es_estudiante(consulta_neg)}") 

