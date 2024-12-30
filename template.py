import os

class ProjectSetup:
    @staticmethod
    def setup_project():
        directories = [
            "frontend",
            "intermediate_representation",
            "backend",
            "model",
            "data/datasets",
        ]

        files_content = {
            "main.py": """<main.py content here>""",
            "frontend/parser.py": """<parser.py content here>""",
            "intermediate_representation/ir_generator.py": """<ir_generator.py content here>""",
            "backend/code_generator.py": """<code_generator.py content here>""",
            "requirements.txt": """transformers\ntorch\npytest\nargparse\n""",
        }

        for directory in directories:
            os.makedirs(directory, exist_ok=True)

        for file_path, content in files_content.items():
            full_path = os.path.join(file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                f.write(content)

        print("Project structure generated successfully.")
