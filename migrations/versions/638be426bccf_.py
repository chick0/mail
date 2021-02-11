"""empty message

Revision ID: 638be426bccf
Revises: cc34b5701786
Create Date: 2021-02-11 20:34:43.875728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638be426bccf'
down_revision = 'cc34b5701786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('activate', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'activate')
    # ### end Alembic commands ###
