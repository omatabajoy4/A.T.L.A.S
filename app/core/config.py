from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definimos los tipos de datos que esperamos de tu archivo .env
    ai_provider: str
    gemini_api_key: str
    database_url: str
    chroma_db_path: str
    api_host: str
    api_port: int
    atlas_secret_key: str

    # Le decimos a Pydantic que busque el archivo .env en la raíz del proyecto
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore" # Ignora variables extra si añadimos Spotify después
    )

# Instanciamos las configuraciones para usarlas en el resto de la app
settings = Settings()