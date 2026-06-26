# 🏠 Bengaluru House Price Analytics

> An end-to-end machine learning project featuring exploratory data analysis, feature engineering, and a Linear Regression model built **from scratch using NumPy** — with a fully interactive Streamlit dashboard.

---

## ✨ Features

| Module | Highlights |
|--------|-----------|
| 🏠 **Dashboard** | KPI cards, price distribution, BHK breakdown, top locations, pipeline overview |
| 📊 **EDA & Insights** | Correlation heatmap, scatter plots, box/violin charts, location premium index |
| 🤖 **ML Model** | Training loss curve, predicted vs actual, residual distribution, learned weights |
| 🔮 **Price Predictor** | Real-time price estimation + comparable listings from dataset |

---

## 🗂️ Project Structure

```
bengaluru-house-price/
├── app.py                          # Streamlit dashboard (4 interactive pages)
├── Bengaluru_House_Data.csv        # Raw dataset (13,320 rows)
├── Preprocessing_EDA.ipynb         # Data cleaning & EDA notebook
├── Linear_Reg_Logistic_Reg.ipynb   # Model training notebook
├── requirements.txt
└── README.md
```

---

## 🧠 ML Pipeline

```
Raw Data (13,320 rows)
        │
        ▼
Preprocessing
  • Drop nulls, irrelevant columns (area_type, availability, society)
  • Parse BHK from size string
  • Convert sqft ranges (e.g., "1200-1500") to numeric midpoint
        │
        ▼
Feature Engineering
  • price_per_sqft  = (price × 100,000) / total_sqft
  • location_avg_price  = mean price per location
  • location_premium    = location_avg_price / city_avg_price
  • sqft_per_bhk        = total_sqft / bhk
        │
        ▼
Outlier Removal
  • sqft_per_bhk ≥ 300
  • bath < bhk + 3
        │
        ▼
Linear Regression (from scratch)
  • Gradient Descent: 5,000 epochs, lr = 0.001
  • Feature standardisation (zero-mean, unit-variance)
  • Loss: Mean Squared Error (MSE)
        │
        ▼
Interactive Prediction
  • Select location, sqft, BHK, bath → instant price estimate
  • Compared against similar listings in dataset
```

---

## 📊 Dataset

| Field | Description |
|-------|-------------|
| `area_type` | Super built-up / Plot / Built-up / Carpet |
| `availability` | Ready to move or possession date |
| `location` | Neighbourhood in Bengaluru (1,305 unique) |
| `size` | e.g., "2 BHK", "3 Bedroom" |
| `society` | Housing society name |
| `total_sqft` | Area in sq ft (ranges converted to midpoint) |
| `bath` | Number of bathrooms |
| `balcony` | Number of balconies |
| `price` | Price in Lakhs (₹) |

**Engineered features:** `bhk`, `price_per_sqft`, `location_avg_price`, `location_premium`, `sqft_per_bhk`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bengaluru-house-price.git
cd bengaluru-house-price
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📦 Requirements

```
streamlit>=1.35.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
```

Create `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Or use the minimal set above.

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | ~0.70+ |
| RMSE | ~₹60–90 Lakhs |
| Training Epochs | 5,000 |
| Learning Rate | 0.001 |
| Train/Test Split | 80 / 20 |

> **Note:** The model is implemented entirely with NumPy — no scikit-learn for training. This demonstrates understanding of gradient descent at a fundamental level.

---

## 🖥️ UI Pages

### 🏠 Dashboard
- Animated gradient hero banner
- 5 KPI metric cards (total listings, locations, median price, sqft, baths)
- Price distribution histogram
- BHK donut chart
- Top 15 locations bar chart
- Pipeline overview cards

### 📊 EDA & Insights
- **Correlations tab:** Feature heatmap + price correlation bar chart
- **Sqft vs Price tab:** Coloured scatter plot + distribution histograms
- **BHK vs Price tab:** Notched box plots + violin charts by bathroom count
- **Location Intel tab:** Avg price bar chart + location premium index

### 🤖 ML Model
- **Training Loss tab:** MSE curve over 5,000 epochs with final loss annotation
- **Predictions vs Actual tab:** Scatter with perfect-prediction reference line + residual histogram
- **Feature Weights tab:** Learned weight bar chart + equation display

### 🔮 Predict Price
- Dropdowns & sliders for location, sqft, BHK, bath
- Real-time computed feature preview (location premium, sqft/BHK)
- Animated glowing prediction result card (Lakhs + Crores)
- Comparable listings table with above/below-market indicator

---

## 🎨 Design System

| Element | Style |
|---------|-------|
| Background | Deep navy `#0f0c29` → `#1a1a2e` |
| Accent | Purple gradient `#7c3aed` → `#4f46e5` |
| Text | Slate `#e2e8f0` / Muted `#94a3b8` |
| Cards | Glass-morphism with hover lift animation |
| Charts | Plotly with dark transparent canvas |
| Fonts | Inter (body) + Poppins (headings) |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  Built with ❤️ using Streamlit • Plotly • NumPy • Pandas
</div>
