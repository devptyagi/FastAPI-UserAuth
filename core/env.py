from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    DB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
