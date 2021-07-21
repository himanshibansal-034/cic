"""empty message

Revision ID: c9fd0d38ffca
Revises: 
Create Date: 2021-06-26 15:09:46.585323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9fd0d38ffca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('announcement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stage', sa.Integer(), nullable=False),
    sa.Column('ans', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stage')
    )
    op.create_table('hints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stage', sa.Integer(), nullable=False),
    sa.Column('hint', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stage')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('college_id', sa.String(length=64), nullable=True),
    sa.Column('teamname', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('user_type', sa.String(length=128), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('upgrade_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_college_id'), 'user', ['college_id'], unique=True)
    op.create_index(op.f('ix_user_teamname'), 'user', ['teamname'], unique=True)
    op.create_table('attempts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('stage', sa.Integer(), nullable=True),
    sa.Column('atmpts', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('uptime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    op.drop_table('attempts')
    op.drop_index(op.f('ix_user_teamname'), table_name='user')
    op.drop_index(op.f('ix_user_college_id'), table_name='user')
    op.drop_table('user')
    op.drop_table('hints')
    op.drop_table('answer')
    op.drop_table('announcement')
    # ### end Alembic commands ###
