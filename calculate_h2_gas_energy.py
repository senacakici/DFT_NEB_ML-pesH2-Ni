from ase import Atoms
from gpaw import GPAW, PW

# H2 gaz molekülü tanımı (boşlukta)
d = 0.74  # tipik bağ uzunluğu
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, d]], cell=[6, 6, 6], pbc=False)

# GPAW hesaplayıcısı
calc = GPAW(mode=PW(400), xc='PBE', txt='h2_gas_output.txt')
h2.calc = calc

# Enerjiyi hesapla
energy = h2.get_potential_energy()

# Sonucu dosyaya yaz
with open('h2_gas_energy.txt', 'w') as f:
    f.write(f'{energy:.6f}\n')

print(f'H2 gaz fazı enerjisi: {energy:.6f} eV')

