import requests
from bs4 import BeautifulSoup

print("""
███╗   ███╗ █████╗ ██╗██╗          ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔══██╗██║██║         ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║███████║██║██║         ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║██║         ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                          by schizophrenic
     
""")

def main():
    option = input("""
[1] Check si un mail existe
[2] Générer des combinaisons d'un mail et check si ils existent
[3] Menu d'aide
""")
    if option == "1":
        mail = input("Veuillez entrer le nom d'un gmail: ")
        page = requests.get(f"https://mailscrap.com/api/verifier-lookup/{mail}@gmail.com")
        soup = BeautifulSoup(page.content, "html.parser")
        if soup is not None:
            if '"deliverable":true' in str(soup):
                print(f"[+] {mail}@gmail.com")
            else:
                print(f"[-] {mail}@gmail.com")
    elif option == "2":
        mail = input("Veuillez entrer le nom d'un gmail: ")
        i = 000
        while i < 999:
            page = requests.get(f"https://mailscrap.com/api/verifier-lookup/{mail}{i}@gmail.com")
            soup = BeautifulSoup(page.content, "html.parser")
            if soup is not None:
                if '"deliverable":true' in str(soup):
                    print(f"[+] {mail}{i}@gmail.com")
                else:
                    print(f"[-] {mail}{i}@gmail.com")
            i += 1
    elif option == "3":
        print("Pour utiliser le tool il faut entrer le nom d'un gmail par exemple pour schizophrenic@gmail.com, entrez schizophrenic")
        return main()
    else:
        print("Option Invalide")
        return main()

main()
