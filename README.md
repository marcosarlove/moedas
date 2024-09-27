PORTUGUÊS


Este projeto é um conversor de moedas que utiliza a API da Moeda para obter as taxas de câmbio mais recentes. O programa pode ser executado em modo de linha de comando e oferece várias funcionalidades, como listar códigos de moedas, verificar a existência de um código, pesquisar códigos e converter valores entre diferentes moedas.


Funcionalidades

- Listar Códigos de Moedas: Exibe todos os códigos de moedas disponíveis para conversão.
- Verificar Existência de um Código: Verifica se um código de moeda específico existe.
- Pesquisar Códigos: Permite a pesquisa de códigos de moeda com base em uma string fornecida.
- Converter Valores: Converte um valor de uma moeda para outra com base nas taxas de câmbio atuais.
- Atualização Automática: O programa tenta buscar dados online e, caso não consiga, utiliza dados armazenados localmente.


Pré-requisitos

- Python 3.x
- Bibliotecas:
  - requests
  - json
  - os
  - argparse
  - re

Você pode instalar a biblioteca requests usando o seguinte comando:

pip install requests


Uso

O programa pode ser executado diretamente no terminal. Aqui estão alguns exemplos de como usá-lo:

▎Listar Códigos de Moedas

python moedas.py --list
ou
python moedas.py -l


▎Verificar Existência de um Código

python moedas.py --exists USD
ou
python moedas.py -e usd


▎Pesquisar Códigos

python moedas.py --search USD
ou
python moedas.py -e usd


▎Converter Moedas

python moedas.py --convert 100USD --to EUR
ou
python moedas.py -c 100usd -t eur


▎Estrutura do Código

O código é dividido em várias funções que gerenciam diferentes aspectos do conversor:

- listAllCodes(): Lista todos os códigos disponíveis.
- exists(code): Verifica se um código existe.
- search(code): Pesquisa códigos com base na entrada do usuário.
- convert(from_, to): Realiza a conversão entre moedas.
- printLastUpdate(): Imprime a data da última atualização das taxas.

▎Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema (issue) ou enviar um pull request.










INGLÊS

▎Currency Converter

This project is a currency converter that uses the Moeda API to obtain the latest exchange rates. The program can be run in command-line mode and offers various functionalities, such as listing currency codes, checking the existence of a code, searching for codes, and converting values between different currencies.

▎Features

- List Currency Codes: Displays all available currency codes for conversion.
- Check Code Existence: Checks if a specific currency code exists.
- Search Codes: Allows searching for currency codes based on a provided string.
- Convert Values: Converts a value from one currency to another based on current exchange rates.
- Automatic Update: The program attempts to fetch data online and, if it fails, uses locally stored data.

▎Prerequisites

- Python 3.x
- Libraries:
  - requests
  - json
  - os
  - argparse
  - re

You can install the requests library using the following command:

pip install requests


▎Usage

The program can be executed directly from the terminal. Here are some examples of how to use it:

▎List Currency Codes

python moedas.py --list
or
python moedas.py -l


▎Check Code Existence

python moedas.py --exists USD
or
python moedas.py -e usd


▎Search Codes

python moedas.py --search USD
or
python moedas.py -s usd


▎Convert Currencies

python moedas.py --convert 100USD --to EUR
or
python moedas.py -c 100usd -t eur


▎Code Structure

The code is divided into several functions that manage different aspects of the converter:

- listAllCodes(): Lists all available codes.
- exists(code): Checks if a code exists.
- search(code): Searches for codes based on user input.
- convert(from_, to): Performs conversion between currencies.
- printLastUpdate(): Prints the date of the last update of rates.

▎Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.
