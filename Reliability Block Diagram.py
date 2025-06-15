import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams

# Define fonte Times New Roman para todo o plot
rcParams['font.family'] = 'Times New Roman'

def rbd_with_lambdaN(n):
    fig, ax = plt.subplots(figsize=(8, 2))

    rect_width = 1.0
    rect_height = 0.6
    spacing = 0.6

    positions = []
    labels = []

    if n <= 4:
        labels = [fr"$\lambda_{{{i+1}}}$" for i in range(n)]
    else:
        # Para n>4 mostra lambda_1, lambda_2, lambda_3, ..., lambda_N (N literal)
        labels = [fr"$\lambda_{{{i+1}}}$" for i in range(3)] + ['...'] + [r"$\lambda_N$"]

    # Posiciona os blocos
    for i in range(len(labels)):
        x = i * (rect_width + spacing)
        positions.append(x)

    # Desenha retângulos com labels
    for i, label in enumerate(labels):
        x = positions[i]
        rect = patches.Rectangle((x, 0), rect_width, rect_height,
                                 linewidth=3, edgecolor='black', facecolor='white')
        ax.add_patch(rect)

        ax.text(x + rect_width/2, rect_height/2, label,
                fontsize=36, ha='center', va='center')

    # Desenha setas entre blocos
    for i in range(len(labels) - 1):
        start_x = positions[i] + rect_width
        end_x = positions[i+1]
        y = rect_height / 2
        ax.annotate("",
                    xy=(end_x, y), xycoords='data',
                    xytext=(start_x, y), textcoords='data',
                    arrowprops=dict(arrowstyle="->", lw=3, color='black'),
                    )

    # Ajustes da figura
    ax.set_xlim(-0.5, positions[-1] + rect_width + 0.5)
    ax.set_ylim(-0.2, rect_height + 0.2)
    ax.axis('off')
    ax.set_aspect('equal')

  
    plt.show()

# Teste com N=10
rbd_with_lambdaN(10)
