"""created tables Restaurant, Pizza and RestaurantPizza

Revision ID: 6475768e8d9a
Revises: c4b7565eae44
Create Date: 2023-09-23 17:04:33.645274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6475768e8d9a'
down_revision = 'c4b7565eae44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('ingredients', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('restaurant_pizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(asdecimal=True), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizza.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_pizza')
    op.drop_table('restaurant')
    op.drop_table('pizza')
    # ### end Alembic commands ###
