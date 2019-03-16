"""empty message

Revision ID: f2994abbe6c0
Revises: 51191581c998
Create Date: 2019-03-16 13:22:23.983432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2994abbe6c0'
down_revision = '51191581c998'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('color', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('metric', sa.String(length=100), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    op.drop_table('activity')
    op.drop_table('goal')
    op.drop_table('user')
    # ### end Alembic commands ###
