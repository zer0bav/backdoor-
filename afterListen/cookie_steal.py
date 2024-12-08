import requests

def steal():
    session = requests.Session()
    cookies = session.cookies.get_dict()
    with open("cookies.txt", "w") as f:
        f.write(str(cookies))
    return "cookies.txt"  
