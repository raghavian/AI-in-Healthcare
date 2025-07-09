import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pdb

params = {'font.size': 20,
          'font.sans-serif': 'cmr10',
          'font.weight': 'bold',
          'axes.labelsize':24,
          'axes.titlesize':20,
#          'axes.labelweight':'heavy',
#          'axes.titleweight':'bold',
          'legend.fontsize': 22,
          'xtick.major.pad':'10'
         }
matplotlib.rcParams.update(params)

# Prepare the data
df = pd.read_csv('datasets.csv')
# Plot setup
plt.figure(figsize=(14, 8))
markers = {'vision': 'o', 'medical': 's'}
colors = {'vision': 'tab:blue', 'medical': 'tab:red'}

# Scatter by type
for t in df['type'].unique():
    subset = df[df['type'] == t]
    plt.scatter(subset['year'], subset['pixels'],
                label=t.capitalize(),
                marker=markers[t],
                color=colors[t],
                edgecolor='k',
                s=150,
                alpha=0.85)

# Annotate each point with uniform offset
for _, row in df.iterrows():
    plt.annotate(
        row['dataset'],
        xy=(row['year'], row['pixels']),
        xytext=(35, 5),
        textcoords='offset points',
        ha='center',
        va='bottom',
#        fontsize=9
    )

# Formatting
plt.yscale('log')
plt.ylim([10e6,10e19])
#plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Pixels (log scale)')
#plt.title('Total Number of Pixels per Dataset Over Time')
#plt.rcParams['axes.spines.right'] = False
#plt.gca().set_frame_on(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Dataset Type')
plt.tight_layout()
plt.savefig('dataset.pdf',dpi=150)
#plt.show()

