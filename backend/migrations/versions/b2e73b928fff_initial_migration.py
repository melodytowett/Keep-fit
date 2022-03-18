"""Initial Migration

Revision ID: b2e73b928fff
Revises: 
Create Date: 2022-03-18 01:30:32.504775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e73b928fff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('profile_pic', sa.String(), nullable=False),
    sa.Column('urole', sa.String(length=80), nullable=True),
    sa.Column('message', sa.String(length=1000), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('username')
    )
    op.create_table('gig',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('duration', sa.String(length=100), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('trainer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trainer_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enroll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trainee_id', sa.Integer(), nullable=False),
    sa.Column('gig_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gig_id'], ['gig.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['trainee_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_trainers_email', table_name='trainers')
    op.drop_index('ix_trainers_username', table_name='trainers')
    op.drop_table('trainers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trainers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('profile_pic', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='trainers_pkey'),
    sa.UniqueConstraint('phone_number', name='trainers_phone_number_key')
    )
    op.create_index('ix_trainers_username', 'trainers', ['username'], unique=False)
    op.create_index('ix_trainers_email', 'trainers', ['email'], unique=False)
    op.drop_table('enroll')
    op.drop_table('gig')
    op.drop_table('user')
    # ### end Alembic commands ###
