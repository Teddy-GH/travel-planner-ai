from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from app.vectorstore.db import (
    get_vector_store,
)

DOCUMENTS_DIR = "app/documents"

def load_documents():
    documents = []
    
    pdf_files  = Path(
        DOCUMENTS_DIR
    ).glob("*.pdf")
    
    for pdf in pdf_files:
        loader = PyPDFLoader(
            str(pdf)
        )
        
        documents.extend(
            loader.load()
        )    
        
    return documents
def split_documents(
    documents
):
    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )
    return splitter.split_documents(documents)    

def main():

    docs = load_documents()

    chunks = split_documents(
        docs
    )

    db = get_vector_store()

    db.add_documents(chunks)

    print(
        f"Stored {len(chunks)} chunks"
    )


if __name__ == "__main__":
    main()