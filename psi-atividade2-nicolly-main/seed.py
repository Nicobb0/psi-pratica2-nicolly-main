from models import Autor, Livro
from database import nova_sessao

def popular_banco(session):
    # TODO: crie pelo menos 3 autores e 6 livros.
    # TODO: relacione os livros aos autores.
    # TODO: use session.add ou session.add_all e session.commit.
    with session as session:
        try:
            autor1 = Autor(nome="Ali Hazelwood", pais="Italia")
            autor2 = Autor(nome="Nicholas Sparks", pais="Americano")
            autor3 = Autor(nome="Machado de Assis", pais="Brasil")
            autor4 = Autor(nome="Manuel Bandeira", pais="Brasil")
            session.add_all([autor1, autor2, autor3, autor4])

            livro1 = Livro(titulo="A Hipótese do Amor", ano=2021, autor_id=1)
            livro2 = Livro(titulo="A razão do amor", ano=2022, autor_id=1)
            livro3 = Livro(titulo=" Diário de uma Paixão", ano=1996, autor_id=2)
            livro4 = Livro(titulo="Uma Carta de Amor", ano=1998, autor_id=2)
            livro5 = Livro(titulo="Dom Casmurro", ano=1899, autor_id=3)
            livro6 = Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor_id=3)
            session.add_all([livro1, livro2, livro3, livro4, livro5, livro6])

            session.commit()
        except Exception:
            session.rollback()