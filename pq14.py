import pandas as pd 

Names   = ["Ravi", "Asha", "Meera", "John"]
Salary  = [45000, 52000, 61000, 47000]
Dept    = ["HR", "Finance", "IT", "IT"]


data={'Names': Names, 
      'Salary': Salary, 
      'Dept':Dept}

df=pd.DataFrame(data)

df['Bonus']=0.1*(df['Salary'])
print(df)
print(f"The highest salary is:")
print(df['Salary'].max())
print("The average salary is")
print(df['Salary'].mean())

count=0

for i in Dept:
    if i=='IT':
        count+=1
        
print(f"The number of employees in IT are {count}")

df=df.sort_values(by='Salary', ascending=False)

print("Sorted Data:")
print(df)