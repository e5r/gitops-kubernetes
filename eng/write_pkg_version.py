"""Grava o número de versão do pacote

Lê o número de versão do arquivo 'pyproject.toml' na raiz do repositório e
grava o código Python que declara a variável `__version__ = '??'` no arquivo
`src/gitops_kubernetes/pkg_version.py`.
"""

import os
import sys
import eng_cli_util as cli

current_directory = os.path.dirname(__file__)
project_file_path = os.path.join(current_directory, '..', 'pyproject.toml')
version_file_path = os.path.join(current_directory, '..', 'src', 'gitops_kubernetes', 'pkg_version.py')

version_number = cli.get_pkg_version(project_file_path)

if(version_number == None):
    print('O arquivo', project_file_path, 'não tem a entrada [tool.poetry.version] esperada!')
    sys.exit(1)

with open(version_file_path, 'w', encoding='utf-8') as file:
    file.write(f'__version__ = "{version_number}"')
    file.write("\n")
