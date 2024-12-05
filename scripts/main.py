from classe_DadosRepositorios import DadosRepositorios

git_username = input("Informe o Username da Conta GitHub: ")

git_token = input("Informe sua access_token Token: ")

consulta_repositorio = DadosRepositorios(git_username,git_token)

resultado_consulta = consulta_repositorio.df_dados()

print(resultado_consulta)


output_directory = '../projeto_Requests/data_lake' 

# Salvar o DataFrame no diretório 

resultado_consulta.to_csv(f'{output_directory}/{git_username}.csv') 

print(f"Resultados salvos em '{output_directory}/{git_username}.csv'")