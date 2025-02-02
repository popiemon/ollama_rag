from pydantic import BaseModel


class Configuration(BaseModel):
    model: str
    ollama_baseurl: str | None
    pdf_dir: str
    persist_directory: str
