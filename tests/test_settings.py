from pathlib import Path

import pytest

from ufc_model.settings import Settings, get_settings


def test_defaults_point_at_compose_postgres(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)  # no .env here
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("ODDS_API_KEY", raising=False)
    settings = Settings()
    assert settings.database_url.startswith("postgresql+psycopg://ufc:ufc@localhost:5432/")
    assert settings.odds_api_key is None


def test_env_overrides(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://u:p@db:5432/x")
    monkeypatch.setenv("ODDS_API_KEY", "secret-key")
    settings = Settings()
    assert settings.database_url.endswith("@db:5432/x")
    assert settings.odds_api_key is not None
    assert settings.odds_api_key.get_secret_value() == "secret-key"
    assert "secret-key" not in repr(settings)


def test_get_settings_is_cached() -> None:
    assert get_settings() is get_settings()
