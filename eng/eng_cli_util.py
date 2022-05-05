"""Utilitário para scripts de engenharia no modelo CLI"""

import tomli

def get_pkg_version(project_file_path):
    with open(project_file_path, 'rb') as file:
        toml_dict = tomli.load(file)

        # Conferindo se o arquivo TOML tem a entrada [tool.poetry.version] esperada
        if('tool' not in toml_dict or
        'poetry' not in toml_dict['tool'] or
        'version' not in toml_dict['tool']['poetry']):
            return None

        return toml_dict['tool']['poetry']['version']
