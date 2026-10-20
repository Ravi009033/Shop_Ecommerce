from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Shop Catalog API",
    description="Product catalog API for a WhatsApp-first storefront",
    version="1.0.0",
)

# Replace these examples with your real products.
PRODUCTS = [
    {
        "id": 1,
        "name": "Everyday Cotton T-Shirt",
        "category": "Clothing",
        "description": "Soft, comfortable cotton for everyday wear.",
        "price": 499,
        "original_price": 699,
        "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=900",
        "stock": 18,
        "is_featured": True,
        "offer_text": "Save ₹200",
    },
    {
        "id": 2,
        "name": "Classic Casual Shirt",
        "category": "Clothing",
        "description": "A versatile shirt for work and weekends.",
        "price": 899,
        "original_price": 1099,
        "image_url": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=900",
        "stock": 7,
        "is_featured": True,
        "offer_text": "18% OFF",
    },
    {
        "id": 3,
        "name": "Daily Essentials Backpack",
        "category": "Accessories",
        "description": "A practical backpack for daily essentials.",
        "price": 1199,
        "original_price": None,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=900",
        "stock": 0,
        "is_featured": False,
        "offer_text": None,
    },
    {
        "id": 4,
        "name": "Minimal Wrist Watch",
        "category": "Accessories",
        "description": "A clean, minimal design for everyday use.",
        "price": 1499,
        "original_price": 1799,
        "image_url": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=900",
        "stock": 12,
        "is_featured": True,
        "offer_text": "Limited offer",
    },
    {
        "id": 5,
        "name": "Everyday Sneakers",
        "category": "Footwear",
        "description": "Lightweight sneakers designed for daily comfort.",
        "price": 1599,
        "original_price": None,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=900",
        "stock": 4,
        "is_featured": False,
        "offer_text": None,
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "description": "A timeless look for sunny days.",
        "price": 599,
        "original_price": 799,
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=900",
        "stock": 21,
        "is_featured": False,
        "offer_text": "₹200 OFF",
    },
]


class Product(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float = Field(ge=0)
    original_price: Optional[float] = None
    image_url: str
    stock: int = Field(ge=0)
    is_featured: bool = False
    offer_text: Optional[str] = None


@app.get("/")
def root():
    return {"message": "Shop Catalog API is running", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products", response_model=list[Product])
def list_products(
    category: Optional[str] = Query(default=None),
    featured: Optional[bool] = Query(default=None),
    search: Optional[str] = Query(default=None),
):
    results = PRODUCTS
    if category and category.lower() != "all":
        results = [p for p in results if p["category"].lower() == category.lower()]
    if featured is not None:
        results = [p for p in results if p["is_featured"] == featured]
    if search:
        term = search.strip().lower()
        results = [
            p for p in results
            if term in p["name"].lower()
            or term in p["description"].lower()
            or term in p["category"].lower()
        ]
    return results


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
