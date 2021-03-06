"""Add bdc-db and activities v1.0

Revision ID: 962a0f21f6e8
Revises:
Create Date: 2019-12-09 11:37:25.277622

"""
from alembic import op
import geoalchemy2
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '962a0f21f6e8'
down_revision = '15c5dd54c390'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.String(length=20), nullable=False),
    sa.Column('activity_type', sa.String(length=64), nullable=False),
    sa.Column('args', sa.JSON(), nullable=True),
    sa.Column('tags', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('scene_type', sa.String(), nullable=True),
    sa.Column('sceneid', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='collection_builder'
    )

    op.create_table('activity_history',
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('env', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['collection_builder.activities.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['celery_taskmeta.id'], ),
    sa.PrimaryKeyConstraint('activity_id', 'task_id'),
    schema='collection_builder'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('activity_history', schema='collection_builder')
    op.drop_table('activities', schema='collection_builder')

    # ### end Alembic commands ###
