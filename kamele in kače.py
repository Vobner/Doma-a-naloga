import re

def convert_camel_to_snake_case(word):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', word).lower()

def convert_variable_names(content):
    lines = content.split('\n')
    
    converted_lines = []
    for line in lines:
        indentation = re.match(r'^\s*', line).group(0) 
        words = line.split()
        
        converted_words = []
        for word in words:
            if word in ['True', 'False', 'True:']:  
                converted_words.append(word)
            elif "'" in word or '"' in word:  
                converted_words.append(word)
            else:
                converted_words.append(convert_camel_to_snake_case(word))
        
        converted_line = ' '.join(converted_words)
        converted_lines.append(indentation + converted_line)
    
    return '\n'.join(converted_lines)

input_file_path = 'mnozenje.py'
output_file_path = 'mnozenje2.py'

with open(input_file_path, 'r') as f:
    content = f.read()

converted_content = convert_variable_names(content)

with open(output_file_path, 'w') as f:
    f.write(converted_content)