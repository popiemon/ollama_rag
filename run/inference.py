import os

from ollama_rag.chatpdf import ChatPDF


def main():
    localhost_ollama = os.getenv(
        "LOCALHOST_OLLAMA", "http://host.docker.internal:11434"
    )
    chatpdf = ChatPDF("phi4", localhost_ollama, "/workspace/db")

    while True:
        query = input("Ask a question: ")
        if query == "exit":
            break
        print(chatpdf.ask(query))
        print()


if __name__ == "__main__":
    main()
