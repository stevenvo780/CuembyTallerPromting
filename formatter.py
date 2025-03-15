def format_response(response):
    text = getattr(response, 'content', str(response))
    return "\n".join("    " + line for line in text.splitlines())
