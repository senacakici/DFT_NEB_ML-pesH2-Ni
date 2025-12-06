import os

def is_floatable(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Sadece sayısal dosya isimlerini filtrele
energy_files = []
for f in os.listdir():
    if f.startswith("calc_") and f.endswith(".txt"):
        val = f.replace("calc_", "").replace(".txt", "")
        if is_floatable(val):
            energy_files.append(f)

# Dosyaları sıralıyoruz
energy_files = sorted(energy_files, key=lambda x: float(x.replace("calc_", "").replace(".txt", "")))

# Sabit enerjileri al
with open("slab_energy.txt") as f:
    slab_energy = float(f.read().strip())

with open("h2_gas_energy.txt") as f:
    h2_gas_energy = float(f.read().strip())

# CSV oluştur
with open("pes_data.csv", "w") as f:
    f.write("height,adsorption_energy\n")
    for filename in energy_files:
        with open(filename) as ef:
            lines = ef.readlines()
            total_energy = None
            for line in lines:
                if "Extrapolated:" in line:
                    try:
                        total_energy = float(line.split()[-1])
                        break
                    except ValueError:
                        continue
        if total_energy is None:
            print(f"⚠️ Uyarı: {filename} içinde 'Extrapolated:' bulunamadı, atlandı.")
            continue
        height = float(filename.replace("calc_", "").replace(".txt", ""))
        E_ads = total_energy - slab_energy - h2_gas_energy
        f.write(f"{height},{E_ads:.6f}\n")

print("✅ pes_data.csv başarıyla oluşturuldu.")

