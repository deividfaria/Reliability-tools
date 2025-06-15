import numpy as np
import matplotlib.pyplot as plt

class Weibull_Distribution:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        
    def HF(self, xvals):
        return (self.beta / self.alpha) * (xvals / self.alpha) ** (self.beta - 1)

class Exponential_Distribution:
    def __init__(self, Lambda):
        self.Lambda = Lambda
    
    def HF(self, xvals):
        return np.full_like(xvals, self.Lambda)

# Dados
xvals = np.linspace(0.01, 1000, 1000)

# Curvas
infant_mortality = Weibull_Distribution(alpha=400,beta=0.7).HF(xvals)
random_failures = Exponential_Distribution(Lambda=0.005).HF(xvals)
wear_out = Weibull_Distribution(alpha=1000, beta=50).HF(xvals)

combined = infant_mortality + random_failures + wear_out

# Limites dos trechos
t1, t2 = 100, 900

plt.figure(figsize=(12,7))
# plt.style.use('seaborn-whitegrid')  # comentar se causar erro

# Fundo cinza claro
plt.gca().set_facecolor("#F0F0F0")

# Áreas coloridas para cada trecho com transparência
plt.axvspan(0, t1, color='red', alpha=0.1, label='Early Failures Region')
plt.axvspan(t1, t2, color='green', alpha=0.1, label='Random Failures Region ')
plt.axvspan(t2, xvals[-1], color='blue', alpha=0.1, label='Wear Out Failures Region')

# Plot das curvas individuais
plt.plot(xvals, infant_mortality, label='Early Failures Distribution', color='red', linewidth=3.5)
plt.plot(xvals, random_failures, label='Random Failures Distribution', color='green', linewidth=3.5)
plt.plot(xvals, wear_out, label='Wear Out Distribution', color='blue', linewidth=3.5)

# Plot da curva combinada
plt.plot(xvals, combined, linestyle='--', label='Combined Hazard Rate', color='black', linewidth=5)

# Adicionando textos nas regiões
plt.text(t1/2, max(combined)*0.5, r'$\beta < 1$', color='red', fontsize=30, fontweight='bold', ha='center')
plt.text((t1+t2)/2, max(combined)*0.5, r'$\beta = 1$', color='green', fontsize=30, fontweight='bold', ha='center')
plt.text((t2 + xvals[-1])/2, max(combined)*0.5, r'$\beta > 1$', color='blue', fontsize=39, fontweight='bold', ha='center')

# Configurações do gráfico
plt.legend(fontsize=28)
plt.xlabel('Time',fontweight='bold', fontsize=30)
plt.ylabel('Hazard (t)',fontweight='bold', fontsize=30)
plt.xticks([])  # remove os números do eixo x
plt.yticks([])  # remove os números do eixo y
plt.xlim(0, 1000)
plt.ylim(bottom=0)
plt.grid(True)

plt.show()
