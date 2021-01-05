ssn = str(input('Please enter SSN: '))

if len(ssn) == 9:
    part1 = ssn[0:3]
    part2 = ssn[3:5]
    part3 = ssn[5:9]
    result = part1 + '-' + part2 + '-' + part3
else:
    result = 'Incorrect SSN length.'

print(result)
