import os

import hydra
from omegaconf import DictConfig
from tqdm import tqdm

from ollama_rag.chatpdf import ChatPDF
from ollama_rag.conf import Configuration


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg_yaml: DictConfig):
    cfg = Configuration.model_validate(cfg_yaml)
    localhost_ollama = "http://ollama_server:11434"
    if cfg.ollama_baseurl:
        localhost_ollama = cfg.ollama_baseurl
    chatpdf = ChatPDF(cfg.model, localhost_ollama, cfg.persist_directory)
    pdf_dir = cfg.pdf_dir
    for filename in tqdm(os.listdir(pdf_dir)):
        if filename.endswith(".pdf"):
            try:
                chatpdf.learn(os.path.join(pdf_dir, filename))
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
