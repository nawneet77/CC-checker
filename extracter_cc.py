import re

def extract_pipe_format(text):
    pattern = r'\b\d{16}\|\d{2}\|\d{4}\|\d{3}\b'

    matches = re.findall(pattern, text)
    
    return matches

if __name__ == "__main__":
    input_file = input("Enter the File name: ")
    output_file = 'cc.txt'
    
    with open(input_file, 'r') as file:
        large_text_block = file.read()

    extracted_text = extract_pipe_format(large_text_block)
    
    with open(output_file, 'w') as file:
        for item in extracted_text:
            file.write(item + '\n')

    print(f"Extracted matches have been saved to {output_file}")
