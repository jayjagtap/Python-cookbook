"""
Jay Jagtap
You can unpack any iterable object into separate values
"""

record = ['Jay', 'Jagtap','Engineer', ('1','June','3002')]

fname, lname, _ , date = record

print(fname, lname, date)

# Output:
# Jay Jagtap ('1', 'June', '3002')

dd, mm, yy = date

print(yy)

# Upacking iterables using the * expression

record = ['History','Maths','Science','Geography','Biology']

subject1, *subjects, subject2 = record

print(f"{subject1}, {subject2}, {subjects}")

# Output: History, Biology, ['Maths', 'Science', 'Geography']
