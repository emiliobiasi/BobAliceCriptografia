from Message import Message
from fernet import cifra, decifra


def send_message(user, banco):
    m = input(f"\nOk {user[0]}, digite a mensagem: \n")
    txtchave = input("Agora digite um pequeno texto para cifrar a mensagem: \n")
    m_cifrada = cifra(txtchave, m)
    msn = Message(user[0], user[1], m_cifrada)
    print(msn.__str__())
    banco.inserir_documento(msn.to_json())


def see_message(user, banco):
    lista_de_docs = banco.get_messages(user)
    lista_de_mensagens = []
    for documento in lista_de_docs:
        # Extrai o valor do campo "message" e adiciona à lista_de_mensagens
        mensagem = documento['message']
        lista_de_mensagens.append(mensagem)

    print(f"\nOk {user[0]}, aqui estão suas mensagens cifradas:\n")
    i = 0
    for e in lista_de_mensagens:
        print(f"{i} - {e}")
        i += 1

    opcao = int(input("\nQual das mensagens voce deseja decifrar? "))
    txtchave = input(f"\n{user[0]}, qual a chave secreta:")

    print("\nTexto da mensagem decifrado:")
    print(f"{user[1]}: {decifra(txtchave, lista_de_mensagens[opcao])}")

