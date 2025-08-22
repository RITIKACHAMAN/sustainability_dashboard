# 🌱 Sustainability Dashboard

**Live App**: [Click here to view on Streamlit Cloud](https://sustainabilitydashboard-8dnd2a5stimk3aw4f8bqnd.streamlit.app/)
# Sustainability Dashboard (Textile Company)

This project is a Streamlit-based interactive dashboard that demonstrates all must-have features described in the assignment: KPI tiles (Energy, Water, Waste, Emissions), Overall performance, filters, drill-down views, anomaly alerts, export, and more.

## Files
- `app.py` — Main Streamlit app (single-file; contains UI, charts, export, anomaly detection, persistent filters).
- `data_gen.py` — Optional: generate a sample CSV dataset for testing.
- `requirements.txt` — Python dependencies.

## Setup & Run
1. Create and activate a Python virtual environment (recommended):

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Generate sample data:

   ```bash
   python data_gen.py --out sample_data.csv --start 2024-01-01 --end 2024-06-30
   ```

4. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

5. The dashboard opens at http://localhost:8501 by default.
