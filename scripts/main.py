from classe_DadosRepositorios import DadosRepositorios
from classe_GerenciaRepositorios import GerenciaRepositorios

# Solicitar username e token do usuário
git_username_repos = input("Informe o Userncleaame da Conta GitHub que você deseja Consultar os Repositórios: ")
git_token = input("Informe sua chave Token: ")

consulta_repositorio = DadosRepositorios(git_username_repos,git_token)

resultado_consulta = consulta_repositorio.df_dados()

print(resultado_consulta)


output_directory = '../projeto_Requests/data_lake' 

# Salvar o DataFrame no diretório 

resultado_consulta.to_csv(f'{output_directory}/{git_username_repos}.csv') 

print(f"Resultados salvos em '{output_directory}/{git_username_repos}.csv'")

git_username_upload = input("Informe o Username da Conta GitHub que você deseja Fazer o Upload dos Arquivos de Repositório: ")

# Criando a instância do objeto GerenciaRepositorios
novo_repo = GerenciaRepositorios(git_username_upload, git_token)

# Criando o repositório (descomente se necessário)
nome_repo = 'alura_python_api_request'
# novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, f'{git_username_repos}.csv', f'{output_directory}/{git_username_repos}.csv')
