import os

import hydra
from omegaconf import DictConfig

from ollama_rag.chatpdf import ChatPDF
from ollama_rag.conf import Configuration


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg_yaml: DictConfig):
    cfg = Configuration.model_validate(cfg_yaml)
    localhost_ollama = os.getenv(
        "LOCALHOST_OLLAMA", "http://host.docker.internal:11434"
    )
    if cfg.ollama_baseurl:
        localhost_ollama = cfg.ollama_baseurl
    chatpdf = ChatPDF(cfg.model, localhost_ollama, cfg.persist_directory)

    while True:
        query = input("Ask a question: ")
        if query == "exit":
            break
        print(chatpdf.ask(query))
        print()


if __name__ == "__main__":
    main()
