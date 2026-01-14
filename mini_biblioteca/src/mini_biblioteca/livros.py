class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel