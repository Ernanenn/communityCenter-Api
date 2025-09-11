Projeto de Testes e Automação - Community Center API

Este repositório contém os artefactos de teste para a Community Center API, desenvolvidos como parte de um processo seletivo para a área de Quality Assurance. O objetivo principal é validar a funcionalidade, a robustez e a fiabilidade da API, que foi projetada para gerir centros de apoio comunitário durante situações de emergência.

📜 Visão Geral do Projeto
O projeto abrange um ciclo completo de testes de API, incluindo:
Planeamento: Criação de um roteiro de testes detalhado com base no Documento de Requisitos do Produto e na especificação Swagger.
Automação Nível 1 (Postman): Implementação de testes automatizados para a maioria dos cenários, focando em validações de status, schemas de resposta e fluxos de trabalho.
Automação Nível 2 (Python/PyTest): Desenvolvimento de scripts de automação para cenários com lógica de negócio mais complexa, demonstrando uma abordagem de teste via código.
Análise Crítica: Elaboração de um relatório com os bugs encontrados e sugestões de melhoria para o produto.

🎯 Funcionalidades Testadas
Os testes cobrem todas as principais funcionalidades da API, incluindo:
Gestão de Centros (CRUD):
Cadastro de novos centros comunitários.
Listagem paginada e ordenada de centros.
Remoção de centros existentes.

Regras de Negócio:
Atualização da ocupação atual de um centro.
Validação de limites (ex: ocupação vs. capacidade máxima).

Lógica de Intercâmbio:
Troca de recursos entre dois centros.
Validação da regra de equilíbrio de pontos.
Validação da regra de exceção para centros com mais de 90% de ocupação.

Relatórios:
Relatório de centros com alta ocupação.
Relatório de média de recursos por centro.
Consulta ao histórico de negociações.

🛠️ Tecnologias Utilizadas
Automação de API: Postman
Automação via Código: Python 3.11
Framework de Teste: PyTest
Biblioteca HTTP: Requests
Controlo de Versão: Git & GitHub

🚀 Como Executar os Testes
Para executar os testes, siga os passos abaixo.

Pré-requisitos
Postman Desktop Agent

Python 3.8+

Git

1. Configuração do Ambiente
Primeiro, clone o repositório para a tua máquina local:

git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>

a) Configurar o Postman
Abre o Postman e importa a collection Community Center API.postman_collection.json que se encontra neste repositório.
Cria um novo Ambiente no Postman (clica no ícone de olho no canto superior direito > "Add"). Podes dar-lhe o nome de Community Center Env.

Dentro do novo ambiente, adiciona as seguintes variáveis:
baseUrl: https://cj98hakmf0.execute-api.us-east-1.amazonaws.com/phoebus-apps
apiKey: COLE_A_SUA_CHAVE_DE_API_FORNECIDA_AQUI

b) Configurar o Ambiente Python (para os testes com PyTest)
É altamente recomendado usar um ambiente virtual (venv) para isolar as dependências do projeto.

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

Nota: O ficheiro requirements.txt contém as bibliotecas pytest e requests.

2. Execução dos Testes
a) Executar com o Postman
Com o Postman aberto, certifica-te de que a collection "Community Center API" e o ambiente "Community Center Env" estão selecionados.
Clica nos três pontos ao lado do nome da collection e seleciona "Run collection".
Na janela do Collection Runner, podes selecionar a ordem dos testes ou simplesmente clicar no botão "Run Community Center API" para executar todos.
Os resultados, incluindo as asserções de cada teste, serão exibidos no final da execução.

b) Executar com PyTest
Importante: Antes de executar, abre o ficheiro test_community_center_api.py e insere a tua apiKey na variável API_KEY.
Certifica-te de que o teu ambiente virtual está ativado.
No terminal, a partir da raiz do projeto, executa o seguinte comando:

pytest -v

O comando -v (verbose) irá mostrar um output detalhado de cada teste executado.

📂 Estrutura do Repositório
.
├── artefacts/
│   ├── Roteiro_de_Testes.xlsx
│   └── Relatorio_Bugs_e_Melhorias.pdf
├── test_community_center_api.py
├── Community Center API.postman_collection.json
└── README.md
