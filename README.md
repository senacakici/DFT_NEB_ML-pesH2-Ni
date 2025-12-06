# 🧠 ML-Enhanced DFT Modeling of H₂ on Ni(111)

This project combines first-principles **DFT simulations** and **Machine Learning** to estimate the **Potential Energy Surface (PES)** and dissociation barrier of hydrogen on a Ni(111) surface.

It was developed as part of a research portfolio for PhD applications in **computational surface chemistry**, including programs such as the one at **Leiden University**.

---

## 🔬 Key Highlights

- ✅ DFT calculations using GPAW for multiple H₂ heights
- ✅ Adsorption energy computation and PES visualization
- ✅ NEB pathway modeling for dissociative adsorption
- ✅ Gaussian Process Regression (GPR) to model the PES
- ✅ Model performance evaluated via LOOCV, RMSE, R²

---

## 📓 Full Results in Notebook

➡️ All steps, codes, results, and visual insights are documented in  
**[`Project_Jupyter.ipynb`](./Project_Jupyter.ipynb)**

This includes:

- Geometry generation and GPAW setup  
- PES data collection and adsorption energy analysis  
- NEB reaction barrier profiling  
- GPR model training, prediction, and uncertainty analysis  
- Physical interpretation of the results

---

## 🧪 Future Improvements

- Perform vibrational analysis for transition states  
- Compare different functionals (PBE, RPBE, SCAN, etc.)  
- Expand dataset to 2D/3D PES mapping  
- Benchmark multiple ML models (SVR, NN, RF...)  
- Perform Bader charge analysis for charge transfer insights

---

## 👨‍🔬 Author

This project was created by Sena Çakıcı as part of an independent research initiative to explore ML-assisted quantum simulations of surface reactions.

> Feel free to check out the notebook for full reproducibility and discussion.
