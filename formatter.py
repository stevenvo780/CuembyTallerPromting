def format_response(response):
    # Obtiene el contenido de la respuesta, asumiendo que tiene el atributo 'content'
    text = getattr(response, 'content', str(response))
    return "\n".join("    " + line for line in text.splitlines())
