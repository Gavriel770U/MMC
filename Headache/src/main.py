import os

CURRENT_DIR: str = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR: str = os.path.join(CURRENT_DIR, '..', 'resources')
FIRST_FILE_NAME: str = os.path.join(RESOURCES_DIR, "start\\first.png")
SECOND_FILE_NAME: str = os.path.join(RESOURCES_DIR, "start\\second.png")
OUTPUT_FOLDER_NAME: str = os.path.join(RESOURCES_DIR, "output")
READ_BIN: str = 'rb'
WRITE_BIN: str = 'wb'

def main() -> None: 
    # create ../resources/output/  
    if not os.path.exists(OUTPUT_FOLDER_NAME):
        os.makedirs(OUTPUT_FOLDER_NAME)
    
    output_file_name = os.path.join(OUTPUT_FOLDER_NAME, "merged.png")    
    
    with open(FIRST_FILE_NAME, READ_BIN) as first_bin_file:
        with open(SECOND_FILE_NAME, READ_BIN) as second_bin_file:
            with open(output_file_name, WRITE_BIN) as merged_bin_file:
                total = b''
                
                first_file_lines = []
                second_file_lines = []
                
                for line in first_bin_file.readlines():
                    if line and len(line) > 1 and line != '\n':
                        first_file_lines.append(line)
                 
                for line in second_bin_file.readlines():
                    if line and len(line) > 1 and line != '\n':
                        second_file_lines.append(line)  
                
                while len(first_file_lines) or len(second_file_lines):
                    if len(first_file_lines):
                        total += first_file_lines[0]
                        first_file_lines = first_file_lines[1:]
                    if len(second_file_lines):
                        total += second_file_lines[0]
                        second_file_lines = second_file_lines[1:]
                
                merged_bin_file.write(total)

if __name__ == '__main__':
    main()