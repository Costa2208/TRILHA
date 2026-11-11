class Livro:

    def __init__(self, titulo, autor, paginas, paginas_lidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, quantidade):
        if self.paginas_lidas + quantidade > self.paginas:
            print(
                f"Você tentou ler páginas demais! O livro possui apenas {self.paginas} páginas."
            )
            return

        self.paginas_lidas += quantidade
        print(f"Lendo {quantidade} páginas...")

    def progresso(self):
        porcentagem = (self.paginas_lidas / self.paginas) * 100
        print(f"Você já leu {porcentagem:.1f}% do livro '{self.titulo}'.")



meu_livro = Livro("POO", "Mateus", 100, 50)

meu_livro.ler(20)  

meu_livro.progresso()  