import pandas as pd
import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

def load_data():
    data = {}

    # --- Siebel ---
    data["siebel_accounts"] = pd.read_csv(os.path.join(BASE_PATH, "siebel_accounts.csv"))
    data["siebel_assets"] = pd.read_csv(os.path.join(BASE_PATH, "siebel_assets.csv"))
    data["siebel_asset_attributes"] = pd.read_csv(os.path.join(BASE_PATH, "siebel_asset_attributes.csv"))

    # --- Antillia ---
    data["billing_accounts"] = pd.read_csv(os.path.join(BASE_PATH, "billing_accounts.csv"))
    data["billing_products"] = pd.read_csv(os.path.join(BASE_PATH, "billing_products.csv"))
    data["billing_product_attributes"] = pd.read_csv(os.path.join(BASE_PATH, "billing_product_attributes.csv"))

    # --- CSS ---
    data["css_customers"] = pd.read_csv(os.path.join(BASE_PATH, "css_customers.csv"))
    data["css_services"] = pd.read_csv(os.path.join(BASE_PATH, "css_services.csv"))
    data["css_billing"] = pd.read_csv(os.path.join(BASE_PATH, "css_billing.csv"))
    data["css_service_attributes"] = pd.read_csv(os.path.join(BASE_PATH, "css_service_attributes.csv"))

    # --- Mapping ---
    data["product_mapping"] = pd.read_csv(os.path.join(BASE_PATH, "product_master_mapping.csv"))
    data["attribute_mapping"] = pd.read_csv(os.path.join(BASE_PATH, "attribute_mapping.csv"))
    data["control_mapping"] = pd.read_csv(os.path.join(BASE_PATH, "control_logic_mapping.csv"))

    return data
