```python
import os
import glob

def search_markdown_files(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    if search_string in content:
                        print(f"Found '{search_string}' in: {file_path}")

# Example usage:
directory = "/path/to/folder"
search_string = "specific string"
search_markdown_files(directory, search_string)

```

```python
def find_string_line(md_file, search_string):
    with open(md_file, 'r') as file:
        lines = file.readlines()
    for line_num, line in enumerate(lines, start=1):
        if search_string in line:
            return line_num
    return -1

md_file = "/path/to/markdown_file.md"  # Replace with the path to your Markdown file
search_string = "specific string"  # Replace with the string you want to search for

line_number = find_string_line(md_file, search_string)
if line_number != -1:
    print(f"The string '{search_string}' is found on line {line_number} in the Markdown file.")
else:
    print(f"The string '{search_string}' is not found in the Markdown file.")

```

```python
## DESCRIPTION: Creates separate Markdown files based on a given Markdown table.
import os

def create_markdown_files_from_table(table_file):
    with open(table_file, 'r') as f:
        table_content = f.read()

    # Assuming the table is in Markdown format with '|' as the separator
    rows = table_content.strip().split('\\n')
    headers = rows[0].split('|')[1:-1]  # Exclude first and last column

    for row in rows[2:]:
        row_data = row.split('|')[1:-1]  # Exclude first and last column

        # Extract data from the row
        file_name = row_data[0].strip()
        frontmatter = {header.strip(): data.strip() for header, data in zip(headers, row_data[1:])}

        # Create a new Markdown file
        file_path = f'{file_name}.md'
        with open(file_path, 'w') as new_file:
            # Write the YAML frontmatter
            new_file.write('---\\n')
            for key, value in frontmatter.items():
                new_file.write(f'{key}: {value}\\n')
            new_file.write('---\\n')

            # Write the remaining content of the row
            new_file.write('\\n'.join(row_data[1:]))

        print(f'Successfully created {file_path}')

# Example usage
create_markdown_files_from_table('table.md')
```