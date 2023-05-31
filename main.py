from bd import BancoDeDados
from functions import send_message, see_message
from menu import login, menu

banco = BancoDeDados("emiliobiasi", "emiliobiasi", "chat.rjdfttx.mongodb.net", "ChatBob&Alice", "Message")
banco.conectar()

r = 1
while r != "0":
    user = login()

    option = menu(user[0], user[1])

    if option == "1":
        send_message(user, banco)
    else:
        see_message(user, banco)

    print("\n1 - Voltar ao Menu")
    print("0 - Finalizar programa")
    r = input("Deseja sair? \n")

