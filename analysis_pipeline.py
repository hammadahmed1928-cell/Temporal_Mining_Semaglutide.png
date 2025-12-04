# Project: Temporal Knowledge Mining of Adverse Events
# Target: Semaglutide (Ozempic) - Tracking report velocity over time
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. MINE THE DATA (The "Harvesting" Phase)
API_URL = "https://api.fda.gov/drug/event.json"
PARAMS = {
    'search': 'patient.drug.openfda.generic_name:"SEMAGLUTIDE"',
    'count': 'receivedate', # We want the Timeline
    'limit': 1000
}

response = requests.get(API_URL, params=PARAMS)
data = response.json()

# 2. PROCESS (The "Temporal" Phase)
df = pd.DataFrame(data['results'])
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')

# 3. VISUALIZE (The "Insight" Phase)
plt.figure(figsize=(10, 5))
plt.plot(df['time'], df['count'], color='#2E86C1', linewidth=2, label='Adverse Event Reports')
plt.fill_between(df['time'], df['count'], color='#2E86C1', alpha=0.1)

plt.title('Temporal Velocity of Medical Knowledge: Semaglutide Safety Signals', fontsize=12, fontweight='bold')
plt.xlabel('Timeline', fontsize=10)
plt.ylabel('Knowledge Inflow (Reports/Day)', fontsize=10)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
