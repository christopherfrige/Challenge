# Challenge
Este repositório abriga o desafio proposto no arquivo docs/**problem.md**.

## Requisitos
- **[Python 3.6+](https://www.python.org/downloads/ "Link para download do Python")**

## Bibliotecas usadas
- Apenas bibliotecas built-in, não necessitando a instalação de nenhuma pelo pip.

## Ingestão de dados

Para fazer os testes com as informações do problema, utilizou-se um arquivo **.json** como banco de dados. Assim, foi feito a leitura e o processamento de seus dados, como é possível observar no script **data_loader.py**. 

Com isso, gerou-se objetos de acordo com as chaves principais _("motoboys", "stores", "orders")_ do arquivo, criando um objeto da classe Motoboy, Store, ou Order, respectivamente.

Tendo isso em vista, colocou-se esses objetos criados numa lista, separados por sua classificação, como forma de utilização nos outros scripts do problema.

## Execução

O script principal está contido no arquivo **main.py**, para rodá-lo verifique as instruções posteriores.

Como proposto no problema, para executar deve haver duas possibilidades:

    * Não passando nenhum motoboy (sem argumento)
        - Terá como output as informações de TODOS os motoboys.

<br>

    * Passando apenas o motoboy (com argumento)
        - O output será APENAS o motoboy com o ID escolhido;
        - No caso desse problema, os IDs vão do número 1 ao 5.

Dessa forma, cada uma dessas abordagens podem ser feitas da seguinte maneira no terminal:

**Sem argumento:**

    python main.py 

**Com argumento:**

    python main.py <motoboyID>

Após a execução, será visto um output semelhante a esse, para cada motoboy:

<img alt="Output após a execução do script para o motoboy com ID 1" src="https://i.imgur.com/fssxwQw.png">
