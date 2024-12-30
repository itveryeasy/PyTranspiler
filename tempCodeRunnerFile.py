import sys
from frontend.parser import parse_code
from intermediate_representation.ir_generator import generate_ir
from backend.code_generator import generate_code

def main(input_file, target_language):
    with open(input_file, 'r') as f:
        source_code = f.read()
    parsed_code = parse_code(source_code)
    ir = generate_ir(parsed_code)
    target_code = generate_code(ir, target_language)
    output_filename = f"output.{target_language}"
    with open(output_filename, 'w') as f:
        f.write(target_code)
    print(f"Compilation successful: {output_filename}")