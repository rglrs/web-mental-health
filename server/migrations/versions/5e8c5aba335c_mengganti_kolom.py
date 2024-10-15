"""Mengganti kolom

Revision ID: 5e8c5aba335c
Revises: 563f9f584f26
Create Date: 2024-09-29 20:22:39.726889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e8c5aba335c'
down_revision = '563f9f584f26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mental_health_input', schema=None) as batch_op:
        batch_op.alter_column('systolic',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=7),
               existing_nullable=False)
        batch_op.alter_column('diastolic',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=7),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('gender', postgresql.ENUM('male', 'female', name='gender'), nullable=False))
        batch_op.drop_column('kelamin')
        batch_op.drop_column('usia')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usia', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('kelamin', postgresql.ENUM('laki-laki', 'perempuan', name='gender'), autoincrement=False, nullable=False))
        batch_op.drop_column('gender')
        batch_op.drop_column('age')

    with op.batch_alter_table('mental_health_input', schema=None) as batch_op:
        batch_op.alter_column('diastolic',
               existing_type=sa.Float(precision=7),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('systolic',
               existing_type=sa.Float(precision=7),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###