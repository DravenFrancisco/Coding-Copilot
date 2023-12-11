import os

def create_markdown_files_from_table(table_file):
    with open(table_file, 'r') as f:
        table_content = f.read()
        # print(table_content)

    # Assuming the table is in Markdown format with '|' as the separator
    rows = table_content.strip().split('\\n')
    # print(rows)
    headers = rows[0].split('|')[1:-1]  # Exclude first and last column

    for row in rows[2:]:
        row_data = row.split('|')[1:-1]  # Exclude first and last column
        # print(row_data)
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
