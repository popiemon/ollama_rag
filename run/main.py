from ollama_rag.chatpdf import ChatPDF


def main():
    chatpdf = ChatPDF()
    chatpdf.ingest("/workspace/data/GaN/1.126940.pdf")
    print(chatpdf.ask("What is GaN?"))


if __name__ == "__main__":
    main()
