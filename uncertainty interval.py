import numpy as np
import matplotlib.pyplot as plt

# Configurações básicas
np.random.seed(42)
tempo = np.linspace(0, 100, 500)  # eixo X: tempo (pode ser número de amostras ou dias)
mtbf_nominal = 1000  # valor médio esperado de MTBF

# Função que modela a incerteza: grande no início, decresce com o tempo (exponencial decrescente)
def largura_incerteza(t, max_largura=600, decaimento=0.02):
    return max_largura * np.exp(-decaimento * t)

# Limites de confiança: nominal ± largura da incerteza
upper_confidence = mtbf_nominal + largura_incerteza(tempo)
lower_confidence = mtbf_nominal - largura_incerteza(tempo)

# Plotagem
plt.figure(figsize=(10,6))
plt.plot(tempo, np.full_like(tempo, mtbf_nominal), label='True MTBF', color='black', linewidth=5)
plt.plot(tempo, upper_confidence, label='Upper Confidence', color='red',  linewidth=3,linestyle='--')
plt.plot(tempo, lower_confidence, label='Lower Confidence', color='red',  linewidth=3, linestyle='--')



t1 = tempo[tempo <= 33]
t2 = tempo[(tempo > 33) & (tempo <= 66)]
t3 = tempo[tempo > 66]

# Correspondentes limites para cada região
lower1 = lower_confidence[tempo <= 33]
upper1 = upper_confidence[tempo <= 33]

lower2 = lower_confidence[(tempo > 33) & (tempo <= 66)]
upper2 = upper_confidence[(tempo > 33) & (tempo <= 66)]

lower3 = lower_confidence[tempo > 66]
upper3 = upper_confidence[tempo > 66]

# Preenchendo cada região com cor diferente
plt.fill_between(t1, lower1, upper1, color="#b22222", alpha=0.25, label='Prediction')  # vermelho fogo
plt.fill_between(t2, lower2, upper2, color="#d2691e", alpha=0.25, label='Assessment')  # laranja escuro (mais visível que amarelo)
plt.fill_between(t3, lower3, upper3, color="#228b22", alpha=0.25, label='Estimation')  # verde floresta








# Anotações para as regiões
plt.text(20, mtbf_nominal + 550, 'Prediction\nPaper Analysis', 
         color='black', ha='center', va='center', fontsize=28, fontweight='bold')

plt.text(50, mtbf_nominal + 350, 'Assessment\nIn-House Testing', 
         color='black', ha='center', va='center', fontsize=28, fontweight='bold')

plt.text(90, mtbf_nominal + 250, 'Estimation\nField Data', 
         color='black', ha='center', va='center', fontsize=28, fontweight='bold')

# Configurações dos eixos e título
plt.xticks([])  # remove os números do eixo x
plt.yticks([])  # remove os números do eixo y
plt.xlabel('Time',fontsize=28,fontweight='bold')
plt.ylabel('MTBF',fontsize=28,fontweight='bold')
plt.legend(fontsize=28)
plt.ylim(0, mtbf_nominal+700)

plt.show()
