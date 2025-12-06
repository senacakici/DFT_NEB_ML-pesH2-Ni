import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pes_data.csv")
plt.plot(data['height'], data['energy'], marker='o', linestyle='-')
plt.xlabel('H2–Surface Height (Å)')
plt.ylabel('Total Energy (eV)')
plt.title('Potential Energy Surface')
plt.grid(True)
plt.show()


