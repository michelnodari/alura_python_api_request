import requests
import pandas as pd
import base64
from math import ceil

class DadosRepositorios:

    def __init__(self,owner,git_token):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = git_token
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}
        
    def list_repositorios(self):
        repos_list = []

        # calculando a quantidade de paginas
        response = requests.get(f'{self.api_base_url}/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30) + 1

        for page_num in range(1,num_pages):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url,headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    
    def name_repos(self,repos_list):
        repo_name=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_name.append(repo['name'])
                except:
                    pass
        return repo_name
    
    def language_repos(self,repos_list):
        repo_language = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_language.append(repo['language'])
                except:
                    pass
        return repo_language
    
    
    def df_dados(self):
        repositorios = self.list_repositorios()
        name_rp = self.name_repos(repositorios)
        language_rp= self.language_repos(repositorios)
        
        dados = pd.DataFrame()
        dados['repository_name'] = name_rp
        dados['language'] = language_rp

        return dados

git_username = input("Informe o Username da Conta GitHub: ")

git_token = input("Informe sua access_token Token: ")

consulta_repositorio = DadosRepositorios(git_username,git_token)

resultado_consulta = consulta_repositorio.df_dados()

print(resultado_consulta)

# Verificar se o diretório existe e, se não, criar 

output_directory = '../projeto_Requests/data_lake' 

# Salvar o DataFrame no diretório 

resultado_consulta.to_csv(f'{output_directory}/{git_username}.csv') 

print(f"Resultados salvos em '{output_directory}/{git_username}.csv'")