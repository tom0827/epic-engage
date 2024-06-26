"""alter submission

Revision ID: e69d7ac92afb
Revises: 6764af39864e
Create Date: 2022-12-20 17:08:59.040079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e69d7ac92afb'
down_revision = '6764af39864e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('comment', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.add_column('comment', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('comment', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.add_column('email_verification', sa.Column('submission_id', sa.Integer(), nullable=True))
    op.create_foreign_key('email_verification_submission_id_fkey', 'email_verification', 'submission', ['submission_id'], ['id'])
    op.add_column('submission', sa.Column('engagement_id', sa.Integer(), nullable=True))
    op.create_foreign_key('submission_engagement_id_fkey', 'submission', 'engagement', ['engagement_id'], ['id'], ondelete='CASCADE')

    op.execute('UPDATE submission SET engagement_id = (select survey.engagement_id from survey where survey.id = submission.survey_id) WHERE engagement_id IS NULL')
    op.alter_column('submission', 'engagement_id', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('submission_engagement_id_fkey', 'submission', type_='foreignkey')
    op.drop_column('submission', 'engagement_id')
    op.drop_index(op.f('ix_met_users_username'), table_name='met_users')
    op.create_index('ix_user_username', 'met_users', ['username'], unique=False)
    op.drop_constraint('email_verification_submission_id_fkey', 'email_verification', type_='foreignkey')
    op.drop_column('email_verification', 'submission_id')
    op.drop_column('comment', 'updated_by')
    op.drop_column('comment', 'created_by')
    op.drop_column('comment', 'updated_date')
    op.drop_column('comment', 'created_date')
    # ### end Alembic commands ###
