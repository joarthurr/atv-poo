from .livros import Livro
from .usuarios import Usuario
from .emprestimos import Emprestimo


def main():
    usuario = Usuario(nome="Ana", id_usuario="U001")

    livro = Livro(titulo="1984", autor="George Orwell", codigo="L001")

    if livro.disponivel:
        emprestimo = Emprestimo(livro=livro, usuario=usuario)
        livro.disponivel = False
    else:
        emprestimo = None
        print(f"Livro '{livro.titulo}' não está disponível para empréstimo.")

    print(f"Usuário: {usuario.nome} (id={usuario.id_usuario})")
    print(f"Livro: {livro.titulo} - Disponível: {livro.disponivel}")
    print(f"Empréstimo ativo: {getattr(emprestimo, 'ativo', False)}")

    if emprestimo is not None:
        emprestimo.ativo = False
        livro.disponivel = True

    print("\nApós devolução:")
    print(f"Livro: {livro.titulo} - Disponível: {livro.disponivel}")
    print(f"Empréstimo ativo: {getattr(emprestimo, 'ativo', False)}")


if __name__ == "__main__":
    main()