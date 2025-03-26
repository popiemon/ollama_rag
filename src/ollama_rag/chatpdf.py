import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata

from ollama_rag.model import OllamaModel


class ChatPDF:
    """PDF Chatbot that uses a PDF document to answer questions."""

    def __init__(
        self,
        ollama_model: str,
        base_url: str,
        persist_directory: str,
        template: str = """
            <s> [INST] You are an assistant for question-answering tasks. Use the following context to answer the question.
            If you don't know the answer, simply say you don't know. Use a maximum of three sentences and be concise in your response. [/INST] </s>
            [INST] Question: {question}
            Context: {context}
            Answer: [/INST]
            """,
    ) -> None:
        """PDF Chatbot that uses a PDF document to answer questions.

        Parameters
        ----------
        model : str
            model name
        base_url : str
            ollama base url
        persist_directory : str
            directory to persist the PDF documents
        template : str, optional
            template for the prompt, by default
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024, chunk_overlap=100
        )
        persist_directory = persist_directory
        client = chromadb.PersistentClient(path=persist_directory)
        self.db = Chroma(
            collection_name="pdfs",
            embedding_function=FastEmbedEmbeddings(),
            client=client,
        )
        self.retriever = self.db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )
        self.model = OllamaModel(
            model_name=ollama_model,
            base_url=base_url,
            context=self.retriever,
            prompt_template=template,
        )
        # self.chain = (
        #     {"context": self.retriever, "question": RunnablePassthrough()}
        #     | self.prompt
        #     | self.ollama_model
        #     | StrOutputParser()
        # )

    def learn(self, pdf_file_path: str) -> None:
        """Learn from a PDF document.

        Parameters
        ----------
        pdf_file_path : str
            path to the PDF file
        """
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)
        self.db.add_documents(
            documents=chunks,
            embeddings=FastEmbedEmbeddings(),
        )

    def ask(self, query: str) -> str:
        """Ask a question.

        Parameters
        ----------
        query : str
            question

        Returns
        -------
        str
            answer
        """
        return self.model.forward(query)

    def clear(self) -> None:
        """Clear the PDF Chatbot."""
        self.vector_store = None
        self.retriever = None
        self.chain = None
