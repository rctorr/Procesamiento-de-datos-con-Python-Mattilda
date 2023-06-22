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
        return 0  # Acceso denedado
    username_db = base_de_datos[username]
    # Se valida si el usuario es lector, ya que es el rol más simple
    if username_db["rol"] == "lector":
        return 2  # Lectura autorizada
    # Se valida si el usuario es admin, ya que no necesita nip
    elif username_db["rol"] == "admin":
        return 1  # Edición autorizada
    elif username_db["rol"] == "editor" and "nip_de_acceso" in username_db:
        # Acceso denegado o Edición autorizada, False -> 0, True -> 1
        return int(username_db["nip_de_acceso"] == nip_de_acceso)
    else:
        return 0  # En cualquier otro caso acceso denegado


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
