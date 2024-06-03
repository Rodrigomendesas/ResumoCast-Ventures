# Documentação e Manual de Uso - Brainstorming Startups App

## Descrição
Esta aplicação CLI (Command Line Interface) utiliza a API da OpenAI para gerar conceitos inovadores de startups com base nas respostas fornecidas pelo usuário para uma série de perguntas. A aplicação coleta informações-chave sobre a startup e utiliza essas informações para gerar sugestões e ideias inovadoras. O objetivo é fazer algumas perguntas para ajudar o usuário a pensar e criar ideias disruptivas e personalizadas

## Pré-requisitos
Python 3.7+: certifique-se de ter o Python instalado na sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

Virtual Environment: recomenda-se o uso de um ambiente virtual para gerenciar as dependências.

OpenAI API Key: você precisa de uma chave de API da OpenAI. Você pode obter uma chave [aqui](https://platform.openai.com/api-keys)

## Configuração
### Passo 1: Clone o Repositório
Clone o repositório para o seu ambiente local:

    git clone https://github.com/Rodrigomendesas/ResumoCast-Ventures
    cd seu-repositorio

### Passo 2: Crie e Ative um Ambiente Virtual
Crie e ative um ambiente virtual:

    python -m venv myenv
    # No Windows
    myenv\Scripts\activate
    # No Unix ou macOS
    source myenv/bin/activate

### Passo 3: Instale as Dependências
Instale as dependências necessárias:

    pip install openai python-dotenv

### Passo 4: Configure as Variáveis de Ambiente
Crie um arquivo `.env` no diretório raiz do projeto e adicione sua chave de API da OpenAI:

    OPENAI_API_KEY=sua-chave-da-api-aqui
Observação: é importante usar `OPENAI_API_KEY` para sua variável de ambiente pois a biblioteca Python da OpenAI procura por essa chave por padrão. 

## Uso
Para executar a aplicação, certifique-se de que o ambiente virtual esteja ativado e execute o seguinte comando:

    python app.py

## Interação com a Aplicação
A aplicação fará uma série de perguntas para coletar informações sobre sua startup. Responda a cada pergunta conforme solicitado.

## Contribuindo
Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
