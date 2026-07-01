from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Enterprise Financial AI Platform"

    VERSION: str = "1.0"

    OPENAI_API_KEY: str = ""

    AZURE_OPENAI_API_KEY: str = ""

    AZURE_OPENAI_ENDPOINT: str = ""

    POSTGRES_HOST: str = "localhost"

    POSTGRES_DB: str = "finance_ai"

    LOG_LEVEL: str = "INFO"

    class Config:

        env_file = ".env"


settings = Settings()