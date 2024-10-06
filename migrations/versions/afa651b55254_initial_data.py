"""initial data

Revision ID: afa651b55254
Revises: a6d3f7aa52eb
Create Date: 2024-10-06 02:39:05.469599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afa651b55254'
down_revision: Union[str, None] = 'a6d3f7aa52eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO kitties (color, age, description) VALUES ('черный', 3, 'сфинкс'),
    ('белый', 6, 'мейн-кун'),
    ('серый', 12, 'британская'),
    ('рыжий', 24, 'бурма'),
    ('серый', 15, 'сфинкс');
    """)


def downgrade() -> None:
    op.execute("""
    DELETE FROM kitties;
    """)
