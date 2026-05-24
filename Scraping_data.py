
from pathlib import Path
import pickle
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from playwright.sync_api import sync_playwright



CACHE_DIR = Path("project_cache")
PROJECT_CACHE_FILE = CACHE_DIR / "project_cache.pkl"
CLEANED_CACHE_FILE = CACHE_DIR / "project_cache_cleaned.pkl"

URLS = {
    "unemployment": "https://www.macrotrends.net/datasets/1316/us-national-unemployment-rate",
    "inflation": "https://www.macrotrends.net/datasets/2497/historical-inflation-rate-by-year",
    "debt_to_gdp": "https://www.macrotrends.net/datasets/1381/debt-to-gdp-ratio-historical-chart",
    "housing_starts": "https://www.macrotrends.net/datasets/1314/housing-starts-historical-char",
}

INDIVIDUAL_CACHE_FILES = {
    "unemployment": CACHE_DIR / "unemployment.pkl",
    "inflation": CACHE_DIR / "inflation.pkl",
    "debt_to_gdp": CACHE_DIR / "debt_to_gdp.pkl",
    "housing_starts": CACHE_DIR / "housing_starts.pkl",
}

