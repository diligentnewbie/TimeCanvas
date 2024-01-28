"""creat tables

Revision ID: 3dc479c359e5
Revises: 
Create Date: 2024-01-28 15:11:16.119863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dc479c359e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('baidu_name', sa.String(length=50), nullable=False),
    sa.Column('avatar_url', sa.String(length=200), nullable=False),
    sa.Column('access_token', sa.String(length=500), nullable=False),
    sa.Column('baidu_uk', sa.String(length=15), nullable=False),
    sa.Column('baidu_vip_type', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('baidu_uk')
    )
    op.create_index(op.f('ix_user_baidu_name'), 'user', ['baidu_name'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('classmates',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('nickname', sa.String(length=50), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('hometown', sa.String(length=100), nullable=True),
    sa.Column('hobby', sa.String(length=200), nullable=True),
    sa.Column('qq_number', sa.String(length=20), nullable=True),
    sa.Column('wx_number', sa.String(length=20), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('constellation', sa.String(length=5), nullable=True),
    sa.Column('dream', sa.String(length=200), nullable=True),
    sa.Column('graduation_message', sa.Text(), nullable=True),
    sa.Column('classmates_album_name', sa.String(length=50), nullable=True),
    sa.Column('classmates_avatar_name', sa.String(length=50), nullable=True),
    sa.Column('baidu_uk', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['baidu_uk'], ['user.baidu_uk'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classmates_id'), 'classmates', ['id'], unique=False)
    op.create_table('interesting_event',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('event_name', sa.String(length=50), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=False),
    sa.Column('event_description', sa.Text(), nullable=True),
    sa.Column('event_participant', sa.Text(), nullable=True),
    sa.Column('event_album_image', sa.String(length=50), nullable=True),
    sa.Column('event_album_name', sa.String(length=50), nullable=True),
    sa.Column('baidu_uk', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['baidu_uk'], ['user.baidu_uk'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interesting_event_id'), 'interesting_event', ['id'], unique=False)
    op.create_table('travel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('travel_album_name', sa.String(length=50), nullable=True),
    sa.Column('travel_theme', sa.String(length=50), nullable=False),
    sa.Column('travel_date', sa.DateTime(), nullable=False),
    sa.Column('travel_description', sa.Text(), nullable=True),
    sa.Column('travel_participant', sa.Text(), nullable=True),
    sa.Column('travel_place', sa.String(length=300), nullable=False),
    sa.Column('travel_album_image', sa.String(length=50), nullable=True),
    sa.Column('baidu_uk', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['baidu_uk'], ['user.baidu_uk'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('travel_album_name')
    )
    op.create_index(op.f('ix_travel_id'), 'travel', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_travel_id'), table_name='travel')
    op.drop_table('travel')
    op.drop_index(op.f('ix_interesting_event_id'), table_name='interesting_event')
    op.drop_table('interesting_event')
    op.drop_index(op.f('ix_classmates_id'), table_name='classmates')
    op.drop_table('classmates')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_baidu_name'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###