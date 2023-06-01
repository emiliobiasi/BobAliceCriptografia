from Message import Message
from fernet import cifra, decifra


def send_message(user, banco):
    m = input(f"\nOk {user[0]}, digite a mensagem: \n")
    txtchave = input("Agora digite um pequeno texto para cifrar a mensagem: \n")
    m_cifrada = cifra(txtchave, m)
    msn = Message(user[0], user[1], m_cifrada)
    banco.inserir_documento(msn.to_json())


def see_message(user, banco):
    lista_de_docs = banco.get_messages(user)
    if lista_de_docs:
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

        opcao = -1
        while opcao < 0 or opcao > int(len(lista_de_docs)) - 1:
            opcao = int(input("\nQual das mensagens voce deseja decifrar? "))

        txtchave = input(f"\n{user[0]}, qual a chave secreta:")
        try:
            print("\nTexto da mensagem decifrado:")
            print(f"{user[1]}: {decifra(txtchave, lista_de_mensagens[opcao])}")
            doc = lista_de_docs[opcao]
            id_value = doc['_id']
            banco.update_was_read(id_value)
        except Exception as e:
            print("ERRO: Palavra chave incorreta.", str(e))
    else:
        print("Não existe mensagens em sua caixa de mensagens.")

