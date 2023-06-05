import pandas as pd
import matplotlib.pyplot as plt
from japanmap import picture
import subprocess
FileName=r"SSDSE-C-2022.xlsx"
df=pd.read_excel(FileName, header=1)
df.head()
# df = pd.read_csv('data_dssdse\\SSDSE-B-2022.xlsx')
# df = df.set_index('都道府県')
df1=df[['都道府県','生うどん・そば']]
df1 = df1.set_index('都道府県')
df1=df1.drop('全国', axis=0)
df1.columns =['生うどんそば']
cmap = plt.get_cmap('Reds')
norm = plt.Normalize(vmin=df1.生うどんそば.min(), vmax=df1.生うどんそば.max()) 
fcol = lambda x: '#' + bytes(cmap(norm(x), bytes=True)[:3]).hex() 
plt.title('消費 生うどん・そば',fontname="Yu Gothic")
plt.rcParams['figure.figsize'] = 12, 12
plt.colorbar(plt.cm.ScalarMappable(norm, cmap))
plt.imshow(picture(df1.生うどんそば.apply(fcol)));
plt.savefig('udon.png')
subprocess.Popen(['start', 'udon.png'], shell=True)