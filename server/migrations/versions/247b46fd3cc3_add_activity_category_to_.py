"""Add activity_category to MentalHealthInput

Revision ID: 247b46fd3cc3
Revises: b653e2bfc2b2
Create Date: 2024-10-14 08:01:20.998341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '247b46fd3cc3'
down_revision = 'b653e2bfc2b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mental_health_input', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity_category', sa.String(length=20), nullable=True))
        batch_op.alter_column('systolic',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=7),
               existing_nullable=False)
        batch_op.alter_column('diastolic',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=7),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mental_health_input', schema=None) as batch_op:
        batch_op.alter_column('diastolic',
               existing_type=sa.Float(precision=7),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('systolic',
               existing_type=sa.Float(precision=7),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.drop_column('activity_category')

    # ### end Alembic commands ###
