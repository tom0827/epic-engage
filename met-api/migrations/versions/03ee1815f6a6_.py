"""Add avatar_filename to contact

Revision ID: 03ee1815f6a6
Revises: 9536f547cdd5
Create Date: 2022-11-10 14:21:02.844093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ee1815f6a6'
down_revision = '9536f547cdd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('avatar_filename', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'avatar_filename')
    # ### end Alembic commands ###
