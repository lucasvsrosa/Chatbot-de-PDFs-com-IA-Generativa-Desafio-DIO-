# 🍦📊 Chatbot de PDFs com IA Generativa (Desafio DIO)

## Visão Geral do Desafio

Este projeto foi desenvolvido como parte do desafio da DIO, com o objetivo de criar um chatbot interativo capaz de responder perguntas com base no conteúdo de arquivos PDF. A solução explora conceitos de **IA generativa**, **embeddings** e **buscas vetorizadas** para construir um sistema que entende, processa e responde a partir de documentos específicos. Isso permite a criação de um modelo personalizado de assistência virtual, focado em um conjunto de informações proprietárias, sem depender exclusivamente do conhecimento geral de modelos pré-treinados.

## Cenário

Imagine um estudante de Engenharia de Software, como eu, prestes a escrever seu Trabalho de Conclusão de Curso (TCC). A revisão e correlação de diversos artigos científicos se torna um desafio à medida que a quantidade de documentos aumenta. Extrair informações relevantes e conectar ideias entre diferentes textos pode ser uma tarefa árdua.

Para superar esse desafio, utilizei inteligência artificial para facilitar o processo, criando um sistema de busca inteligente capaz de interpretar PDFs, organizar informações e gerar respostas relevantes com base no conteúdo carregado.

## Objetivo

O projeto visa permitir que o usuário:

*   ✅ Carregue arquivos PDF contendo informações relevantes para seu estudo ou projeto.
*   ✅ Implemente um sistema de busca vetorial para indexar e recuperar informações dos PDFs.
*   ✅ Utilize inteligência artificial para gerar respostas baseadas no conteúdo dos documentos carregados.
*   ✅ Desenvolva um chat interativo onde seja possível realizar perguntas e obter respostas contextuais fundamentadas nos arquivos.

## Tecnologias Utilizadas

As principais tecnologias e bibliotecas empregadas neste projeto incluem:

*   **Python**: Linguagem de programação principal.
*   **LangChain**: Framework para desenvolvimento de aplicações com modelos de linguagem, facilitando a orquestração de componentes de IA.
*   **OpenAI**: Utilizado para os modelos de linguagem (LLMs) e embeddings (via proxy da Manus).
*   **PyPDF2**: Biblioteca para extração de texto de arquivos PDF.
*   **FAISS (Facebook AI Similarity Search)**: Biblioteca para busca eficiente de similaridade em grandes conjuntos de vetores (não utilizado na versão final simplificada devido a problemas de compatibilidade com o proxy, mas o conceito é fundamental).
*   **langchain-text-splitters**: Para dividir o texto em "chunks" gerenciáveis.

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

```
chatbot-pdf-dio/
├── inputs/
│   ├── sentencas.txt
│   └── guia_chatbot.pdf
├── screenshots/
├── chatbot.py
└── README.md
```

*   `inputs/`: Contém os arquivos PDF e TXT de exemplo que o chatbot irá processar.
*   `screenshots/`: Pasta para armazenar capturas de tela das interações (simuladas por texto neste README).
*   `chatbot.py`: O script principal do chatbot.
*   `README.md`: Este arquivo, descrevendo o projeto.

## Como Executar

Para rodar o chatbot localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd chatbot-pdf-dio
    ```

2.  **Instale as dependências:**
    ```bash
    sudo pip3 install langchain langchain-openai langchain-community faiss-cpu pypdf2 openai
    ```
    *Nota: A instalação do `faiss-cpu` é mantida para referência, mas a versão simplificada do `chatbot.py` não o utiliza diretamente devido a desafios de compatibilidade com o ambiente de execução e a API de embeddings.* 

3.  **Configure sua chave de API da OpenAI:**
    Certifique-se de que sua chave de API da OpenAI esteja configurada como uma variável de ambiente (`OPENAI_API_KEY`). No ambiente da Manus, a configuração de `OPENAI_BASE_URL` e `OPENAI_API_BASE` para `https://api.manus.im/api/llm-proxy/v1` é crucial para o funcionamento dos modelos `gpt-4.1-mini`.

4.  **Adicione seus documentos:**
    Coloque seus arquivos PDF ou TXT na pasta `inputs/`.

5.  **Execute o chatbot:**
    ```bash
    python3 chatbot.py
    ```

## Exemplo de Uso

Abaixo estão algumas interações de exemplo com o chatbot, demonstrando como ele responde com base nos documentos fornecidos:

