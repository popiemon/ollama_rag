import weave
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_ollama import ChatOllama

weave.init("ollama_rag")


class OllamaModel(weave.Model):
    """Ollama model."""

    model_name: str
    prompt_template: str = """
            <s> [INST] You are an assistant for question-answering tasks. Use the following context to answer the question.
            If you don't know the answer, simply say you don't know. Use a maximum of three sentences and be concise in your response. [/INST] </s>
            [INST] Question: {question}
            Context: {context}
            Answer: [/INST]
            """
    base_url: str
    context: VectorStoreRetriever

    @weave.op()
    def forward(self, sentence: str) -> str:
        """Forward pass.

        Parameters
        ----------
        sentence : str
            sentence

        Returns
        -------
        str
            response
        """
        ollama_model = ChatOllama(
            model=self.model_name,
            base_url=self.base_url,
        )
        prompt = PromptTemplate.from_template(
            template=self.prompt_template,
        )
        llm_chain = (
            {"context": self.context, "question": RunnablePassthrough()}
            | prompt
            | ollama_model
            | StrOutputParser()
        )
        return llm_chain.invoke(sentence)
