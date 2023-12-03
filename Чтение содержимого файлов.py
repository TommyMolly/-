import os

directory = r"C:\Users\Artem\Desktop\cook_book\Files"

files = [
    "1.txt",
    "2.txt",
    "3.txt"
]

file_contents = {}
for file_name in files:
    file_path = os.path.join(directory, file_name)
    print(f"Reading file: {file_path}")  # Добавлено для отладки
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_name] = {
            'lines_count': len(lines),
            'content': lines
        }

sorted_files = sorted(file_contents.items(), key=lambda x: x[1]['lines_count'])

result_file_path = os.path.join(directory, 'result.txt')
print(f"Writing to result file: {result_file_path}")  # Добавлено для отладки
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_name, data in sorted_files:
        result_file.write(f"{file_name}\n{data['lines_count']}\n")
        result_file.write(''.join(data['content']))
        result_file.write('\n')

print("Program completed successfully")  # Добавлено для отладки
