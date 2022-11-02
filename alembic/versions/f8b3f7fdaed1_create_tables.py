"""create tables

Revision ID: f8b3f7fdaed1
Revises: 
Create Date: 2022-11-02 14:39:57.336368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b3f7fdaed1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    query = """
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE tenants (
  id UUID PRIMARY KEY NOT NULL default uuid_generate_v4(),
  name VARCHAR(250),
  pe_tenant_id TEXT default NULL
);

CREATE TABLE users (
  id UUID PRIMARY KEY NOT NULL default uuid_generate_v4(),
  email VARCHAR(250) NOT NULL,
  tenant_id UUID NOT NULL,

  CONSTRAINT tenant_id_fk FOREIGN KEY (tenant_id) REFERENCES tenants(id)
);
"""
    connection = op.get_bind()
    connection.execute(query)


def downgrade() -> None:
    query = """
    DROP TABLE tenants, users;
    """
    connection = op.get_bind()
    connection.execute(query)
