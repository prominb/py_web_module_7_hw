"""Rebuild models

Revision ID: edf7e3af1226
Revises: b77ceb0b0a27
Create Date: 2024-06-19 03:22:59.782438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edf7e3af1226'
down_revision: Union[str, None] = 'b77ceb0b0a27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('grades', 'grade_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('grades', 'grade_date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###