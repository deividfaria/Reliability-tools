from matplotlib_venn import venn3
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))

# Criar o diagrama de Venn com interseções completas
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), 
          set_labels=('Prediction', 'Reliability Test', 'Field Data'))

# Definir contornos coloridos e preenchimento branco
colors = {'100': '#b22222',    # Prediction - vermelho
          '010': '#d2691e',    # Reliability Test - laranja
          '001': '#228b22'}    # Field Data - verde

for subset in ('100', '010', '001', '110', '101', '011', '111'):
    patch = v.get_patch_by_id(subset)
    if patch:
        patch.set_edgecolor(colors.get(subset, 'black'))  # cor do contorno
        patch.set_facecolor('white')                      # preenchimento branco
        patch.set_alpha(1)                                # sem transparência
        patch.set_linewidth(2)                            # espessura da linha

# Remover os números das interseções
for text in v.subset_labels:
    if text:
        text.set_visible(False)

# Ajustar os títulos dos conjuntos
for label in v.set_labels:
    label.set_fontsize(14)

plt.title('Reliability Engineering — Data Sources', fontsize=16)
plt.show()
