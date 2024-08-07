print("Olá! Boa tarde! Bem-vindo ao cinema!")

# Lista de filmes e suas classificações etárias
filmes = {
    "1": ("Deadpool", 18),
    "2": ("Toy Story", 0),
    "3": ("Os Vingadores", 12),
    "4": ("A Bela e a Fera", 0)
}

# Mostra os filmes disponíveis
print("Temos alguns filmes disponíveis:")
for key in filmes:
    titulo, classificacao = filmes[key]
    print(f"{key}. {titulo} (Classificação: {classificacao}+ anos)")

# Solicita a escolha do filme
opcao = input("Qual filme você gostaria de assistir? (digite o número correspondente): ")

# Solicita a idade do usuário
idade = int(input("Qual é a sua idade? "))

# Verifica se a opção escolhida é válida
if opcao in filmes:
    titulo, classificacao = filmes[opcao]
    
    # Verifica se a idade do usuário permite assistir ao filme escolhido
    if idade >= classificacao:
        print(f"Você pode assistir a {titulo}. Aproveite o filme!")
    else:
        print(f"Desculpe, você não pode assistir a {titulo} porque sua idade é menor que {classificacao} anos.")
else:
    print("Opção inválida. Por favor, escolha um número da lista.")
