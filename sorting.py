# practice sorting algorithm
# problem 1
# Problem: Sort an Array of Student Scores
def bubble_sort_student_scores(scores:list) -> list:
    n = len(scores)
    # handle edge cases
    if(n <= 1):
        return scores
    # algorithm implementation
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if scores[j] > scores[j+1]:
                scores[j],scores[j+1] = scores[j+1],scores[j]
                swapped = True
        if(not swapped):
            break
    return scores
# print(bubble_sort_student_scores([88, 95, 70, 100, 92, 85, 78, 84, 65, 78]))
# *******************************
# problem 2
# Problem: Sort an Array of Objects by a Key
students = [
  {"name": "Alice", "score": 88},
  {"name": "Bob", "score": 95},
  {"name": "Charlie", "score": 70},
  {"name": "David", "score": 100},
  {"name": "Eve", "score": 92}
]
def bubble_sort_students(students:list) -> list:
    n = len(students) 
    # handle edge case
    if(n < 2):
        return students
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if students[j]["score"] > students[i]["score"]:
                students[j]["score"],students[j+1]["score"] = students[j+1]["score"],students[j]["score"]
                swapped = True
        if(not swapped):
            return students
    return students
s = [{"name": "Eve", "score": 92}]
print(bubble_sort_students(s))
