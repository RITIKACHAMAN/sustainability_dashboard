"""Generate a sample sustainability dataset for the dashboard."""
import argparse
import numpy as np
import pandas as pd

np.random.seed(42)

def generate(start='2024-01-01', end='2024-06-30'):
    dates = pd.date_range(start, end, freq='D')
    units = ['Unit A', 'Unit B', 'Unit C']
    departments = ['Spinning', 'Weaving', 'Dyeing', 'Finishing']
    machines = [f'M{str(i).zfill(3)}' for i in range(1, 11)]
    shifts = ['Morning', 'Evening', 'Night']

    rows = []
    for d in dates:
        for u in units:
            for dept in departments:
                for shift in shifts:
                    energy = int(np.random.normal(400, 60))
                    water = int(np.random.normal(2000, 300))
                    waste = int(np.random.normal(90, 25))
                    emissions = int(np.random.normal(700, 120))
                    rows.append({
                        'Date': d,
                        'Unit': u,
                        'Department': dept,
                        'Machine': np.random.choice(machines),
                        'Shift': shift,
                        'Energy': max(10, energy),
                        'Water': max(100, water),
                        'Waste': max(1, waste),
                        'Emissions': max(10, emissions)
                    })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='sample_data.csv')
    parser.add_argument('--start', default='2024-01-01')
    parser.add_argument('--end', default='2024-06-30')
    args = parser.parse_args()
    df = generate(args.start, args.end)
    df.to_csv(args.out, index=False)
    print(f'Wrote {len(df)} rows to {args.out}')