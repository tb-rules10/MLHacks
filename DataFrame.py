import pandas as pd

df1 = pd.DataFrame({'mark1': [10,40,15,40], 'mark2': [15,45,30,70]})
# print(df1)
df2 = pd.DataFrame({'mark1': [30,20,20,50], 'mark2': [20,25,30,30]})
# print(df2)

# frames = [df1, df2]
# result = pd.concat(frames)
# print("Merged DF :-\n", result)
#
# df3 = df2.add(df1, fill_value=0)
# df4 = df1.subtract(df2, fill_value=0)
# print("On Addition :-\n", df3)
# print("On Subtraction :-\n", df4)

df1 = df1.rename(columns={'mark1':'marks1'})
df2 = df2.rename(columns={'mark1':'marks1'})
print(df1)
print(df2)

print("\n")
df1 = df1.rename(index={0:'zero', 1:'one', 2:'two', 3:'three'})
df2 = df2.rename(index={0:'zero', 1:'one', 2:'two', 3:'three'})
print(df1)
print(df2)
