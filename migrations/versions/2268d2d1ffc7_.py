"""empty message

Revision ID: 2268d2d1ffc7
Revises: d064159128ae
Create Date: 2021-08-19 16:27:28.307020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2268d2d1ffc7'
down_revision = 'd064159128ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.Text(), nullable=False),
    sa.Column('publisher', sa.Text(), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=False),
    sa.Column('publication_date', sa.Date(), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('link', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'pages')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_table')
    # ### end Alembic commands ###