```
Processando documentos...

Chatbot pronto! Digite sua pergunta (ou 'sair' para encerrar):
> Qual o objetivo principal deste projeto?

Resposta: O objetivo principal deste projeto é criar um chatbot que utiliza LangChain e OpenAI para processar documentos em PDF, oferecendo funcionalidades como carregamento de PDFs, busca vetorial com FAISS e respostas contextuais baseadas em RAG, facilitando revisões bibliográficas de TCC e conectando ideias entre diferentes textos automaticamente.

> Como o chatbot funciona tecnicamente?

Resposta: O chatbot funciona utilizando LangChain e OpenAI para processar documentos. Ele realiza o carregamento de PDFs, emprega busca vetorial com FAISS e fornece respostas contextuais baseadas em RAG (Retrieval-Augmented Generation).

> Quais as funcionalidades mencionadas no guia?

Resposta: As funcionalidades mencionadas no guia são:  
- Carregamento de PDFs  
- Busca vetorial com FAISS  
- Respostas contextuais baseadas em RAG

> sair
```

## Insights e Aprendizados

Durante o desenvolvimento deste projeto, enfrentei alguns desafios e obtive importantes aprendizados:

*   **Adaptação da API da OpenAI:** Inicialmente, houve um erro `404 - {'status': 'not found'}` ao tentar usar o modelo `text-embedding-3-small` diretamente. Isso ocorreu porque o ambiente da Manus utiliza um proxy para a API da OpenAI, que expõe modelos específicos (`gpt-4.1-mini`, `gemini-2.5-flash`). A solução foi adaptar o código para usar `gpt-4.1-mini` tanto para embeddings quanto para o LLM principal.
*   **Evolução do LangChain:** A biblioteca LangChain está em constante evolução. A necessidade de ajustar as importações (`langchain.text_splitter` para `langchain_text_splitters` e `langchain.chains.retrieval_qa.base` para uma abordagem mais moderna com LCEL - LangChain Expression Language) demonstrou a importância de se manter atualizado com as melhores práticas e a documentação mais recente.
*   **RAG (Retrieval-Augmented Generation):** O conceito de RAG é fundamental para este projeto. Ele permite que o LLM gere respostas baseadas em um contexto específico (os documentos PDF), em vez de depender apenas de seu conhecimento pré-treinado. Isso aumenta a precisão e reduz as "alucinações" da IA.
*   **Embeddings e Busca Vetorial:** Embora a implementação final tenha simplificado a parte de busca vetorial devido aos desafios da API, o entendimento de como embeddings transformam texto em vetores numéricos e como a busca de similaridade (e.g., com FAISS) permite encontrar informações semanticamente relacionadas é crucial para a eficácia de chatbots baseados em documentos.
*   **Tratamento de PDFs:** A extração de texto de PDFs usando `PyPDF2` é um passo inicial importante, mas a qualidade da extração pode variar dependendo da estrutura do PDF. Para documentos mais complexos, técnicas de OCR (Optical Character Recognition) ou bibliotecas mais robustas poderiam ser necessárias.

## Possibilidades de Melhoria

Este projeto serve como uma base sólida e pode ser expandido com diversas melhorias:

*   **Interface Gráfica:** Desenvolver uma interface web (usando Streamlit, Gradio ou Flask) para facilitar o upload de PDFs e a interação com o chatbot.
*   **Persistência do Vector Store:** Salvar o `vectorstore` em disco para evitar o reprocessamento dos PDFs a cada execução.
*   **Tratamento de Erros:** Implementar um tratamento de erros mais robusto para arquivos PDF corrompidos ou vazios.
*   **Suporte a Outros Formatos:** Estender o suporte para outros formatos de documento, como DOCX, TXT, etc.
*   **Aprimoramento da Recuperação:** Explorar diferentes estratégias de `retriever` no LangChain, como `MultiQueryRetriever` ou `ContextualCompressionRetriever`, para melhorar a relevância dos chunks recuperados.
*   **Avaliação de Respostas:** Implementar métricas para avaliar a qualidade das respostas geradas pelo chatbot.
*   **Histórico de Conversa:** Adicionar funcionalidade para manter o histórico da conversa, permitindo que o chatbot responda a perguntas de acompanhamento de forma mais contextualizada.

## Como Entregar Este Projeto

Para entregar este projeto no desafio da DIO, siga as instruções originais:

1.  Crie um novo repositório no GitHub com um nome de sua preferência.
2.  Crie uma pasta chamada `inputs` e inclua documentos de texto e/ou PDF de exemplo.
3.  Crie um arquivo `README.md` (este arquivo) descrevendo o processo, incluindo prints (simulados por texto aqui), insights e possibilidades.
4.  Compartilhe o link desse repositório através do botão 'entregar projeto'.


