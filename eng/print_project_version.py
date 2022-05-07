"""Imprime o número da versão do projeto

Este script é utilizado pelas rotinas de build, integração, entrega e outros
utilitários que precisam sincronizar o número da versão do código com o número
definido no arquivo 'pyproject.toml' na raiz do repositório.
"""

import os
import sys
import eng_cli_util as cli

current_directory = os.path.dirname(__file__)
project_file_path = os.path.join(current_directory, "..", "pyproject.toml")

version_number = cli.get_pkg_version(project_file_path)

if version_number == None:
    print("O arquivo", project_file_path, "não tem a entrada [tool.poetry.version] esperada!")
    sys.exit(1)

print(version_number)
