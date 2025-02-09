"""update contact model

Revision ID: b36e4e227e5d
Revises: 1136f866487c
Create Date: 2024-03-18 19:59:45.976033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36e4e227e5d'
down_revision = '1136f866487c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=False))
        batch_op.drop_constraint('contact_name_key', type_='unique')
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('contact_name_key', ['name'])
        batch_op.drop_column('phone_number')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
