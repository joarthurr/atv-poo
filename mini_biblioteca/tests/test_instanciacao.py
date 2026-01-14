import pytest

from mini_biblioteca.livro import Livro
from mini_biblioteca.usuario import Usuario
from mini_biblioteca.emprestimo import Emprestimo

def test_instanciacao_livro():
    livro = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", codigo="L002")
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == "J.R.R. Tolkien"
    assert livro.codigo == "L002"
    assert livro.disponivel is True

def test_instanciacao_usuario():
    usuario = Usuario(nome="Carlos", id_usuario="U002")
    assert usuario.nome == "Carlos"
    assert usuario.id_usuario == "U002"

def test_instanciacao_emprestimo():
    usuario = Usuario(nome="Maria", id_usuario="U003")
    livro = Livro(titulo="A Revolução dos Bichos", autor="George Orwell", codigo="L003")
    emprestimo = Emprestimo(livro=livro, usuario=usuario)
    
    assert emprestimo.livro == livro
    assert emprestimo.usuario == usuario
    assert emprestimo.ativo is True

if __name__ == "__main__":
    pytest.main()