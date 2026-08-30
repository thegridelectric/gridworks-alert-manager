"""Environment-backed settings for gridworks-alert-manager."""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_ENV_FILE = ".env"


class Settings(BaseSettings):
    telegram_bot_token: SecretStr = SecretStr("")
    # Always checked on the write route; the dev default pairs with
    # gwalert's. Production sets its own in .env.
    api_token: SecretStr = SecretStr("dev-alert-token")
    google_sheets_spreadsheet_id: str = ""
    google_credentials_file: str = "google-credentials.json"
    schedule_file: str = "google-sheet.json"
    alert_log_file: str = "alerts.csv"
    timezone: str = "America/New_York"
    max_alert_count: int = 6
    escalate_after_count: int = 3
    check_interval_seconds: int = 30
    reminder_interval_seconds: int = 5 * 60
    mute_clear_interval_seconds: int = 24 * 60 * 60
    # Loopback: only gwalert on this box may raise alerts. Reads that the
    # web front end needs go through a TLS proxy in front of the GET routes.
    host: str = "127.0.0.1"
    port: int = 8000

    model_config = SettingsConfigDict(
        env_prefix="ALERT_MANAGER_",
        env_nested_delimiter="__",
        env_file=DEFAULT_ENV_FILE,
        extra="ignore",
    )
