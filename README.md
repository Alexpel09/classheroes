# Class Heroes

## Descrição
Este repositório contém um código em Python que implementa uma classe `Heroi` para representar diferentes tipos de heróis em um jogo ou simulação. Cada herói tem a capacidade de atacar um inimigo com um tipo específico de ataque.

## Estrutura do Projeto
O projeto está organizado da seguinte forma:
- `herois.py`: O arquivo principal que contém a definição da classe `Heroi` e a implementação do código.
- `README.md`: Este arquivo, que fornece uma visão geral do projeto, instruções de uso e documentação.
- `LICENSE`: O arquivo de licença que especifica os termos de uso do código.

## Uso
Para usar a classe `Heroi`, siga estas etapas:
1. Clone este repositório em seu ambiente local.
2. Importe a classe `Heroi` em seu próprio código Python.
3. Crie instâncias da classe `Heroi`, especificando o nome, idade e tipo do herói.
4. Chame o método `atacar()` de cada herói, passando outro objeto `Heroi` como argumento.

Exemplo de uso:
```python
from herois import Heroi

mago = Heroi("Preston", 1000, "mago")
guerreiro = Heroi("Capitão Caverna", 40, "guerreiro")

mago.atacar(guerreiro)

Contribuição
Se você quiser contribuir para este projeto, siga estas etapas:

Faça um fork deste repositório.
Crie uma nova branch com sua funcionalidade (git checkout -b minha-feature).
Faça commit de suas alterações (git commit -am 'Adicionar nova funcionalidade').
Faça push para a branch (git push origin minha-feature).
Crie um novo pull request.
Licença
Este projeto está licenciado sob a Licença MIT.

