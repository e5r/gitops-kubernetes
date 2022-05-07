Como contribuir?
================

Fico feliz por ler isso, porque precisamos de desenvolvedores voluntários para ajudar este projeto
a se concretizar. Caso ainda não tenha feito, envie um email para `erlimar@gmail.com` e nos diga
como você deseja ajudar que acharemos um trabalho pra você.

## Eis aqui por onde você pode começar

* Faça um fork do repositório
* Use o [Poetry](https://python-poetry.org) e tenha seu ambiente dev pronto
* Faça suas alterações e nos envie um PR

Simples assim!

## Quando estiver codificando

* Codifique na `master`
* Tudo deve ter teste unitário
* Usamos [Black](https://github.com/psf/black) para facilitar estilo de código
* Usamos [pre-commit](https://pre-commit.com/) para facilitar integração contínua

> Esteja familiarizado com isso!

### Inicialize assim

```console
$ poetry install
$ # ative seu virtualenv como preferir, e já no virtualenv faça:
$ pre-commit install
$ # Codifique!
$ pre-commit run --all-files # Sugestão: antes de cada commit
```
