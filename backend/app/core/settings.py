from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================
    # Application Configuration
    # ==========================
    app_name: str
    app_version: str
    environment: str
    host: str
    port: int

    # ==========================
    # Database Configuration
    # ==========================
    database_url: str

    # ==========================
    # GitHub Configuration
    # ==========================
    github_token: str = ""
    github_owner: str = ""
    github_repository: str = ""

    # ==========================
    # Jira Configuration
    # ==========================
    jira_base_url: str = ""
    jira_email: str = ""
    jira_api_token: str = ""

    # ==========================
    # Google Cloud Configuration
    # ==========================
    google_cloud_project: str = ""
    google_application_credentials: str = ""

    # ==========================
    # Gemini Configuration
    # ==========================
    gemini_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()