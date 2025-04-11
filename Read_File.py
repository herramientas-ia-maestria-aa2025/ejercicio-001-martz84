# Open in a read mode
with open('informacion.txt', 'r', encoding='utf-8') as file:
    # Read all lines
    lines = file.readlines()

    # Procees each line
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()  # Delete white spaces and new lines
        print(f"Línea {line_number}: {line}")
