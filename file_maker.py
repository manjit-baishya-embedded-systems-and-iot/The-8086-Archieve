import os

# Specify the path to the Markdown file
markdown_file_path = 'Project Ideas.md'

# Specify the directory where you want to create the new files
output_directory = '04. Project Work'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the Markdown file and extract problem titles
with open(markdown_file_path, 'r') as file:
    lines = file.readlines()

# Function to sanitize filenames
def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c == ' ' else '_' for c in filename).rstrip()

# Extract the titles and create files
for line in lines:
    if line.startswith('##') or any(line.startswith(f'{i}.') for i in range(1, 51)):
        # Extract the title after the number and the space
        parts = line.split('. ', 1)
        if len(parts) == 2:
            number = parts[0].strip()
            title = parts[1].strip()
            # Sanitize the title to create a valid filename

            if (int(number) < 9):
                filename = "0" + sanitize_filename(f"{number}") + '. ' + sanitize_filename(f"{title}") + '.asm'
            else:
                filename = sanitize_filename(f"{number}") + '. ' + sanitize_filename(f"{title}") + '.asm'
            
            filename = filename.replace('_', '')

            # Create the new file in the specified directory
            with open(os.path.join(output_directory, filename), 'w') as new_file:
                new_file.write(f'# {title}\n\n')