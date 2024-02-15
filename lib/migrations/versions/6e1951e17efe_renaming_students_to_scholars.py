"""Renaming students to scholars

Revision ID: 6e1951e17efe
Revises: 791279dd0760
Create Date: 2024-02-15 23:57:04.450744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e1951e17efe'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
     op.rename_table('scholars', 'students')
