def generate_ir(parsed_code):
    ir = {"instructions": parsed_code["tokens"]}
    print(f"Generated IR: {ir}")
    return ir