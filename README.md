# AA Crew Sequence Risk Classifier
### EPPS-American Airlines Data Challenge — GROW 26.2

## Problem
Identify airport pairs (A → DFW → B) that represent high-risk
pilot sequences due to weather-driven cascading delays.

## Approach
Binary classification model (XGBoost) trained on flight-level
delay data and weather observations to predict sequence risk.

## Architecture
[Paste your architecture diagram here]

## Data Sources
- BTS On-Time Performance (transtats.bts.gov)
- OpenSky Network REST API (opensky-network.org)
- NOAA Storm Events Database

## Project Structure
[Paste folder tree here]

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_data_exploration.ipynb
```

## Results
- PR-AUC: X.XX
- F1-Score: X.XX
- Top risky pairs: [table]

## Team
Sruthi, Krishna, Nikhil — MS Business Analytics & AI, UTD