def save_to_file(feature, text_array, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        #text_with_newlines = ''.join(map(str, text_array))
        file.write(f"feature: {feature}\ntext:\n{text_array}\n\n")