"""create Phonenumber for user column

Revision ID: 01b44ee054b2
Revises: 
Create Date: 2025-12-11 14:25:27.085610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01b44ee054b2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.execute(" ALTER TABLE user ADD COLUMN Phone_number VARCHAR")
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
