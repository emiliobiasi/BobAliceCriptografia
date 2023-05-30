def login():
    user = "a"
    while user not in ["Bob", "Alice"]:
        user = input("Login: ")
    if user == "Bob":
        friend = "Alice"
    else:
        friend = "Bob"
    return user, friend


def menu(user, friend):
    option = 0
    while option not in ["1", "2"]:
        print(f"\nVocê está conectado como: {user}")
        print(f"\n{user}, o que deseja? ")
        print(f"1 - Enviar uma mensagem secreta para {friend}?")
        print("2 - Ler suas mensagens que estão no banco?")
        option = input("Digite umas das opções a cima: ")
    return option
