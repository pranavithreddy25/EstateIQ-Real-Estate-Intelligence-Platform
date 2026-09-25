# EstateIQ — Real Estate Intelligence & Property Analytics Platform

> **See the market differently.**
> *Smarter property decisions, backed by data.*

EstateIQ is a serious, production-ready PropTech platform designed for real-world real estate investors, home buyers, renters, property owners, and agents.

---

## 🌟 Key Features

1. **Apple-Inspired Minimalist Interface**: Clean typography (Inter font stack), spacious card elevation, glassmorphism header, and restrained financial indicator badge accents.
2. **"I Have ₹80 Lakh" Budget Experience**: Budget-first discovery engine ranking top Hyderabad localities (Kokapet, Narsingi, Tellapur, Gachibowli, etc.) and properties matched to user financial goals.
3. **Explainable Investment Score (0–100)**: 6-factor weighted algorithm evaluating Gross Yield (30%), Growth (25%), Location Quality (15%), Budget Fit (15%), Demand (10%), and Condition (5%) with explicit reasoning.
4. **Institutional Financial Calculators**:
   - **Gross & Net Rental Yield Engine** (factoring vacancy & maintenance expenses)
   - **Mortgage EMI & Repayment Schedule Generator**
   - **10-Year Real Estate ROI Engine**
   - **Buy vs Rent Comparative Simulator** (ownership equity vs renting + index fund investing)
   - **ML Automated Property Price Valuation Engine**
5. **No-API First Architecture**: Operates self-contained with local coordinate visualizers and calculation engines without requiring paid API keys, with modular adapter interfaces for future Google Maps integration.
6. **Multi-Role Portals**:
   - **Public Discovery**: Multi-criteria filters, property cards, local visualizer map
   - **User Workspace**: Saved properties, saved search criteria, lead tracking
   - **Owner Portal**: Property submission workflow, listing manager
   - **Agent Portal**: Active listing metrics, buyer lead inbox & status workflow
   - **Admin Console**: Executive metrics, listing verification queue (Approve/Reject), Ad Slot Manager
7. **Monetization & Ad Infrastructure**: Built-in `AdSlot` components and schemas for advertisements, featured listings, lead packages, and subscriptions.
8. **Power BI Ready Exporter**: Includes automated CSV exporter script for building executive, market, and investment dashboards.

---

## 📁 Project Architecture

```
estateiq/
├── app/
│   ├── __init__.py          # Flask Application Factory & Jinja filters
│   ├── extensions.py       # SQLAlchemy, LoginManager, CSRF
│   ├── models/             # PostgreSQL-compatible ORM models
│   ├── routes/             # Blueprints (public, properties, investment, market, auth, user, owner, agent, admin)
│   ├── analytics/          # Yield, EMI, ROI, Buy vs Rent & Scoring engines
│   ├── ml/                 # Scikit-learn ML Price Predictor
│   └── utils/              # Formatters, SEO JSON-LD schema, Ad helpers
├── scripts/
│   ├── generate_dataset.py # Locality & property dataset generator
│   ├── seed_database.py    # Database table initializer & seed script
│   ├── export_powerbi.py   # Power BI CSV exporter
│   └── train_ml_model.py   # Retrains machine learning price predictor
├── static/
│   ├── css/style.css       # Custom design system tokens & animations
│   └── uploads/            # Property image storage
├── templates/              # Jinja HTML5 responsive layouts
├── tests/                  # Automated unit test suite
├── config.py               # Dev (SQLite) & Prod (PostgreSQL) configs
├── requirements.txt        # Python dependencies
├── run.py                  # Entry point
└── README.md
```

---

## 🚀 Quick Setup & Local Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Synthetic Dataset & Train ML Model
```bash
python scripts/generate_dataset.py
python scripts/train_ml_model.py
```

### 3. Seed SQLite Database
```bash
python scripts/seed_database.py
```

### 4. Run Automated Test Suite
```bash
python -m unittest discover tests
```

### 5. Launch EstateIQ Server
```bash
python run.py
```
Open **http://127.0.0.1:5000** in your browser.

---

## 🔑 Demo Accounts

| Role | Email | Password |
|---|---|---|
| **Admin** | `admin@estateiq.in` | `Admin@123` |
| **Agent** | `rajesh.agent@estateiq.in` | `Agent@123` |
| **Owner** | `srinivas.owner@gmail.com` | `Owner@123` |
| **Buyer** | `ananya.buyer@gmail.com` | `Buyer@123` |

---

## 📊 Exporting Data to Power BI

Run the automated Power BI CSV exporter:
```bash
python scripts/export_powerbi.py
```
Generated CSV files will be written to `data/exports/`:
- `properties_export.csv`
- `locations_export.csv`
- `price_history_export.csv`
- `leads_export.csv`

---

## 🛡️ Production Deployment (Render / Railway / VPS / Docker)

Set environment variables in production:
```env
FLASK_ENV=production
SECRET_KEY=your-production-super-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/estateiq_db
```
The SQLAlchemy ORM automatically switches to PostgreSQL without code modifications.
