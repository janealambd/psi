"""Add is system to role model

Revision ID: 2a4243d9cd8c
Revises: ad98a504518a
Create Date: 2017-01-07 20:52:05.186304

"""

# revision identifiers, used by Alembic.
revision = '2a4243d9cd8c'
down_revision = 'ad98a504518a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('is_system', sa.Boolean(), server_default='1'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'is_system')
    # ### end Alembic commands ###
