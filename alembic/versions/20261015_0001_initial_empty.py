"""initial empty migration

Revision ID: 0001
Revises:
Create Date: 2026-10-15
"""

from collections.abc import Sequence

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Empty baseline; tables arrive with the M1 schema migration."""


def downgrade() -> None:
    """Nothing to undo."""
