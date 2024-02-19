import json
import os
import re

def generar_id():
    try:
        with open(os.path.join(os.getcwd(), "registro_campers.json"), "r") as file:
            id_camper = json.load(file)
    except FileNotFoundError:
        id_camper = 1
        with open(os.path.join(os.getcwd(), "registro_campers.json"), "w") as file:
            json.dump(id_camper, file, indent=4)
    return id_camper


def crear_camper(camper_data):
    registro_campers = "registro_campers.json"

    if not os.path.exists(registro_campers):
        with open(registro_campers, "w") as file:
            json.dump([], file)

    with open(registro_campers, "r") as file:
        campers = json.load(file)

    id_camper = generar_id()
    camper_data["id"] = id_camper

    campers.append(camper_data)

    with open(registro_campers, "w") as file:
        json.dump(campers, file, indent=4)

def validar_camper(camper, valor):
    if not valor:
        raise ValueError(f"El campo {camper} no puede estar vacío.")
    return valor

def crear_camper_con_validacion(nombres, apellidos, direccion, acudiente, telefonos_contacto, estado, riesgo, documento):
    documento= validar_camper("numro de documento", documento)
    nombres = validar_camper("nombres", nombres)
    apellidos = validar_camper("apellidos", apellidos)
    direccion = validar_camper("direccion", direccion)
    acudiente = validar_camper("acudiente", acudiente)
    telefonos_contacto = validar_camper("telefonos_contacto", telefonos_contacto)
    estado = validar_camper("estado", estado)
    riesgo = validar_camper("riesgo", riesgo)

    camper_data = {
        "numero de documento": documento,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefonos_contacto": telefonos_contacto,
        "estado": estado,
        "riesgo": riesgo,
        "numero de documento": documento
    }

    crear_camper(camper_data)