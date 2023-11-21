"""Add Chef Table

Revision ID: a741748a3d61
Revises: add0fd980de9
Create Date: 2023-11-18 22:14:13.611690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a741748a3d61'
down_revision: Union[str, None] = 'add0fd980de9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('recipes', sa.Column('chef_id_new', sa.Integer(), nullable=False), )
    # sa.ForeignKeyConstraint(['chef_id'], ['chefs.id'], )

    # Create a new table recipes_new with the desired schema
    op.create_table(
        'recipes_new',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('ingredients', sa.Text(), nullable=False),
        sa.Column('instructions', sa.Text(), nullable=False),
        sa.Column('chef_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['chef_id'], ['chefs.id'], )
    )

    # Copy data from the old recipes table to the new one
    op.execute(
        'INSERT INTO recipes_new (id, name, ingredients, instructions, chef_id) SELECT id, name, ingredients, instructions, chef_id_new FROM recipes')

    # Drop the old recipes table
    op.drop_table('recipes')

    # Rename the new recipes table to replace the old one
    op.rename_table('recipes_new', 'recipes')

    # Drop the chef_id_new column
    # op.drop_column('recipes', 'chef_id_new')


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'chef_id')
    # ### end Alembic commands ###