# FastAPI E-commerce Backend

## Setup Instructions

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the database:**
   - Ensure you have a MySQL server running.
   - Update the `DATABASE_URL` in `app/database.py` 
4. **Initialize the database and seed demo data:**
   ```bash
   uvicorn app.main:app --reload
   python -m demo_data.seed_data
   ```

## API Endpoints

### Products
- `GET /products/` — List all products
- `POST /products/` — Register a new product

### Inventory
- `GET /inventory/` — List all inventory items
- `PUT /inventory/{product_id}/update-quantity` — Update inventory quantity for a product
- `GET /inventory/low-stock` — List products with low stock

### Sales
- `GET /sales/` — List sales (optionally filter by date)
- `GET /sales/revenue/` — Get revenue summary (grouped by day, month, or year)
- `GET /sales/compare/` — Compare revenue between two periods

## Database Schema

- **Product**: `id`, `name`, `category`, `price`, `created_at`
- **Inventory**: `id`, `product_id`, `quantity`, `updated_at`
- **Sale**: `id`, `product_id`, `quantity`, `sale_price`, `sale_date`
