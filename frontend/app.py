import os
from urllib.parse import quote
import requests
import streamlit as st

st.set_page_config(
    page_title="Your Shop | Shop Online",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===== CUSTOMIZE THESE DETAILS FOR YOUR SHOP =====
SHOP_NAME = "YOUR SHOP NAME"
TAGLINE = "Quality you love. Prices you'll love even more."
WHATSAPP_NUMBER = "919876543210"  # Country code + number, digits only
PHONE_DISPLAY = "+91 98765 43210"
CONTACT_EMAIL = "hello@yourshop.com"
SHOP_ADDRESS = "Your shop address, Your City"
INSTAGRAM_URL = "https://www.instagram.com/"
FACEBOOK_URL = "https://www.facebook.com/"
YOUTUBE_URL = "https://www.youtube.com/"
DELIVERY_NOTE = "Message us on WhatsApp to confirm delivery options and availability."
#API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
try:
    API_URL = st.secrets["API_URL"].rstrip("/")
except Exception:
    API_URL = os.getenv(
        "API_URL",
        "http://127.0.0.1:8000"
    ).rstrip("/")
# ================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');
    .stApp { background: #faf9f6; color: #1e293b; }
    [data-testid="stHeader"] { background: rgba(250,249,246,0.92); }
    .block-container { max-width: 1200px; padding-top: 1.1rem; padding-bottom: 3rem; }
    .brand { font-family: 'Playfair Display', Georgia, serif; font-size: 2.15rem; font-weight: 700; color: #153e35; line-height: 1.15; }
    .tagline { color: #64748b; font-size: .98rem; margin-top: .2rem; }
    .topline { background: #153e35; color: white; padding: 9px 14px; border-radius: 10px; text-align: center; font-size: .88rem; margin-bottom: 16px; }
    .hero { background: linear-gradient(120deg, #153e35 0%, #236653 55%, #d6a65c 140%); color: white; padding: 30px 30px; border-radius: 20px; margin: 20px 0 24px 0; }
    .hero h1 { font-family: 'Playfair Display', Georgia, serif; font-size: clamp(2rem, 4vw, 3.3rem); line-height: 1.08; color: white; margin: 0 0 12px 0; }
    .hero p { color: #e7f1eb; font-size: 1.03rem; max-width: 650px; }
    .section-title { font-family: 'Playfair Display', Georgia, serif; color: #153e35; font-size: 1.8rem; font-weight: 700; margin: 18px 0 4px 0; }
    .section-sub { color: #64748b; margin-bottom: 15px; }
    .product-name { font-size: 1.05rem; font-weight: 700; color: #172f2a; min-height: 2.6rem; }
    .price { font-size: 1.28rem; font-weight: 800; color: #153e35; }
    .old-price { color: #94a3b8; text-decoration: line-through; font-size: .95rem; margin-left: 8px; }
    .stock { font-size: .85rem; font-weight: 700; }
    .in-stock { color: #16803d; }
    .out-stock { color: #b91c1c; }
    .offer { display: inline-block; background: #fff0d8; color: #8a4b08; padding: 4px 9px; border-radius: 99px; font-size: .78rem; font-weight: 800; margin-bottom: 7px; }
    .contact-card { background: #fff; border: 1px solid #e8e6df; border-radius: 14px; padding: 16px; }
    div.stButton > button { border-radius: 10px; font-weight: 700; min-height: 2.7rem; }
    .footer { color: #64748b; text-align: center; padding: 24px 0 8px; font-size: .9rem; }
    hr { border-color: #e8e6df; }
</style>
""", unsafe_allow_html=True)


def get_products(category="All", featured=None, search=""):
    params = {}
    if category != "All":
        params["category"] = category
    if featured is not None:
        params["featured"] = str(featured).lower()
    if search:
        params["search"] = search
    try:
        response = requests.get(f"{API_URL}/products", params=params, timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException:
        return [], f"Could not connect to the product API at {API_URL}. Start FastAPI in another terminal."


def whatsapp_url(product):
    message = (
        f"Hello {SHOP_NAME}! I would like to order:\n"
        f"Product: {product['name']}\n"
        f"Product ID: {product['id']}\n"
        f"Price: ₹{product['price']:,.0f}\n"
        "Quantity: 1\n"
        "Please confirm availability, delivery charges, and payment options."
    )
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


st.markdown('<div class="topline">✨ Special offers available — order directly on WhatsApp Business ✨</div>', unsafe_allow_html=True)

header_left, header_right = st.columns([2.3, 1])
with header_left:
    st.markdown(f'<div class="brand">{SHOP_NAME}</div><div class="tagline">{TAGLINE}</div>', unsafe_allow_html=True)
with header_right:
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown(
        f"[📸 Instagram]({INSTAGRAM_URL}) &nbsp; · &nbsp; "
        f"[📘 Facebook]({FACEBOOK_URL}) &nbsp; · &nbsp; "
        f"[▶ YouTube]({YOUTUBE_URL})",
        unsafe_allow_html=True,
    )
    st.link_button("💬 Order on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}", use_container_width=True)

st.markdown("---")
st.markdown(f"""
<div class="hero">
  <h1>Find something<br>you'll love.</h1>
  <p>{TAGLINE} Browse our latest collection, check availability, and order in a few taps through WhatsApp.</p>
</div>
""", unsafe_allow_html=True)

contact1, contact2, contact3 = st.columns(3)
with contact1:
    st.markdown(f'<div class="contact-card">📞 <b>Call us</b><br>{PHONE_DISPLAY}</div>', unsafe_allow_html=True)
with contact2:
    st.markdown(f'<div class="contact-card">✉️ <b>Email</b><br>{CONTACT_EMAIL}</div>', unsafe_allow_html=True)
with contact3:
    st.markdown(f'<div class="contact-card">📍 <b>Visit us</b><br>{SHOP_ADDRESS}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🔥 Offers you’ll love</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">A few customer favourites with special prices.</div>', unsafe_allow_html=True)
featured, error = get_products(featured=True)
if error:
    st.error(error)
elif featured:
    offer_cols = st.columns(min(3, len(featured)))
    for i, product in enumerate(featured[:3]):
        with offer_cols[i]:
            with st.container(border=True):
                st.image(product["image_url"], use_container_width=True)
                if product.get("offer_text"):
                    st.markdown(f'<span class="offer">{product["offer_text"]}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-name">{product["name"]}</div>', unsafe_allow_html=True)
                if product.get("original_price") and product["original_price"] > product["price"]:
                    st.markdown(f'<span class="price">₹{product["price"]:,.0f}</span><span class="old-price">₹{product["original_price"]:,.0f}</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<span class="price">₹{product["price"]:,.0f}</span>', unsafe_allow_html=True)
                if product["stock"] > 0:
                    st.markdown(f'<div class="stock in-stock">● In stock ({product["stock"]} available)</div>', unsafe_allow_html=True)
                    st.link_button("🟢 Buy now on WhatsApp", whatsapp_url(product), use_container_width=True, key=f"offer_{product['id']}")
                else:
                    st.markdown('<div class="stock out-stock">● Currently out of stock</div>', unsafe_allow_html=True)
                    st.button("Out of stock", disabled=True, use_container_width=True, key=f"offer_out_{product['id']}")
else:
    st.info("No offers are configured yet. Mark products as featured in backend/main.py.")

st.markdown("---")
st.markdown('<div class="section-title">🛍️ Explore all products</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Find your favourite product and order directly with us.</div>', unsafe_allow_html=True)

all_products, error = get_products()
if error:
    st.error(error)
else:
    categories = ["All"] + sorted({p["category"] for p in all_products})
    filter_col, search_col = st.columns([1, 2])
    with filter_col:
        category = st.selectbox("Category", categories)
    with search_col:
        search = st.text_input("Search products", placeholder="Search by product name or category…")
    products, error = get_products(category=category, search=search)
    if error:
        st.error(error)
    elif not products:
        st.info("No products match your search.")
    else:
        columns_per_row = 3
        for start in range(0, len(products), columns_per_row):
            cols = st.columns(columns_per_row)
            for col, product in zip(cols, products[start:start + columns_per_row]):
                with col:
                    with st.container(border=True):
                        st.image(product["image_url"], use_container_width=True)
                        if product.get("offer_text"):
                            st.markdown(f'<span class="offer">{product["offer_text"]}</span>', unsafe_allow_html=True)
                        st.markdown(f'<div class="product-name">{product["name"]}</div>', unsafe_allow_html=True)
                        st.caption(product["category"])
                        st.write(product["description"])
                        if product.get("original_price") and product["original_price"] > product["price"]:
                            st.markdown(f'<span class="price">₹{product["price"]:,.0f}</span><span class="old-price">₹{product["original_price"]:,.0f}</span>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<span class="price">₹{product["price"]:,.0f}</span>', unsafe_allow_html=True)
                        if product["stock"] > 0:
                            st.markdown(f'<div class="stock in-stock">● In stock ({product["stock"]} available)</div>', unsafe_allow_html=True)
                            st.link_button("🟢 Buy now on WhatsApp", whatsapp_url(product), use_container_width=True, key=f"product_{product['id']}")
                        else:
                            st.markdown('<div class="stock out-stock">● Currently out of stock</div>', unsafe_allow_html=True)
                            st.button("Out of stock", disabled=True, use_container_width=True, key=f"product_out_{product['id']}")

st.markdown("---")
st.markdown('<div class="section-title">Need help with an order?</div>', unsafe_allow_html=True)
help_col, button_col = st.columns([2, 1])
with help_col:
    st.write(f"Questions about a product, size, delivery, or payment? {DELIVERY_NOTE}")
with button_col:
    st.link_button("Chat with us on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}", use_container_width=True)

st.markdown(
    f'<div class="footer">© {SHOP_NAME} · Made with care · Orders are confirmed by our team on WhatsApp.</div>',
    unsafe_allow_html=True,
)
