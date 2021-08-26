"""empty message

Revision ID: dcdc20c8898f
Revises: 
Create Date: 2021-08-24 20:14:46.209116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcdc20c8898f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.Text(), nullable=False),
    sa.Column('publisher', sa.Text(), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=False),
    sa.Column('publication_date', sa.Date(), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('link', sa.Text(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('check_in_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('rent_date', sa.Date(), nullable=False),
    sa.Column('return_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rental_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('rent_date', sa.Date(), nullable=False),
    sa.Column('return_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental_book')
    op.drop_table('check_in_book')
    op.drop_table('customer')
    op.drop_table('book')
    # ### end Alembic commands ###