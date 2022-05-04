"""Imprime o número da versão do projeto

Este script é utilizado pelas rotinas de build, integração, entrega e outros
utilitários que precisam sincronizar o número da versão do código com o número
definido no arquivo 'pyproject.toml' na raiz do projeto.
"""

import sys
import tomli

def show_usage():
    print('Usage:', sys.argv[0], '{pyproject_toml_file}')

if(len(sys.argv) != 2):
    show_usage()
    sys.exit(1)

with open(sys.argv[1], 'rb') as file:
    toml_dict = tomli.load(file)

    # Conferindo se o arquivo TOML tem a entrada [tool.poetry.version] esperada
    if('tool' not in toml_dict or
       'poetry' not in toml_dict['tool'] or
       'version' not in toml_dict['tool']['poetry']):
        print('O arquivo', sys.argv[1], 'não tem a entrada [tool.poetry.version] esperada!')
        sys.exit(2)

    # Imprime o número da versão
    print(toml_dict['tool']['poetry']['version'])
