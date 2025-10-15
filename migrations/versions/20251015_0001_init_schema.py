"""Initial DB schema migration"""

from alembic import op
import sqlalchemy as sa

# Revision identifiers
revision = '20251015_0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # === Users ===
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), unique=True, nullable=False),
        sa.Column('email', sa.String(150), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('role', sa.String(50), default='user'),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # === Inventory ===
    op.create_table(
        'inventory',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('quantity', sa.Integer, default=0),
        sa.Column('warehouse_id', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # === Orders ===
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('status', sa.String(50), default='pending'),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # === Tracking ===
    op.create_table(
        'tracking',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.id')),
        sa.Column('location', sa.String(255)),
        sa.Column('status', sa.String(100)),
        sa.Column('timestamp', sa.DateTime, server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('tracking')
    op.drop_table('orders')
    op.drop_table('inventory')
    op.drop_table('users')
