#Draw names in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")
# Import library
import matplotlib.pyplot as plt

# code
def plot_names(names):
    fig, ax = plt.subplots()

    ax.text(0.5, 0.5, '\n'.join(names), ha='center', va='center', fontsize=24, fontstyle='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Integrantes del Grupo')

    plt.show()

names = ['Alejandro', 'Juan Carlos', 'Sebastián']
plot_names(names)