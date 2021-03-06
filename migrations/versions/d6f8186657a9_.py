"""empty message

Revision ID: d6f8186657a9
Revises: 
Create Date: 2021-02-11 20:58:42.891138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6f8186657a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('idx', sa.String(length=16), nullable=False),
    sa.Column('client_id', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=96), nullable=False),
    sa.Column('register', sa.DateTime(), nullable=False),
    sa.Column('token', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('idx')
    )
    op.create_table('client',
    sa.Column('idx', sa.String(length=36), nullable=False),
    sa.Column('secret', sa.String(length=96), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('activate', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('idx')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    op.drop_table('auth')
    # ### end Alembic commands ###
