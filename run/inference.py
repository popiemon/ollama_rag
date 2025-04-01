import hydra
from omegaconf import DictConfig

from ollama_rag.chatpdf import ChatPDF
from ollama_rag.conf import Configuration


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg_yaml: DictConfig):
    cfg = Configuration.model_validate(cfg_yaml)
    ollama_server = "http://ollama_server:11434"
    if cfg.ollama_baseurl:
        ollama_server = cfg.ollama_baseurl
    chatpdf = ChatPDF(cfg.model, ollama_server, cfg.persist_directory)

    while True:
        query = input("Ask a question: ")
        if query == "exit":
            break
        print(chatpdf.ask(query))
        print()


if __name__ == "__main__":
    main()
