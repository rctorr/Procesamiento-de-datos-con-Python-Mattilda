# BD de usuario en formato diccionario
usuarios = {
    "manolito_garcia": {
        "rol": "admin"
    },
    "sebas_macaco_23": {
        "rol": "editor",
        "nip_de_acceso": 3594
    },
    "la_susanita_maestra": {
        "rol": "admin"
    },
    "pepe_le_pu_88": {
        "rol": "lector"
    },
    "jonny_bravo_estuvo_aqui": {
        "rol": "editor",
        "nip_de_acceso": 9730
    },
    "alfonso_torres_69": {
        "rol": "editor",
        "nip_de_acceso": 2849
    },
    "jocosita_99": {
        "rol": "lector"
    }
}

def nivel_de_acceso_para_username(base_de_datos, username, nip_de_acceso):
    """ Valida el acceso para username usando instrucciones de Python de
    manera explícita """
    # Se valida si el usuario existe en la BD, si no se acabó
    if username not in base_de_datos:
        return 0
    # De aquí en adelante ya sabemos que el usuario existe en la BD
    # Primero el caso de Acceso denegado validando que el usuario teng rol
    # editor, tenga nip asignado en la BD y el nip coincida con el
    # proporcionado
    if base_de_datos[username]["rol"] == "editor" and \
        "nip_de_acceso" in base_de_datos[username] and \
        base_de_datos[username]["nip_de_acceso"] != nip_de_acceso:
        return 0  # Acceso denegado
    # 2o caso: Modo edición autorizada, cuando el rol es admin o el rol es
    # editor y el nip sea el correcto.
    if base_de_datos[username]["rol"] == "editor" and \
        base_de_datos[username]["nip_de_acceso"] == nip_de_acceso or \
        base_de_datos[username]["rol"] == "admin":
        return 1  # Acceso concedido
    # 3o caso: Modo lectura, cuando el rol es editor
    if base_de_datos[username]["rol"] == "lector":
        return 2  # Acceso concedido

# Caso usuario lector - 2
user = "jocosita_99"
nivel_acceso = nivel_de_acceso_para_username(usuarios, user, None)
print(f"username={user} acceso={nivel_acceso}")

# Caso usuario no existe, acceso denegado - 0
user = "no_existe"
nivel_acceso = nivel_de_acceso_para_username(usuarios, user, None)
print(f"username={user} acceso={nivel_acceso}")

# Caso usuario editor con nip correcto, edición autorizada - 1
user = "alfonso_torres_69"
nivel_acceso = nivel_de_acceso_para_username(usuarios, user, 2849)
print(f"username={user} acceso={nivel_acceso}")

# Caso usuario admin sin nip edición autorizada - 1
user = "la_susanita_maestra"
nivel_acceso = nivel_de_acceso_para_username(usuarios, user, 2849)
print(f"username={user} acceso={nivel_acceso}")

# Caso usuario editor con nip erroneo, acceso denegado - 0
user = "alfonso_torres_69"
nivel_acceso = nivel_de_acceso_para_username(usuarios, user, 2840)
print(f"username={user} acceso={nivel_acceso}")
