# Shop E-commerce Website — FastAPI + Streamlit

A simple product-catalog website for a small shop. Customers can browse products, see stock status and offers, and tap **Buy on WhatsApp** to place an order through WhatsApp Business.

## Features
- Shop name, slogan, contact details, social links and WhatsApp ordering link
- Offer banner
- Product catalog with image, name, price, stock status and optional offer badge
- Search and category filter
- Buy Now opens WhatsApp with a pre-filled order message
- FastAPI backend serves product data
- Streamlit frontend displays the storefront
- Sample data is included so you can run it immediately

## 1. Requirements
- Python 3.10 or newer
- Internet connection for product images and WhatsApp links

## 2. Install
Open a terminal in this project folder:

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 3. Configure your shop
Edit `frontend/app.py` and update:
- `SHOP_NAME`
- `TAGLINE`
- `WHATSAPP_NUMBER` — country code + number, digits only, no `+` or spaces (example format: `919876543210`)
- `PHONE_DISPLAY`
- `CONTACT_EMAIL`
- `INSTAGRAM_URL`, `FACEBOOK_URL`, `YOUTUBE_URL`
- Address and delivery details

Replace the sample product data in `backend/main.py` with your own products, prices, image URLs, stock counts and offers. Use publicly accessible image URLs or host images in your own storage.

## 4. Run the website
Open **two terminals** from the project folder.

Terminal 1 — start FastAPI:
```bash
uvicorn backend.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

Terminal 2 — start Streamlit:
```bash
streamlit run frontend/app.py
```
The website opens at http://localhost:8501.

If you change the API address, set the `API_URL` environment variable accordingly.

## Important notes
- This is a starter storefront, not a payment gateway. Orders are initiated by WhatsApp and are confirmed manually by you.
- Stock values are display-only in this starter. They are not reserved or decremented automatically when someone clicks Buy Now.
- Before public deployment, use your own domain, HTTPS, robust image hosting, input validation, logging, rate limiting, and a production deployment setup.
- Do not publish private API keys or customer data in source control.
