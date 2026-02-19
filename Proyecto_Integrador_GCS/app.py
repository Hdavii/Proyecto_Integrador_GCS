# Módulo de Autenticación

def login(usuario, password):
    if not usuario or not password:
        return "Datos inválidos"
    if len(password) < 4:
        return "Contraseña demasiado corta"
    return "Login correcto"

if __name__ == "__main__":
    print(login("admin", "1234"))
