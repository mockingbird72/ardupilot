import numpy as np
import pandas as pd

df = pd.read_csv('../logfile/1_gyro_latest.csv')

num = 10
num2 = 10
tmpx = 0
tmpy = 0
tmpz = 0
print(df.describe())

df1 = pd.DataFrame(columns=['x', 'y', 'z'])
df2 = pd.DataFrame(columns=['x', 'y', 'z'])
df3 = pd.DataFrame(columns=['x', 'y', 'z'])
#print(df['x'][0], " ",df['x'][1] )

#f = open("../../logfile/gap_1_gyro_latest.csv", 'w')

#f.writelines(['x', ',', 'y',',', 'z', '\n'])
for i in range(1, int(len(df['x']))):
    a = abs(df['x'][i] - df['x'][i-1])
    b = abs(df['y'][i] - df['y'][i-1])
    c = abs(df['z'][i] - df['z'][i-1])
    a= round(a,10)
    b= round(b,10)
    c= round(c,10)
    data_to_insert= {'x':a, 'y':b, 'z':c}
    df1= df1.append(data_to_insert, ignore_index=True)

    if (i>num):
        a1 = abs(df['x'][i] - df['x'][i-num])
        b1 = abs(df['y'][i] - df['y'][i-num])
        c1 = abs(df['z'][i] - df['z'][i-num])
        a1 = round(a1, 10)
        b1 = round(b1, 10)
        c1 = round(c1, 10)
        data_to_insert2= {'x':a1, 'y':b1, 'z':c1}
        df2= df2.append(data_to_insert2, ignore_index=True)  


    tmpx = tmpx + df['x'][i]
    tmpy = tmpy + df['y'][i]
    tmpz = tmpz + df['z'][i]

    if i%num2 ==0:
        a2 = tmpx / num2
        b2 = tmpy / num2
        c2 = tmpz / num2
        a2 = round(a2, 10)
        b2 = round(b2, 10)
        c2 = round(c2, 10)
        data_to_insert3= {'x':a2, 'y':b2, 'z':c2}
        df3= df3.append(data_to_insert3, ignore_index=True) 
        tmpx = 0
        tmpy = 0
        tmpz = 0


print(df1.describe())

print(df2.describe())

print(df3.describe())

#print('x_mean -> ',df1['x'].mean(), 'y_mean -> ', df1['y'].mean(), 'z_mean -> ', df1['z'].mean())
#print('x_min -> ',df1['x'].min(), 'y_min -> ', df1['y'].min(), 'z_min -> ', df1['z'].min())
#print('x_max -> ',df1['x'].max(), 'y_max -> ', df1['y'].max(), 'z_max -> ', df1['z'].max())
#print('x_std -> ',df1['x'].std(), 'y_std -> ', df1['y'].std(), 'z_std -> ', df1['z'].std())
    #f.writelines([str(a), ',', str(b), ',', str(c), '\n']) 
    
#f.close()

#df2 = pd.read_csv("../../logfile/gap_1_gyro_latest.csv")

#print(df2.describe())
