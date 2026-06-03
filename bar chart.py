import matplotlib.pyplot as plt
import numpy as np

subjects = ["Math", "Physics", "Chemistry"]
marks_sem1 = [85, 78, 88]
marks_sem2 = [90, 82, 91]

x = np.arange(len(subjects))

plt.bar(x - 0.2, marks_sem1, width=0.4, label="Sem 1")
plt.bar(x + 0.2, marks_sem2, width=0.4, label="Sem 2")

plt.xticks(x, subjects)

plt.title("Semester")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()

plt.show()