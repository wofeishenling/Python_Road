import  matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(12,3))
# plt.figure(figsize=(3,3))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.family'] = 'Times New Roman' # 全局字体样式
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=None)

'''
    X=Greek_labels
    Y=Geographical_descroptors
'''

ax1 = plt.subplot(131)
CCM_data = pd.read_excel("./CCM-data.xlsx", usecols=[1, 2, 3])
plt.title("A", fontsize=15, x=-0.14, y=1, fontweight='bold')
plt.xlim(0, 150)
plt.yticks([0,0.2,0.4,0.6,0.8,1], [0,0.2,0.4,0.6,0.8,1], size=10)
plt.ylim(0 - 0.06, 1 + 0.06)
plt.xlabel('L', fontsize=11, loc="center", fontstyle='italic')
plt.ylabel('ρ', fontsize=11, loc="center", fontstyle='italic')
l1,=plt.plot(CCM_data[["LibSize"]],CCM_data[["Geographical_descroptors:Greek_labels"]])
l2,=plt.plot(CCM_data[["LibSize"]],CCM_data[["Greek_labels:Geographical_descroptors"]])
plt.legend(handles=[l1, l2], loc='upper right', labels=['$\hat{X}(t)|M_{Y}$', '$\hat{Y}(t)|M_{X}$'],fontsize=7,frameon=False)

ax2 = plt.subplot(132)
predData2 = pd.read_excel("./Simplex_predict-data1.xlsx", usecols=[2, 3])
plt.title("B", fontsize=15, x=-0.23, y=1, fontweight='bold')
plt.xlabel('$\mathit{X(t)}$ (observed)', fontsize=11, loc="center")
plt.ylabel('$\hat{X}(t)|M_{Y}$ (estimated)', fontsize=11, loc="center")
plt.scatter(predData2[["Observations"]], predData2[["Predictions"]], alpha=0.8, marker='x', color='#1E76B4', s = 16)

ax3 = plt.subplot(133)
predData1 = pd.read_excel("./Simplex_predict-data2.xlsx", usecols=[2, 3])
plt.title("C", fontsize=15, x=-0.23, y=1, fontweight='bold')
plt.xlabel('$\mathit{Y(t)}$ (observed)', fontsize=11, loc="center")
plt.ylabel('$\hat{Y}(t)|M_{X}$ (estimated)', fontsize=11, loc="center")
plt.scatter(predData1[["Observations"]], predData1[["Predictions"]], alpha=0.8, marker='x', color='#FF861E', s = 16)

plt.savefig('./figure/experiment3/ex3_300dpi.jpg', bbox_inches='tight', dpi=300)
plt.savefig('./figure/experiment3/ex3_150dpi.jpg', bbox_inches='tight', dpi=150)
plt.savefig('./figure/experiment3/ex3_300dpi.png', bbox_inches='tight', dpi=300)
plt.savefig('./figure/experiment3/ex3_150dpi.png', bbox_inches='tight', dpi=150)
plt.savefig('./figure/experiment3/ex3_300dpi.tiff', bbox_inches='tight', dpi=300)
plt.savefig('./figure/experiment3/ex3_150dpi.tiff', bbox_inches='tight', dpi=150)
plt.savefig('./figure/experiment3/ex3_300dpi.svg', bbox_inches='tight', dpi=300)
plt.savefig('./figure/experiment3/ex3_150dpi.svg', bbox_inches='tight', dpi=150)
plt.show()
