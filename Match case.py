def describir_estado(codigo):
    match codigo:
        case 200:
            return "OK (Petición exitosa)"
        case 404 | 403: # Múltiples valores en un solo caso
            return "Error del cliente"
        case 500:
            return "Error del servidor"
        case _: # Si no coincide con ninguno de los anteriores
            return "Código desconocido"

print(describir_estado(200)) # Salida: OK (Petición exitosa)
print(describir_estado(404)) # Salida: Error del cliente
print(describir_estado(503)) # Salida: Código desconocido
