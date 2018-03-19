"""Create tables

Revision ID: 934bda37ac41
Revises:
Create Date: 2017-02-09 23:48:55.704304

"""

# revision identifiers, used by Alembic.
revision = '934bda37ac41'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op   # noqa
import sqlalchemy as sa  # noqa


def upgrade():
    op.create_table(
        'users',

        sa.Column('uuid', sa.String(36), primary_key=True, nullable=False,
                  index=True, unique=True),
        sa.Column('email', sa.String(48), nullable=False, index=True,
                  unique=True),

        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime, index=True),
        sa.Column('deleted_at', sa.DateTime, index=True),
    )

    op.create_table(
        'table2',

        sa.Column('id', sa.Integer, primary_key=True, nullable=False,
                  index=True, unique=True),
        sa.Column('user_uuid', sa.String(36), nullable=False, index=True),
        sa.Column('user_type', sa.String(16)),
        sa.Column('key', sa.Integer, index=True),
        sa.Column('key2', sa.Integer, index=True),

        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime, index=True),
        sa.Column('deleted_at', sa.DateTime, index=True),
    )


def downgrade():
    op.drop_table('table2')
    op.drop_table('users')
