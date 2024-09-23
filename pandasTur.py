import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3, 4], [6, 7, 8, 9]], columns=["D", "B", "E", "A"], index=[1, 2]
)

other = pd.DataFrame(
    [[10, 20, 30, 40], [60, 70, 80, 90], [600, 700, 800, 900]],
    columns=["A", "B", "C", "D"],
    index=[2, 3, 4],
)


print("df")

print(df)



print("other")
print(other)


print("******************")
print("inner join")


left, right = df.align(other, join="right", axis=1)

print("left which is The DataFrame df  is aligned with Other.")

print(left)


print("Right which is The DataFrame other is aligned with df.")
print(right)


print("******************")
print("outer join")


left, right = df.align(other, join="outer", axis=1)

print("left which is The DataFrame df  is aligned with Other.")

print(left)


print("Right which is The DataFrame other is aligned with df.")
print(right)
