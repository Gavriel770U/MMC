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
                data = first_bin_file.readlines() + second_bin_file.readlines()
                total = b''
                
                for line in data:
                    total += line                
                
                merged_bin_file.write(total)

if __name__ == '__main__':
    main()