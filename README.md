# Dns_mouse_tool
DNS_Mouse é uma ferramenta simples e eficiente desenvolvida em Python para realizar varredura de subdiretórios em servidores web. Ela automatiza a descoberta de possíveis diretórios acessíveis publicamente em um site ou servidor, similar ao funcionamento do Gobuster. A ferramenta pode ser útil para testes de penetração e auditorias de segurança, ajudando a identificar áreas sensíveis e vulneráveis de um servidor.

Características:

Varredura de subdiretórios usando uma wordlist personalizada.

Exibe apenas diretórios encontrados (HTTP 200).

Mensagens de sucesso em verde para facilitar a visualização.

Suporte para wordlists personalizadas.

Cabeçalho estilizado para uma interface amigável.

Utiliza HTTP GET para acessar os subdiretórios.

Tratamento de exceções para erros de conexão.

Como Funciona:
A ferramenta percorre uma lista de subdiretórios (wordlist) fornecida pelo usuário, tenta acessá-los via requisições HTTP e identifica quais estão acessíveis. Se o subdiretório retornar um código de status 200, o diretório é considerado existente e acessível. Outros códigos de status, como 403 ou 404, são ignorados ou indicados como proibidos.

Requisitos:

Python 3.x
Bibliotecas: requests, argparse
Como Usar:

Clone o repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/DNS_Mouse.git
Instale as dependências:

bash
Copiar código
pip install requests

Execute a ferramenta:
python Dns_mouse.py http://example.com /caminho/para/wordlist.txt

Exemplo de Execução:
python Dns_mouse.py http://example.com wordlist.txt

Saída esperada:
#########################################
#         Subdir Scanner Tool           #
#        Criado por: Seu Nome           #
#########################################
[*] Iniciando varredura em: http://example.com

