"""create-tow-modle

Revision ID: 8ff92975e197
Revises: 2b1450d6e543
Create Date: 2024-03-06 15:06:00.347852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '8ff92975e197'
down_revision: Union[str, None] = '2b1450d6e543'
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
