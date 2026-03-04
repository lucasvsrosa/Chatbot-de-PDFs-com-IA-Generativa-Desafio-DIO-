import os
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def process_pdfs(pdf_folder):
    text = ""
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def main():
    pdf_folder = "inputs"
    print("Processando documentos...")
    raw_text = process_pdfs(pdf_folder)
    
    if not raw_text:
        for filename in os.listdir(pdf_folder):
            if filename.endswith(".txt"):
                with open(os.path.join(pdf_folder, filename), "r") as f:
                    raw_text += f.read()
    
    if not raw_text:
        print("Nenhum conteúdo encontrado na pasta 'inputs'.")
        return

    text_chunks = get_text_chunks(raw_text)
    
    llm = ChatOpenAI(model_name="gpt-4.1-mini", temperature=0)
    
    template = """Responda à pergunta baseando-se apenas no seguinte contexto:
    {context}

    Pergunta: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    # Simulação de recuperação (usando todo o contexto para o exemplo simplificado)
    context = "\n\n".join(text_chunks)

    rag_chain = (
        {"context": lambda x: context, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    print("\nChatbot pronto! Digite sua pergunta (ou 'sair' para encerrar):")
    while True:
        try:
            query = input("> ")
        except EOFError:
            break
            
        if query.lower() in ["sair", "exit", "quit"]:
            break
        
        if not query.strip():
            continue
            
        response = rag_chain.invoke(query)
        print(f"\nResposta: {response}\n")

if __name__ == "__main__":
    main()
