"""Initial table

Revision ID: e081d1952177
Revises: 
Create Date: 2024-05-03 17:59:23.712196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e081d1952177'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Numeric(precision=4, scale=2), nullable=False),
    sa.Column('wind_direction', sa.String(), nullable=False),
    sa.Column('wind_speed', sa.Numeric(precision=4, scale=2), nullable=False),
    sa.Column('pressure', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('precipitation', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_data')
    # ### end Alembic commands ###
