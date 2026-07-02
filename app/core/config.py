from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definimos aquí solo las variables que el código necesita obligatoriamente
    gemini_api_key: str
    
    # Configuramos Pydantic para que ignore variables extra en el .env
    # y que busque el archivo .env en la raíz del proyecto
    model_config = SettingsConfigDict(
        env_file=".env", 
        extra='ignore'
    )

# Instanciamos los settings para importarlos desde cualquier parte del código
settings = Settings()