def generate_code(ir, target_language):
    if target_language == "python":
        return "\n".join(ir["instructions"])
    elif target_language == "c":
        return "/* C Code Generated */\n" + "\n".join(ir["instructions"])
    else:
        raise ValueError(f"Unsupported target language: {target_language}")