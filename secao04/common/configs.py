from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais
    """

    API_V1_STR: str = '/api/v1'
    DATABASE_URL: str = 'sqlite:///faculdade.db'
    DATABASE_BASEMODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
