import os
from consts import *

def get_sorted_dict_by_values(dct: dict) -> dict:
    return dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))

def get_dict_values_sum(dct: dict) -> float:
    dct_sum = 0
    for val in dct.values():
        dct_sum += val
    
    return dct_sum

def get_frequencies(data: str) -> dict:
    count = {}
        
    for ch in data:
        if not ch in count.keys():
            count[ch] = 1
        else:
            count[ch] += 1

    data_vals_sum = get_dict_values_sum(count)
    
    for key in count.keys():
        count[key] /= data_vals_sum

    return get_sorted_dict_by_values(count)
    
def get_priority_in_dict(dct: dict, val: any) -> int:
    index = 0
    for key in dct.keys():
        if key == val:
            return index
        index += 1
        
    return -1
 

def main() -> None:
    with open('./resources/encrypted.txt', READ_FILE_MODE) as enc_file:
        data = enc_file.read()
        freq = get_frequencies(data=data)
        
        with open('./output.txt', WRITE_FILE_MODE) as dec_file:
            for ch in data:
                p = get_priority_in_dict(freq, ch)
                if p != -1 and p < len(LETTERS_SCORE.keys()):
                    dec_file.write(list(LETTERS_SCORE.items())[p][0])             

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    main()