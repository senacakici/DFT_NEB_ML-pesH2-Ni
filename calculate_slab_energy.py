from ase.io import read from gpaw import GPAW, PW from ase.optimize import BFGS

# Slab yapısını oku
slab = read('ni111.traj')

# GPAW hesaplayıcısını tanımla
calc = GPAW(mode=PW(400), xc='PBE', kpts=(3, 3, 1), txt='slab_output.txt')
slab.calc = calc

# Geometri optimizasyonu (isteğe bağlı, atlayabiliriz)
# opt = BFGS(slab)
# opt.run(fmax=0.05)

# Enerji hesapla
energy = slab.get_potential_energy()

# Sonucu dosyaya yaz
with open('slab_energy.txt', 'w') as f:
    f.write(f'{energy:.6f}\n')

print(f'Slab enerjisi: {energy:.6f} eV')

