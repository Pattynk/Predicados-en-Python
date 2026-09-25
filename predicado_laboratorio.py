#Universo (D)
DOMINIO = {
    "personas": { "Irma", "Anette", "Jose", "Jorge", "Francisco", "Raul", "Prof_Lulu", "Prof_Guillermo", "Prof_Xenia" },
    "clases": { "Automatas", "Investigacion_I", "Investigacion_II", "Redes", "Programacion", "Graficacion" },
    "aulas": {"Aula_101", "Lab_C3"},
    "examenes": {"Parcial_1", "U1_Programacion"}
}

#Aulas
AULAS = {"Aula_101", "Lab_C3"}

#Laboratorio (L)
LABORATORIOS = {"Lab_C3"}


def es_laboratorio(aula: str) -> bool:
    """Predicado unario: Laboratorio(z)"""
    if aula not in DOMINIO["aulas"]:
        raise ValueError(f"'{aula}' no pertenece al dominio válido de aulas.")
    return aula in LABORATORIOS


if __name__ == "__main__":
    print("--- Predicado: Laboratorio(L) ---")
    
#Consulta Positiva, porque Lab_C3 sí es un laboratorio de especialidad
    print(f"¿Laboratorio(Lab_C3)?: {es_laboratorio('Lab_C3')}")
    
#Consulta Negativa, porque Aula_101 solo es un salón de clases
    print(f"¿Laboratorio(Aula_101)?: {es_laboratorio('Aula_101')}")