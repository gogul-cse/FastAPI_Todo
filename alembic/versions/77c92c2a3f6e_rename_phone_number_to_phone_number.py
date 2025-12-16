"""rename Phone_number to phone_number

Revision ID: 77c92c2a3f6e
Revises: 01b44ee054b2
Create Date: 2025-12-15 16:43:54.201624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77c92c2a3f6e'
down_revision: Union[str, Sequence[str], None] = '01b44ee054b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
