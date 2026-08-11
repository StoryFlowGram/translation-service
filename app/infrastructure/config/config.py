from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    gemini_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        extra="ignore" 
    )

settings = Setting()