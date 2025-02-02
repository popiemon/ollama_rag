import os

from tqdm import tqdm

from ollama_rag.chatpdf import ChatPDF


def main():
    chatpdf = ChatPDF()
    pdf_dir = "/workspace/data/GaN"
    for filename in tqdm(os.listdir(pdf_dir)):
        if filename.endswith(".pdf"):
            try:
                chatpdf.learn(os.path.join(pdf_dir, filename))
                # chatpdf.ingest(os.path.join(pdf_dir, filename))
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                print("Continuing to the next document...")
                print("file:, ", filename)
                continue

    while True:
        query = input("Ask a question: ")
        if query == "exit":
            break
        print(chatpdf.ask(query))


if __name__ == "__main__":
    main()
