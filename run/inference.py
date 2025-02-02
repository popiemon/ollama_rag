from ollama_rag.chatpdf import ChatPDF


def main():
    chatpdf = ChatPDF()

    while True:
        query = input("Ask a question: ")
        if query == "exit":
            break
        print(chatpdf.ask(query))


if __name__ == "__main__":
    main()
