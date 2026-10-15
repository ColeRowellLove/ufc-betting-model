from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect

from ufc_model.settings import get_settings

ROOT = Path(__file__).resolve().parents[1]


def test_upgrade_and_downgrade_on_sqlite(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    url = f"sqlite:///{(tmp_path / 'test.db').as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    get_settings.cache_clear()
    cfg = Config(str(ROOT / "alembic.ini"))
    cfg.set_main_option("script_location", str(ROOT / "alembic"))
    try:
        command.upgrade(cfg, "head")
        assert "alembic_version" in inspect(create_engine(url)).get_table_names()
        command.downgrade(cfg, "base")
    finally:
        get_settings.cache_clear()
