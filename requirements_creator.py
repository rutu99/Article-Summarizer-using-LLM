import subprocess

def create_requirements_file(output_file="requirements.txt"):
    try:
        with open(output_file, "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)
        print(f"{output_file} created.")
    except Exception as e:
        print(f"Error: {e}")
create_requirements_file()