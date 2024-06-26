"""video_up_column5

Revision ID: dc8d228c33e7
Revises: aff283eb49c9
Create Date: 2024-04-17 21:58:39.523210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'dc8d228c33e7'
down_revision: Union[str, None] = 'aff283eb49c9'
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
