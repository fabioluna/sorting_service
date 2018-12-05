**Requerimentos**

Python 3.5.6

**Como rodar**

Dentro da pasta onde foi clonado o repositório rode o seguinte comando:

- python sorting_service/\_\_init\_\_.py

Opcionalmente pode ser passado os seguintes parâmetros:

- -b: Json com a lista de livros a serem ordernados.

- -k: Json com as chaves e forma de ordenação desejada.

Os exemplos de Json podem ser encontrados dentro da pasta data.

**Testes**

Para rodar os testes podem execute o seguinte comando:

- python -m unittest tests/test_sorting_service.py