import pymongo


class BancoDeDados:
    def __init__(self, usuario, senha, cluster, banco, colecao):
        self.usuario = usuario
        self.senha = senha
        self.cluster = cluster
        self.banco = banco
        self.colecao = colecao

    def conectar(self):
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{self.usuario}:{self.senha}@{self.cluster}/?retryWrites=true&w=majority")
        self.db = self.client.get_database(self.banco)
        self.col = self.db.get_collection(self.colecao)

    def inserir_documento(self, documento):
        self.col.insert_one(documento)
        print(f"Mensagem enviada")

    def get_messages(self, user):
        results = list(self.col.find({"to": user[0]}))
        return results

    def update_was_read(self, id):
        filtro = {"_id": id}
        atualizacao = {"$set": {"wasRead": True}}
        self.col.update_one(filtro, atualizacao)

