import matplotlib.pyplot as plt
import numpy as np

labels = ['512', '1024', '2048']
pytorch = [5146, 9438, 18928]
share = [3582, 7156, 14238]

x = np.arange(len(labels))  
width = 0.3  

fig, ax = plt.subplots()
rects1 = ax.bar(x + width/2, pytorch, width, label='Pytorch')
rects2 = ax.bar(x + 1.5*width, share, width, label='Share')

ax.set_xlabel('Batch Size')  # 设定x轴的单位为Batch Size
ax.set_ylabel('Memory Usage (MiB)')  # 设定y轴的单位为Memory Usage (MiB)
ax.set_title('SEP+TRACE')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.savefig('trace.png')  # 放在plt.show()之前
plt.show()