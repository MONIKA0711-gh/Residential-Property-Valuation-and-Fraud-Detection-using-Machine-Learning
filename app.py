import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import io
import base64
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PropVista | Bengaluru Real Estate",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Premium CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.main .block-container { padding: 1.5rem 2rem 3rem 2rem; max-width: 1400px; }

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0a0a1a 0%, #1a0533 40%, #0d1b3e 100%);
    border-radius: 24px;
    padding: 3rem 2.5rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0,0,0,0.5);
}
.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 70% 50%, rgba(124,58,237,0.18) 0%, transparent 65%),
                radial-gradient(ellipse at 20% 80%, rgba(59,130,246,0.12) 0%, transparent 55%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(124,58,237,0.2);
    border: 1px solid rgba(124,58,237,0.4);
    border-radius: 50px;
    padding: 0.3rem 1rem;
    font-size: 0.75rem;
    font-weight: 600;
    color: #c4b5fd;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    font-weight: 800;
    color: #fff;
    line-height: 1.15;
    margin-bottom: 0.6rem;
}
.hero-title span { color: #a78bfa; }
.hero-sub {
    font-size: 1.05rem;
    color: #94a3b8;
    max-width: 560px;
    line-height: 1.6;
}
.hero-stats {
    display: flex; gap: 2.5rem; margin-top: 2rem;
}
.hero-stat-val {
    font-family: 'Inter', sans-serif;
    font-size: 1.6rem; font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-stat-lbl { font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }

/* ── KPI Cards ── */
.kpi-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin-bottom: 1.5rem; }
.kpi-card {
    background: linear-gradient(145deg, #111827, #1f2937);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 1.4rem 1.2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: default;
}
.kpi-card::after {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    border-radius: 18px 18px 0 0;
}
.kpi-card.purple::after { background: linear-gradient(90deg,#7c3aed,#a78bfa); }
.kpi-card.blue::after   { background: linear-gradient(90deg,#2563eb,#60a5fa); }
.kpi-card.green::after  { background: linear-gradient(90deg,#059669,#34d399); }
.kpi-card.pink::after   { background: linear-gradient(90deg,#db2777,#f472b6); }
.kpi-card.amber::after  { background: linear-gradient(90deg,#d97706,#fbbf24); }
.kpi-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,0.4); }
.kpi-icon { font-size: 1.6rem; margin-bottom: 0.5rem; }
.kpi-val {
    font-family: 'Inter', sans-serif;
    font-size: 1.7rem; font-weight: 800;
    background: linear-gradient(90deg, #e2e8f0, #a78bfa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1.2;
}
.kpi-lbl { font-size: 0.72rem; color: #6b7280; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 0.3rem; font-weight: 600; }

/* ── Section Header ── */
.sec-hdr {
    font-family: 'Inter', sans-serif;
    font-size: 1.25rem; font-weight: 700;
    color: #e2e8f0;
    margin: 1.6rem 0 1rem;
    display: flex; align-items: center; gap: 0.6rem;
}
.sec-hdr::before {
    content: '';
    display: inline-block; width: 4px; height: 1.25rem;
    background: linear-gradient(180deg, #7c3aed, #60a5fa);
    border-radius: 4px;
}

/* ── Glass Card ── */
.glass-card {
    background: rgba(17,24,39,0.8);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 1.5rem;
    backdrop-filter: blur(10px);
    margin-bottom: 1rem;
}
.glass-card:hover { border-color: rgba(124,58,237,0.3); }

/* ── Prediction Result ── */
.pred-result {
    background: linear-gradient(145deg, #13004d, #1a0066, #0d1b4a);
    border: 1.5px solid rgba(167,139,250,0.4);
    border-radius: 24px;
    padding: 2.2rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 60px rgba(124,58,237,0.2), inset 0 1px 0 rgba(255,255,255,0.05);
    animation: glow 3s ease-in-out infinite;
}
@keyframes glow {
    0%, 100% { box-shadow: 0 0 40px rgba(124,58,237,0.2), inset 0 1px 0 rgba(255,255,255,0.05); }
    50%       { box-shadow: 0 0 80px rgba(124,58,237,0.4), inset 0 1px 0 rgba(255,255,255,0.05); }
}
.pred-label { font-size: 0.8rem; color: #6b7280; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.4rem; }
.pred-price {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem; font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #60a5fa, #a78bfa);
    background-size: 200%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
}
@keyframes shimmer { 0%{background-position:0%} 100%{background-position:200%} }
.pred-crore { font-size: 1rem; color: #94a3b8; margin-top: 0.2rem; }
.pred-badge {
    display: inline-block; margin-top: 1rem;
    background: rgba(124,58,237,0.15); border: 1px solid rgba(124,58,237,0.3);
    border-radius: 50px; padding: 0.3rem 1rem;
    font-size: 0.75rem; color: #c4b5fd; font-weight: 600;
}

/* ── Property Summary Card ── */
.prop-summary {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    border: 1px solid rgba(96,165,250,0.2);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.prop-summary-title {
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem; font-weight: 700;
    color: #60a5fa;
    text-transform: uppercase; letter-spacing: 2px;
    margin-bottom: 1rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.prop-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;
}
.prop-item { display: flex; flex-direction: column; }
.prop-item-lbl { font-size: 0.7rem; color: #6b7280; text-transform: uppercase; letter-spacing: 1px; }
.prop-item-val { font-size: 1rem; font-weight: 700; color: #e2e8f0; margin-top: 0.1rem; }

/* ── Market Badge ── */
.market-tag {
    display: inline-flex; align-items: center; gap: 0.4rem;
    border-radius: 50px; padding: 0.5rem 1.2rem;
    font-weight: 700; font-size: 0.88rem; margin-top: 0.8rem;
}
.market-tag.above { background: rgba(239,68,68,0.12); border:1px solid rgba(239,68,68,0.3); color:#f87171; }
.market-tag.below { background: rgba(52,211,153,0.12); border:1px solid rgba(52,211,153,0.3); color:#34d399; }
.market-tag.fair  { background: rgba(251,191,36,0.12);  border:1px solid rgba(251,191,36,0.3);  color:#fbbf24; }

/* ── Insight Pill ── */
.insight-pill {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    transition: all 0.25s;
    display: flex; align-items: flex-start; gap: 0.8rem;
}
.insight-pill:hover { border-color:rgba(167,139,250,0.3); transform:translateX(3px); }
.insight-pill-icon { font-size:1.4rem; flex-shrink:0; }
.insight-pill-body { flex:1; }
.insight-pill-title { font-size:0.85rem; font-weight:700; color:#c4b5fd; }
.insight-pill-text  { font-size:0.78rem; color:#94a3b8; margin-top:0.2rem; line-height:1.5; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080818 0%, #0f0c29 50%, #0a1628 100%);
    border-right: 1px solid rgba(124,58,237,0.2);
}
.sidebar-logo {
    text-align: center; padding: 1.5rem 0 1rem;
    border-bottom: 1px solid rgba(124,58,237,0.15);
    margin-bottom: 1.2rem;
}
.sidebar-logo-icon { font-size: 2.8rem; }
.sidebar-logo-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem; font-weight: 700; color: #a78bfa; letter-spacing: 1px;
}
.sidebar-logo-sub { font-size: 0.7rem; color: #475569; text-transform: uppercase; letter-spacing: 2px; }
.sidebar-stat {
    background: rgba(124,58,237,0.08);
    border: 1px solid rgba(124,58,237,0.12);
    border-radius: 12px; padding: 0.8rem 1rem;
    margin-bottom: 0.5rem;
    display: flex; justify-content: space-between; align-items: center;
}
.sidebar-stat-lbl { font-size: 0.72rem; color: #64748b; font-weight: 600; }
.sidebar-stat-val { font-size: 0.9rem; font-weight: 800; color: #a78bfa; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white; border: none; border-radius: 12px;
    font-weight: 700; font-size: 0.95rem;
    padding: 0.65rem 1.5rem; width: 100%;
    transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(124,58,237,0.35);
    letter-spacing: 0.3px;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(124,58,237,0.55);
    background: linear-gradient(135deg, #8b5cf6, #6366f1);
}
/* Reset button overrides */
.reset-btn .stButton > button {
    background: linear-gradient(135deg, #1e293b, #334155) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #94a3b8 !important;
    box-shadow: none !important;
}
.reset-btn .stButton > button:hover {
    background: linear-gradient(135deg, #334155, #475569) !important;
    color: #e2e8f0 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
}
/* Download button */
.dl-btn .stDownloadButton > button {
    background: linear-gradient(135deg, #059669, #10b981) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 0.95rem !important; width: 100% !important;
    box-shadow: 0 4px 20px rgba(16,185,129,0.35) !important;
    transition: all 0.3s !important; padding: 0.65rem 1.5rem !important;
}
.dl-btn .stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(16,185,129,0.55) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(15,12,41,0.6); border-radius: 14px;
    padding: 5px; gap: 4px; border: 1px solid rgba(255,255,255,0.05);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px; color: #6b7280; font-weight: 600; font-size: 0.88rem;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
}

/* ── DataFrame ── */
[data-testid="stDataFrame"] { border-radius: 14px; overflow: hidden; border: 1px solid rgba(255,255,255,0.06); }

/* ── Empty state ── */
.empty-state {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; min-height: 280px;
    border: 2px dashed rgba(124,58,237,0.2);
    border-radius: 20px; color: #475569;
    text-align: center; padding: 2rem;
}
.empty-state-icon { font-size: 3rem; margin-bottom: 1rem; opacity: 0.5; }

/* ── Footer ── */
.footer {
    text-align: center; padding: 2rem 0 0.5rem;
    font-size: 0.75rem; color: #374151;
    border-top: 1px solid rgba(255,255,255,0.04); margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)


# ─── Data & Model ─────────────────────────────────────────────────────────────
@st.cache_data
def load_and_preprocess():
    df = pd.read_csv("Bengaluru_House_Data.csv")
    df = df.drop(['area_type', 'availability', 'society'], axis=1)
    df = df.dropna()

    def get_bhk(size):
        try: return int(str(size).split(' ')[0])
        except: return np.nan

    def convert_sqft(x):
        tokens = str(x).split('-')
        if len(tokens) == 2:
            try: return (float(tokens[0]) + float(tokens[1])) / 2
            except: return np.nan
        try: return float(x)
        except: return np.nan

    df['bhk'] = df['size'].apply(get_bhk)
    df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
    df = df.dropna()
    df['price_per_sqft'] = (df['price'] * 100000) / df['total_sqft']
    location_avg_price = df.groupby('location')['price'].mean()
    city_avg_price = df['price'].mean()
    df['location_avg_price'] = df['location'].map(location_avg_price)
    df['location_premium'] = df['location_avg_price'] / city_avg_price
    df['sqft_per_bhk'] = df['total_sqft'] / df['bhk']
    df = df[df['sqft_per_bhk'] >= 300]
    df = df[df['bath'] < df['bhk'] + 3]
    location_count = df.location.value_counts()
    df.location = df.location.apply(lambda x: 'other' if location_count[x] <= 10 else x)
    df = df.drop(['size'], axis=1)
    return df


@st.cache_data
def train_model(df):
    features = ['total_sqft', 'bhk', 'bath', 'location_avg_price', 'location_premium', 'sqft_per_bhk']
    avail = [f for f in features if f in df.columns]
    X = df[avail].values.astype(float)
    y = df['price'].values
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    mean = X_train.mean(axis=0); std = X_train.std(axis=0); std[std == 0] = 1
    X_tr = (X_train - mean) / std; X_te = (X_test - mean) / std
    W = np.zeros(X_tr.shape[1]); b = 0; lr = 0.001; losses = []
    for _ in range(5000):
        yp = np.dot(X_tr, W) + b; loss = np.mean((y_train - yp) ** 2); losses.append(loss)
        n = len(y_train); dw = (-2/n)*np.dot(X_tr.T,(y_train-yp)); db = (-2/n)*np.sum(y_train-yp)
        W -= lr*dw; b -= lr*db
    ytp = np.dot(X_te, W) + b
    r2 = 1 - np.sum((y_test-ytp)**2)/np.sum((y_test-y_test.mean())**2)
    rmse = np.sqrt(np.mean((y_test-ytp)**2))
    return W, b, mean, std, losses, r2, rmse, y_test, ytp, avail


df = load_and_preprocess()
W, b, mean_vals, std_vals, losses, r2, rmse, y_test, y_test_pred, feature_cols = train_model(df)
loc_avg_map = df.groupby('location')['price'].mean().to_dict()
city_avg = df['price'].mean()
CLRS = ["#a78bfa","#60a5fa","#34d399","#f472b6","#fbbf24","#fb923c"]
PTPL = dict(layout=go.Layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#cbd5e1", family="DM Sans"),
    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", linecolor="rgba(255,255,255,0.08)", zerolinecolor="rgba(255,255,255,0.05)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", linecolor="rgba(255,255,255,0.08)", zerolinecolor="rgba(255,255,255,0.05)"),
    colorway=CLRS,
))


# ─── PDF Report Generator ─────────────────────────────────────────────────────
def generate_pdf_report(location, total_sqft, bhk, bath, predicted,
                        loc_avg, loc_premium, sqft_per_bhk,
                        comparables_df, avg_comp, diff_pct, r2_score):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    story = []

    # ── Colours
    PURPLE = colors.HexColor('#7c3aed')
    DARK   = colors.HexColor('#0f172a')
    LIGHT  = colors.HexColor('#e2e8f0')
    MUTED  = colors.HexColor('#94a3b8')
    GREEN  = colors.HexColor('#10b981')
    RED    = colors.HexColor('#f87171')

    # ── Custom styles
    title_style = ParagraphStyle('Title2', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=22, textColor=PURPLE,
        alignment=TA_CENTER, spaceAfter=4)
    sub_style = ParagraphStyle('Sub', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, textColor=MUTED,
        alignment=TA_CENTER, spaceAfter=16)
    sec_style = ParagraphStyle('Sec', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=13, textColor=PURPLE,
        spaceBefore=16, spaceAfter=6)
    body_style = ParagraphStyle('Body', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#334155'),
        leading=16, spaceAfter=6)
    small_style = ParagraphStyle('Small', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, textColor=MUTED,
        alignment=TA_CENTER, spaceAfter=4)

    now = datetime.now().strftime("%d %B %Y, %I:%M %p")

    # ── Header block
    header_data = [[
        Paragraph("<b>PropVista</b>", ParagraphStyle('logo', fontName='Helvetica-Bold',
            fontSize=18, textColor=PURPLE)),
        Paragraph(f"<font color='#94a3b8'>Report Generated: {now}</font>",
                  ParagraphStyle('date', fontName='Helvetica', fontSize=9,
                                 textColor=MUTED, alignment=TA_RIGHT))
    ]]
    header_tbl = Table(header_data, colWidths=[9*cm, 8*cm])
    header_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(header_tbl)
    story.append(HRFlowable(width="100%", thickness=1.5, color=PURPLE, spaceAfter=14))

    # ── Title
    story.append(Paragraph("Property Valuation Report", title_style))
    story.append(Paragraph("Bengaluru Real Estate — ML-Powered Price Estimate", sub_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=16))

    # ── Predicted Price Box
    price_data = [[
        Paragraph("<b>Estimated Market Value</b>",
                  ParagraphStyle('ph', fontName='Helvetica-Bold', fontSize=11, textColor=MUTED, alignment=TA_CENTER)),
    ],[
        Paragraph(f"<b>Rs. {predicted:.2f} Lakhs</b>",
                  ParagraphStyle('pv', fontName='Helvetica-Bold', fontSize=26, textColor=PURPLE, alignment=TA_CENTER)),
    ],[
        Paragraph(f"Approx. Rs. {predicted/100:.3f} Crores",
                  ParagraphStyle('pc', fontName='Helvetica', fontSize=11, textColor=MUTED, alignment=TA_CENTER)),
    ]]
    price_tbl = Table(price_data, colWidths=[17*cm])
    price_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f5f3ff')),
        ('ROUNDEDCORNERS', [10]),
        ('BOX', (0,0), (-1,-1), 1.5, PURPLE),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(KeepTogether(price_tbl))
    story.append(Spacer(1, 16))

    # ── Property Details
    story.append(Paragraph("Property Details", sec_style))
    details = [
        ["Field", "Value"],
        ["Location", location],
        ["Total Area", f"{total_sqft:,} sq ft"],
        ["Configuration", f"{bhk} BHK"],
        ["Bathrooms", str(bath)],
        ["Sqft per BHK", f"{sqft_per_bhk:.0f} sq ft"],
    ]
    det_tbl = Table(details, colWidths=[6*cm, 11*cm])
    det_tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), PURPLE),
        ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
        ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,0), 10),
        ('FONTNAME',     (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',     (0,1), (-1,-1), 10),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TEXTCOLOR',    (0,1), (-1,-1), DARK),
        ('BOX',          (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('INNERGRID',    (0,0), (-1,-1), 0.25, colors.HexColor('#e2e8f0')),
        ('TOPPADDING',   (0,0), (-1,-1), 7),
        ('BOTTOMPADDING',(0,0), (-1,-1), 7),
        ('LEFTPADDING',  (0,0), (-1,-1), 10),
    ]))
    story.append(det_tbl)
    story.append(Spacer(1, 12))

    # ── Location Analysis
    story.append(Paragraph("Location Analysis", sec_style))
    loc_data = [
        ["Metric", "Value", "Insight"],
        ["Location Avg. Price", f"Rs. {loc_avg:.1f}L", "Area benchmark"],
        ["Location Premium Index", f"{loc_premium:.2f}x", "vs city average"],
        ["City Average Price", f"Rs. {city_avg:.1f}L", "Overall benchmark"],
    ]
    loc_tbl = Table(loc_data, colWidths=[6.5*cm, 4.5*cm, 6*cm])
    loc_tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), colors.HexColor('#4f46e5')),
        ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
        ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,0), 10),
        ('FONTNAME',     (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',     (0,1), (-1,-1), 10),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f0f4ff')]),
        ('TEXTCOLOR',    (0,1), (-1,-1), DARK),
        ('BOX',          (0,0), (-1,-1), 0.5, colors.HexColor('#c7d2fe')),
        ('INNERGRID',    (0,0), (-1,-1), 0.25, colors.HexColor('#c7d2fe')),
        ('TOPPADDING',   (0,0), (-1,-1), 7),
        ('BOTTOMPADDING',(0,0), (-1,-1), 7),
        ('LEFTPADDING',  (0,0), (-1,-1), 10),
    ]))
    story.append(loc_tbl)
    story.append(Spacer(1, 12))

    # ── Market Comparison
    if comparables_df is not None and not comparables_df.empty:
        story.append(Paragraph("Market Comparison", sec_style))
        diff_color = GREEN if diff_pct < 0 else RED
        direction = "BELOW" if diff_pct < 0 else "ABOVE"
        story.append(Paragraph(
            f"This property is estimated <b>{abs(diff_pct):.1f}% {direction}</b> the comparable market average of Rs. {avg_comp:.1f}L.",
            body_style))
        story.append(Spacer(1, 6))

        comp_data = [["Location", "Sqft", "BHK", "Bath", "Price (L)"]]
        for _, row in comparables_df.iterrows():
            comp_data.append([row['location'], f"{row['total_sqft']:.0f}",
                              str(int(row['bhk'])), str(int(row['bath'])), f"Rs. {row['price']:.1f}"])
        comp_tbl = Table(comp_data, colWidths=[5*cm, 3*cm, 2.5*cm, 2.5*cm, 4*cm])
        comp_tbl.setStyle(TableStyle([
            ('BACKGROUND',   (0,0), (-1,0), colors.HexColor('#0f766e')),
            ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
            ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE',     (0,0), (-1,-1), 9),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f0fdf9')]),
            ('TEXTCOLOR',    (0,1), (-1,-1), DARK),
            ('BOX',          (0,0), (-1,-1), 0.5, colors.HexColor('#a7f3d0')),
            ('INNERGRID',    (0,0), (-1,-1), 0.25, colors.HexColor('#a7f3d0')),
            ('TOPPADDING',   (0,0), (-1,-1), 6), ('BOTTOMPADDING',(0,0),(-1,-1),6),
            ('LEFTPADDING',  (0,0), (-1,-1), 8),
        ]))
        story.append(comp_tbl)
        story.append(Spacer(1, 12))

    # ── Model Info
    story.append(Paragraph("Model Information", sec_style))
    model_data = [
        ["Parameter", "Value"],
        ["Algorithm", "Linear Regression (NumPy Gradient Descent)"],
        ["Training Epochs", "5,000"],
        ["Learning Rate", "0.001"],
        ["R-squared Score", f"{r2_score:.4f}"],
        ["Features Used", ", ".join(feature_cols)],
    ]
    mod_tbl = Table(model_data, colWidths=[6*cm, 11*cm])
    mod_tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), colors.HexColor('#374151')),
        ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
        ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,0), 10),
        ('FONTNAME',     (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',     (0,1), (-1,-1), 9),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f9fafb')]),
        ('TEXTCOLOR',    (0,1), (-1,-1), DARK),
        ('BOX',          (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
        ('INNERGRID',    (0,0), (-1,-1), 0.25, colors.HexColor('#e5e7eb')),
        ('TOPPADDING',   (0,0), (-1,-1), 6), ('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LEFTPADDING',  (0,0), (-1,-1), 10),
    ]))
    story.append(mod_tbl)
    story.append(Spacer(1, 20))

    # ── Footer
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=8))
    story.append(Paragraph(
        "This report is generated by PropVista AI — for informational purposes only. "
        "Actual prices may vary based on market conditions, property condition, and negotiation.",
        small_style))
    story.append(Paragraph(f"PropVista | Bengaluru Real Estate Analytics | {now}", small_style))

    doc.build(story)
    return buf.getvalue()


# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🏙️</div>
        <div class="sidebar-logo-name">PropVista</div>
        <div class="sidebar-logo-sub">Bengaluru Real Estate</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("", [
        "🏠  Overview",
        "📊  Market Analysis",
        "🤖  ML Engine",
        "🔮  Price Predictor",
    ], label_visibility="collapsed")

    st.markdown("<div style='margin-top:1.5rem;'>", unsafe_allow_html=True)
    for lbl, val, col in [
        ("Total Listings", f"{len(df):,}", "#a78bfa"),
        ("Active Locations", f"{df['location'].nunique()}", "#60a5fa"),
        ("Median Price", f"₹{df['price'].median():.0f}L", "#34d399"),
        ("Model R²", f"{r2:.4f}", "#f472b6"),
    ]:
        st.markdown(f"""
        <div class="sidebar-stat">
            <span class="sidebar-stat-lbl">{lbl}</span>
            <span class="sidebar-stat-val" style="color:{col};">{val}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:2rem; padding:1rem; background:rgba(16,185,129,0.06);
                border:1px solid rgba(16,185,129,0.15); border-radius:12px;">
        <div style="font-size:0.7rem; color:#10b981; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:0.4rem;">Live Status</div>
        <div style="font-size:0.8rem; color:#94a3b8;">✅ Model trained &amp; ready</div>
        <div style="font-size:0.8rem; color:#94a3b8; margin-top:0.2rem;">✅ Dataset loaded</div>
    </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
#  PAGE 1 — OVERVIEW
# ════════════════════════════════════════════════════════════════════════════════
if page == "🏠  Overview":
    st.markdown(f"""
    <div class="hero-wrap">
        <div class="hero-badge">🏙️ Bengaluru Real Estate Intelligence</div>
        <div class="hero-title">The Smart Way to Value<br><span>Property in Bengaluru</span></div>
        <div class="hero-sub">AI-powered price prediction, market analysis, and neighbourhood insights — all in one premium dashboard.</div>
        <div class="hero-stats">
            <div>
                <div class="hero-stat-val">{len(df):,}</div>
                <div class="hero-stat-lbl">Properties Analysed</div>
            </div>
            <div>
                <div class="hero-stat-val">{df['location'].nunique()}</div>
                <div class="hero-stat-lbl">Neighbourhoods</div>
            </div>
            <div>
                <div class="hero-stat-val">₹{df['price'].median():.0f}L</div>
                <div class="hero-stat-lbl">Median Price</div>
            </div>
            <div>
                <div class="hero-stat-val">{r2:.3f}</div>
                <div class="hero-stat-lbl">Model R² Score</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI Cards
    c1,c2,c3,c4,c5 = st.columns(5)
    kpis = [
        ("purple","🏘️",f"{len(df):,}","Total Listings"),
        ("blue","📍",f"{df['location'].nunique()}","Locations"),
        ("green","💰",f"₹{df['price'].median():.0f}L","Median Price"),
        ("pink","📐",f"{df['total_sqft'].median():,.0f}","Median Sqft"),
        ("amber","🛁",f"{df['bath'].median():.0f}","Avg Baths"),
    ]
    for col,(cls,icon,val,lbl) in zip([c1,c2,c3,c4,c5],kpis):
        with col:
            st.markdown(f"""
            <div class="kpi-card {cls}">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-val">{val}</div>
                <div class="kpi-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([3, 2], gap="large")

    with col_a:
        st.markdown('<div class="sec-hdr">Price Distribution</div>', unsafe_allow_html=True)
        fig = px.histogram(df[df['price']<500], x='price', nbins=60, color_discrete_sequence=["#7c3aed"])
        fig.update_traces(opacity=0.85, marker_line_color="#a78bfa", marker_line_width=0.4)
        fig.update_layout(template=PTPL, height=320, margin=dict(l=0,r=0,t=10,b=0),
                          xaxis_title="Price (Lakhs)", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        st.markdown('<div class="sec-hdr">BHK Split</div>', unsafe_allow_html=True)
        bhk_c = df['bhk'].value_counts().reset_index()
        bhk_c.columns = ['BHK','Count']; bhk_c = bhk_c[bhk_c['BHK']<=6]
        fig2 = px.pie(bhk_c, names='BHK', values='Count', color_discrete_sequence=CLRS, hole=0.5)
        fig2.update_traces(textfont_size=12, pull=[0.04]*len(bhk_c))
        fig2.update_layout(template=PTPL, height=320, margin=dict(l=0,r=0,t=10,b=0),
                           legend=dict(orientation="h", y=-0.15))
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown('<div class="sec-hdr">Top 15 Locations by Listing Volume</div>', unsafe_allow_html=True)
    top = df['location'].value_counts().head(15).reset_index(); top.columns=['Location','Count']
    fig3 = px.bar(top, x='Count', y='Location', orientation='h', color='Count',
                  color_continuous_scale='Viridis', text='Count')
    fig3.update_traces(texttemplate='%{text:,}', textposition='outside')
    fig3.update_layout(template=PTPL, height=400, margin=dict(l=0,r=60,t=10,b=0),
                       yaxis=dict(autorange="reversed"), showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

    # ── Quick Insights
    st.markdown('<div class="sec-hdr">Key Market Insights</div>', unsafe_allow_html=True)
    top_loc = df.groupby('location')['price'].mean().idxmax()
    top_price = df.groupby('location')['price'].mean().max()
    insights = [
        ("🏆","Most Premium Location", f"{top_loc} commands the highest avg. price at ₹{top_price:.1f}L"),
        ("📈","Price Range", f"Properties span from ₹{df['price'].min():.0f}L to ₹{df['price'].max():.0f}L — a wide {df['price'].max()/df['price'].min():.0f}x range"),
        ("🏗️","Most Common Type", f"{df['bhk'].mode()[0]} BHK is the most listed configuration at {(df['bhk']==df['bhk'].mode()[0]).mean()*100:.0f}% of all listings"),
        ("💧","Bath Insights", f"Most homes have {df['bath'].mode()[0]} bathrooms; avg. sqft/BHK is {df['sqft_per_bhk'].mean():.0f} sq ft"),
    ]
    c1, c2 = st.columns(2)
    for i,(icon,title,text) in enumerate(insights):
        with (c1 if i%2==0 else c2):
            st.markdown(f"""
            <div class="insight-pill">
                <div class="insight-pill-icon">{icon}</div>
                <div class="insight-pill-body">
                    <div class="insight-pill-title">{title}</div>
                    <div class="insight-pill-text">{text}</div>
                </div>
            </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
#  PAGE 2 — MARKET ANALYSIS
# ════════════════════════════════════════════════════════════════════════════════
elif page == "📊  Market Analysis":
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">📊 Deep Dive Analytics</div>
        <div class="hero-title">Market <span>Analysis</span></div>
        <div class="hero-sub">Correlations, spatial distribution, price drivers and neighbourhood intelligence.</div>
    </div>""", unsafe_allow_html=True)

    tab1,tab2,tab3,tab4 = st.tabs(["🔥 Correlations","📐 Area vs Price","📦 Config Analysis","🌆 Neighbourhood Intel"])

    with tab1:
        num_df = df.select_dtypes(include=np.number); corr = num_df.corr()
        fig = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r", zmin=-1, zmax=1, aspect="auto")
        fig.update_layout(template=PTPL, height=480, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="Feature Correlation Matrix", font=dict(size=14,color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        pc = corr['price'].drop('price').sort_values(ascending=False)
        fig2 = px.bar(x=pc.index, y=pc.values, color=pc.values, color_continuous_scale='RdBu',
                      labels={'x':'Feature','y':'Correlation with Price'},
                      text=[f"{v:.3f}" for v in pc.values])
        fig2.update_traces(textposition='outside')
        fig2.update_layout(template=PTPL, height=310, margin=dict(l=0,r=0,t=10,b=0),
                           title=dict(text="Feature Importance (Correlation with Price)", font=dict(size=13,color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        samp = df[df['price']<500].sample(min(3000,len(df)), random_state=42)
        fig = px.scatter(samp, x='total_sqft', y='price', color='bhk',
                         color_continuous_scale='Plasma', opacity=0.55,
                         labels={'total_sqft':'Total Sqft','price':'Price (Lakhs)','bhk':'BHK'},
                         hover_data=['location','bath'])
        fig.update_layout(template=PTPL, height=440, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="Total Area vs Price (coloured by BHK)", font=dict(size=13,color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        c1,c2 = st.columns(2)
        with c1:
            fig3 = px.histogram(df[df['total_sqft']<5000], x='total_sqft', nbins=50,
                                color_discrete_sequence=["#60a5fa"])
            fig3.update_layout(template=PTPL, height=280, margin=dict(l=0,r=0,t=30,b=0),
                               title=dict(text="Area Distribution", font=dict(color="#c4b5fd"), x=0.5))
            st.plotly_chart(fig3, use_container_width=True)
        with c2:
            fig4 = px.histogram(df[df['price_per_sqft']<50000], x='price_per_sqft', nbins=50,
                                color_discrete_sequence=["#34d399"])
            fig4.update_layout(template=PTPL, height=280, margin=dict(l=0,r=0,t=30,b=0),
                               title=dict(text="Price/Sqft Distribution", font=dict(color="#c4b5fd"), x=0.5))
            st.plotly_chart(fig4, use_container_width=True)

    with tab3:
        fig = px.box(df[(df['bhk']<=6)&(df['price']<500)], x='bhk', y='price', color='bhk',
                     color_discrete_sequence=CLRS, notched=True,
                     labels={'bhk':'BHK','price':'Price (Lakhs)'})
        fig.update_layout(template=PTPL, height=400, showlegend=False, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="Price Distribution by BHK Configuration", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        fig5 = px.violin(df[df['price']<500], x='bath', y='price', color='bath',
                         color_discrete_sequence=CLRS, box=True,
                         labels={'bath':'Bathrooms','price':'Price (Lakhs)'})
        fig5.update_layout(template=PTPL, height=360, showlegend=False, margin=dict(l=0,r=0,t=20,b=0),
                           title=dict(text="Price Distribution by Bathroom Count", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig5, use_container_width=True)

    with tab4:
        la = df.groupby('location')['price'].agg(['mean','count']).reset_index()
        la.columns=['Location','Avg_Price','Count']; la=la[la['Count']>=20].sort_values('Avg_Price',ascending=False).head(20)
        fig = px.bar(la, x='Avg_Price', y='Location', orientation='h',
                     color='Avg_Price', color_continuous_scale='Magma',
                     text=la['Avg_Price'].apply(lambda x:f"₹{x:.0f}L"))
        fig.update_traces(textposition='outside')
        fig.update_layout(template=PTPL, height=560, margin=dict(l=0,r=80,t=20,b=0),
                          yaxis=dict(autorange="reversed"),
                          title=dict(text="Top 20 Locations by Average Price", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)

        pd_df = df.groupby('location')['location_premium'].mean().reset_index()
        pd_df = pd_df.sort_values('location_premium',ascending=False).head(15)
        fig2 = px.bar(pd_df, x='location', y='location_premium', color='location_premium',
                      color_continuous_scale='RdYlGn',
                      text=pd_df['location_premium'].apply(lambda x:f"{x:.2f}x"),
                      labels={'location':'Location','location_premium':'Premium Index'})
        fig2.update_traces(textposition='outside')
        fig2.add_hline(y=1.0, line_dash="dash", line_color="#f472b6", line_width=1.5,
                       annotation_text="City Average", annotation_font_color="#f472b6")
        fig2.update_layout(template=PTPL, height=360, margin=dict(l=0,r=0,t=20,b=80),
                           title=dict(text="Location Premium Index (1.0 = City Average)", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig2, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════════
#  PAGE 3 — ML ENGINE
# ════════════════════════════════════════════════════════════════════════════════
elif page == "🤖  ML Engine":
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">🤖 Machine Learning</div>
        <div class="hero-title">Linear Regression <span>Engine</span></div>
        <div class="hero-sub">Built from scratch with NumPy — gradient descent, feature standardisation, zero sklearn for training.</div>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,(icon,val,lbl) in zip([c1,c2,c3,c4],[
        ("📈",f"{r2:.4f}","R² Score"),
        ("📉",f"₹{rmse:.1f}L","RMSE"),
        ("🏋️","5,000","Epochs"),
        ("⚡","0.001","Learning Rate"),
    ]):
        with col:
            st.markdown(f"""
            <div class="kpi-card purple">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-val">{val}</div>
                <div class="kpi-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    tab1,tab2,tab3 = st.tabs(["📉 Training Loss","🎯 Prediction Quality","⚖️ Feature Weights"])

    with tab1:
        loss_df = pd.DataFrame({'Epoch':range(len(losses)),'MSE Loss':losses})
        fig = px.line(loss_df, x='Epoch', y='MSE Loss', color_discrete_sequence=["#a78bfa"], line_shape='spline')
        fig.update_traces(line_width=2.5)
        fig.add_annotation(x=len(losses)-1, y=losses[-1], text=f"Final: {losses[-1]:,.0f}",
                           showarrow=True, arrowhead=2, arrowcolor="#a78bfa", font=dict(color="#a78bfa",size=12))
        fig.update_layout(template=PTPL, height=400, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="MSE Loss Curve (5,000 Epochs)", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        ck = [(i,losses[i]) for i in range(0,len(losses),500)]
        ck_df = pd.DataFrame(ck, columns=['Epoch','MSE Loss'])
        ck_df['MSE Loss'] = ck_df['MSE Loss'].apply(lambda x:f"{x:,.2f}")
        st.dataframe(ck_df, use_container_width=True, hide_index=True)

    with tab2:
        mask = (y_test<500)&(y_test_pred<500)
        sc_df = pd.DataFrame({'Actual':y_test[mask],'Predicted':y_test_pred[mask],
                               'Error':np.abs(y_test[mask]-y_test_pred[mask])})
        fig = px.scatter(sc_df, x='Actual', y='Predicted', color='Error',
                         color_continuous_scale='Viridis', opacity=0.55,
                         labels={'Actual':'Actual Price (L)','Predicted':'Predicted Price (L)'})
        mn,mx = sc_df['Actual'].min(), sc_df['Actual'].max()
        fig.add_shape(type="line", x0=mn,y0=mn,x1=mx,y1=mx, line=dict(color="#f472b6",dash="dash",width=2))
        fig.add_annotation(x=mx*0.75,y=mx*0.75+25,text="Perfect Prediction Line",
                           font=dict(color="#f472b6",size=11), showarrow=False)
        fig.update_layout(template=PTPL, height=420, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="Predicted vs Actual (Test Set)", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        res = y_test[mask]-y_test_pred[mask]
        fig2 = px.histogram(x=res, nbins=60, color_discrete_sequence=["#34d399"],
                            labels={'x':'Residual (Actual − Predicted)'})
        fig2.add_vline(x=0, line_dash="dash", line_color="#f472b6", line_width=2)
        fig2.update_layout(template=PTPL, height=300, margin=dict(l=0,r=0,t=20,b=0),
                           title=dict(text="Residual Distribution", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        wdf = pd.DataFrame({'Feature':feature_cols,'Weight':W}).sort_values('Weight',ascending=False)
        fig = px.bar(wdf, x='Feature', y='Weight', color='Weight', color_continuous_scale='RdBu',
                     text=wdf['Weight'].apply(lambda x:f"{x:.3f}"))
        fig.update_traces(textposition='outside')
        fig.update_layout(template=PTPL, height=380, margin=dict(l=0,r=0,t=20,b=0),
                          title=dict(text="Learned Feature Weights", font=dict(color="#c4b5fd"), x=0.5))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"""
        <div class="glass-card" style="margin-top:0.5rem;">
            <div style="font-size:0.75rem; font-weight:700; color:#60a5fa; text-transform:uppercase; letter-spacing:2px; margin-bottom:0.6rem;">Model Equation (standardised features)</div>
            <code style="font-size:0.8rem; color:#c4b5fd; line-height:1.8;">
                Price = {' + '.join([f'<b>{w:.3f}</b>×{f}' for w,f in zip(W,feature_cols)])} + {b:.3f}
            </code>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
#  PAGE 4 — PRICE PREDICTOR
# ════════════════════════════════════════════════════════════════════════════════
elif page == "🔮  Price Predictor":
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">🔮 AI Price Predictor</div>
        <div class="hero-title">Instant Property <span>Valuation</span></div>
        <div class="hero-sub">Configure your property below and get a data-driven price estimate with market comparison and a downloadable PDF report.</div>
    </div>""", unsafe_allow_html=True)

    # ── Session state init
    if 'predicted' not in st.session_state:
        st.session_state.predicted     = None
        st.session_state.comparables   = None
        st.session_state.avg_comp      = None
        st.session_state.diff_pct      = None
        st.session_state.pred_location = None
        st.session_state.pred_sqft     = None
        st.session_state.pred_bhk      = None
        st.session_state.pred_bath     = None
        st.session_state.pred_loc_avg  = None
        st.session_state.pred_premium  = None
        st.session_state.pred_s_p_bhk  = None

    locations = sorted([l for l in df['location'].unique() if l != 'other'])

    # ── Layout
    left, right = st.columns([1,1], gap="large")

    with left:
        st.markdown('<div class="sec-hdr">Property Configuration</div>', unsafe_allow_html=True)

        location   = st.selectbox("📍 Neighbourhood / Location", locations, key="sel_loc")
        total_sqft = st.slider("📐 Total Built-up Area (sq ft)", 500, 10000, 1500, step=50, key="sl_sqft")
        bhk        = st.slider("🛏️ Bedrooms (BHK)", 1, 8, 3, key="sl_bhk")
        bath       = st.slider("🛁 Bathrooms", 1, 8, 2, key="sl_bath")

        sel_loc_avg  = loc_avg_map.get(location, city_avg)
        loc_premium  = sel_loc_avg / city_avg
        sqft_per_bhk = total_sqft / bhk if bhk > 0 else total_sqft

        # Live computed features
        st.markdown(f"""
        <div class="prop-summary" style="margin-top:1rem;">
            <div class="prop-summary-title">⚙️ Computed ML Features</div>
            <div class="prop-grid">
                <div class="prop-item">
                    <span class="prop-item-lbl">Location Avg. Price</span>
                    <span class="prop-item-val">₹{sel_loc_avg:.1f}L</span>
                </div>
                <div class="prop-item">
                    <span class="prop-item-lbl">Location Premium</span>
                    <span class="prop-item-val">{loc_premium:.2f}×</span>
                </div>
                <div class="prop-item">
                    <span class="prop-item-lbl">Sqft per BHK</span>
                    <span class="prop-item-val">{sqft_per_bhk:.0f} sq ft</span>
                </div>
                <div class="prop-item">
                    <span class="prop-item-lbl">City Avg. Price</span>
                    <span class="prop-item-val">₹{city_avg:.1f}L</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Buttons
        b1, b2 = st.columns([3,2], gap="small")
        with b1:
            predict_btn = st.button("🔮 Predict Price", use_container_width=True)
        with b2:
            st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
            reset_btn = st.button("↺ Reset", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if reset_btn:
            st.session_state.predicted     = None
            st.session_state.comparables   = None
            st.session_state.avg_comp      = None
            st.session_state.diff_pct      = None
            st.rerun()

        if predict_btn:
            feats = np.array([[total_sqft, bhk, bath, sel_loc_avg, loc_premium, sqft_per_bhk]], dtype=float)
            feat_norm = (feats - mean_vals) / std_vals
            pred = (np.dot(feat_norm, W) + b).item()
            pred = max(pred, 5.0)

            with st.spinner("⚡ Running model..."):
                time.sleep(0.5)

            comps = df[
                (df['location']==location) & (df['bhk']==bhk) &
                (df['total_sqft'].between(total_sqft*0.8, total_sqft*1.2))
            ][['location','total_sqft','bhk','bath','price']].head(8)

            avg_c   = comps['price'].mean() if not comps.empty else None
            diff_p  = ((pred - avg_c) / avg_c * 100) if avg_c else None

            st.session_state.predicted     = pred
            st.session_state.comparables   = comps
            st.session_state.avg_comp      = avg_c
            st.session_state.diff_pct      = diff_p
            st.session_state.pred_location = location
            st.session_state.pred_sqft     = total_sqft
            st.session_state.pred_bhk      = bhk
            st.session_state.pred_bath     = bath
            st.session_state.pred_loc_avg  = sel_loc_avg
            st.session_state.pred_premium  = loc_premium
            st.session_state.pred_s_p_bhk  = sqft_per_bhk

    # ─── Right column: Results
    with right:
        st.markdown('<div class="sec-hdr">Valuation Result</div>', unsafe_allow_html=True)

        if st.session_state.predicted is None:
            st.markdown("""
            <div class="empty-state">
                <div class="empty-state-icon">🔮</div>
                <div style="font-size:1rem; font-weight:600; color:#4b5563;">Configure &amp; Predict</div>
                <div style="font-size:0.85rem; margin-top:0.4rem; color:#374151;">
                    Set your property details on the left<br>and click <b style="color:#a78bfa;">Predict Price</b>
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            pred = st.session_state.predicted

            # ── Prediction card
            st.markdown(f"""
            <div class="pred-result">
                <div class="pred-label">Estimated Market Value</div>
                <div class="pred-price">₹ {pred:.2f} Lakhs</div>
                <div class="pred-crore">≈ ₹ {pred/100:.3f} Crores</div>
                <div class="pred-badge">Linear Regression · R² {r2:.4f} · NumPy from scratch</div>
            </div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Property Summary Card
            st.markdown(f"""
            <div class="prop-summary">
                <div class="prop-summary-title">📋 Property Summary</div>
                <div class="prop-grid">
                    <div class="prop-item">
                        <span class="prop-item-lbl">Location</span>
                        <span class="prop-item-val">{st.session_state.pred_location}</span>
                    </div>
                    <div class="prop-item">
                        <span class="prop-item-lbl">Total Area</span>
                        <span class="prop-item-val">{st.session_state.pred_sqft:,} sq ft</span>
                    </div>
                    <div class="prop-item">
                        <span class="prop-item-lbl">BHK</span>
                        <span class="prop-item-val">{st.session_state.pred_bhk} BHK</span>
                    </div>
                    <div class="prop-item">
                        <span class="prop-item-lbl">Bathrooms</span>
                        <span class="prop-item-val">{st.session_state.pred_bath}</span>
                    </div>
                    <div class="prop-item">
                        <span class="prop-item-lbl">Price per Sqft</span>
                        <span class="prop-item-val">₹{pred*100000/st.session_state.pred_sqft:,.0f}</span>
                    </div>
                    <div class="prop-item">
                        <span class="prop-item-lbl">Location Premium</span>
                        <span class="prop-item-val">{st.session_state.pred_premium:.2f}×</span>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

            # ── Market tag
            if st.session_state.avg_comp is not None:
                dp = st.session_state.diff_pct
                if abs(dp) < 5:
                    tag_cls, tag_icon, tag_txt = "fair","⚖️",f"Fair Value — within 5% of market avg"
                elif dp > 0:
                    tag_cls, tag_icon, tag_txt = "above","🔺",f"{dp:.1f}% Above Market Average"
                else:
                    tag_cls, tag_icon, tag_txt = "below","🔻",f"{abs(dp):.1f}% Below Market Average"
                st.markdown(f"""
                <div style="text-align:center;">
                    <span class="market-tag {tag_cls}">{tag_icon} {tag_txt}</span>
                </div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Download PDF
            comps = st.session_state.comparables
            pdf_bytes = generate_pdf_report(
                st.session_state.pred_location,
                st.session_state.pred_sqft,
                st.session_state.pred_bhk,
                st.session_state.pred_bath,
                pred,
                st.session_state.pred_loc_avg,
                st.session_state.pred_premium,
                st.session_state.pred_s_p_bhk,
                comps if not comps.empty else None,
                st.session_state.avg_comp,
                st.session_state.diff_pct,
                r2
            )
            fname = f"PropVista_Report_{st.session_state.pred_location.replace(' ','_')}_{st.session_state.pred_bhk}BHK.pdf"
            st.markdown('<div class="dl-btn">', unsafe_allow_html=True)
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name=fname,
                mime="application/pdf",
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

    # ── Comparable Listings (full width below)
    if st.session_state.predicted is not None:
        comps = st.session_state.comparables
        st.markdown('<div class="sec-hdr">Similar Listings in Dataset</div>', unsafe_allow_html=True)
        if comps is not None and not comps.empty:
            display = comps.rename(columns={
                'location':'Location','total_sqft':'Area (sq ft)',
                'bhk':'BHK','bath':'Bathrooms','price':'Price (Lakhs)'
            }).reset_index(drop=True)
            st.dataframe(display, use_container_width=True, hide_index=True)
            ac = st.session_state.avg_comp
            c1,c2,c3 = st.columns(3)
            c1.metric("Comparable Avg Price", f"₹{ac:.1f}L")
            c2.metric("Your Estimate",         f"₹{pred:.1f}L")
            c3.metric("Difference",            f"{st.session_state.diff_pct:+.1f}%")
        else:
            st.info("No comparable listings found for this exact configuration. Try adjusting BHK or location.")

# ── Footer
st.markdown("""
<div class="footer">
    🏙️ PropVista — Bengaluru Real Estate Intelligence &nbsp;|&nbsp;
    Built with Streamlit · Plotly · NumPy · ReportLab &nbsp;|&nbsp;
    ML model trained from scratch using Gradient Descent
</div>""", unsafe_allow_html=True)