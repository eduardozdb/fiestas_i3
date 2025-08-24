def get_mensaje_sk(tipo):
    
    ALERTA = '¡Escucha con atención!'

    if tipo == 'inicio_juego':
        return '¡Bienvenido al Juego de Fiestas!'
    
    elif tipo == 'ins_inicial':
        return f'{ALERTA} Di la palabra "USUARIO" seguido de tu número de usuario para buscar tu información, ejemplo: "USUARIO 1".'
    
    return None