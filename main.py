# TODO: Import NumPy
import numpy as np

# TODO: Read two sets of exam scores of five students from user input
# and store the scores into two NumPy arrays
exam1 = np.array(list(map(int, input().split())))
exam2 = np.array(list(map(int, input().split())))

# TODO: Compute the average scores for each of the five students
averages = (exam1 + exam2) / 2

# TODO: Output "Average scores: " followed by the NumPy array of the average scores
print("Average scores:", averages)

# TODO: Count the number of average scores that are >= 80
count_80_or_higher = np.count_nonzero(averages >= 80)

# TODO: Output "Number of students who received 80 and above: " followed by the count
print("Number of students who received 80 and above:", count_80_or_higher)
