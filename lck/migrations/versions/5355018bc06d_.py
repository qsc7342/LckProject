"""empty message

Revision ID: 5355018bc06d
Revises: 
Create Date: 2021-02-07 20:00:18.885305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5355018bc06d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lckplayer',
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('team', sa.Text(), nullable=False),
    sa.Column('line', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lckplayer')
    # ### end Alembic commands ###