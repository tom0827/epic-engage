""" Add rich description to subscribe_item table

Revision ID: 3a88de1e3e7f
Revises: 155c64768a99
Create Date: 2023-09-08 09:34:06.274642

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3a88de1e3e7f'
down_revision = '155c64768a99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribe_item', sa.Column('rich_description', sa.Text(), nullable=True))
    op.execute('UPDATE subscribe_item SET rich_description = description')
    op.execute('UPDATE subscribe_item SET description = NULL')    
    op.alter_column('subscribe_item', 'call_to_action_type',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.alter_column('subscribe_item', 'call_to_action_type',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    op.drop_column('subscribe_item', 'rich_description')

    # ### end Alembic commands ###
