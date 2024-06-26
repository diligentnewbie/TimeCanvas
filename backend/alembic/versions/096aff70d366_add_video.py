"""add_video

Revision ID: 096aff70d366
Revises: 80c722ce54d4
Create Date: 2024-04-15 10:56:11.618858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '096aff70d366'
down_revision: Union[str, None] = '80c722ce54d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
