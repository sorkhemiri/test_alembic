"""make pe tenant id unique

Revision ID: 5d773ad6ea12
Revises: f8b3f7fdaed1
Create Date: 2022-11-02 15:16:33.747248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d773ad6ea12'
down_revision = 'f8b3f7fdaed1'
branch_labels = None
depends_on = 'f8b3f7fdaed1'


def upgrade() -> None:
    query = """
    ALTER TABLE tenants ADD CONSTRAINT tenant_id_unique UNIQUE (pe_tenant_id);
    """
    connection = op.get_bind()
    connection.execute(query)


def downgrade() -> None:
    query = """
    ALTER TABLE tenants DROP CONSTRAINT tenant_id_unique;
    """
    connection = op.get_bind()
    connection.execute(query)
