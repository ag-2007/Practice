Name = ['Asha', 'Ravi', 'Leela', 'Kiran', 'Meena']
Math = [78, 85, 62, 90, 74]
Physics = [82, 79, 70, 88, 80]

data={'Name':Name,
      'Math':Math,
      'Physics':Physics}

import pandas as pd

df = pd.DataFrame(data)

Math_avg=df['Math'].mean()
Phy_avg=df['Physics'].mean()

print("Average Math score:", Math_avg)
print("Average Physics score:", Phy_avg)

Result=[]

for i in range(len(df)):
    if df.loc[i, 'Math'] > 70 and df.loc[i, 'Physics'] > 70:
        Result.append('Pass')
    else:
        Result.append('Fail')

df['Result']=Result

import matplotlib.pyplot as plt
plt.bar(df['Name'], df['Math'], color='blue',edgecolor='black')
plt.legend(['Math'])
plt.xlabel('Students')
plt.ylabel('Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Student Scores in Math')
plt.show()