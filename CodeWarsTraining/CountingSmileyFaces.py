def count_smileys(arr):
    valid_eyes = [':', ';']
    valid_nose = ["-", '~']
    valid_mouth = [')', 'D']
    count = 0
    for i, item in enumerate(arr):
        if len(item) == 2:
            if item[0] in valid_eyes and item[1] in valid_mouth:
                count += 1
        elif len(item) == 3:
            if item[0] in valid_eyes and item[1] in valid_nose and item[2] in valid_mouth:
                count += 1
    return count


### OR ###

import re
def count_smileys1(arr):
    return len(re.findall('[:;][-~]?[)D]', str(arr)))


### OR ###



def count_smileys2(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

print(count_smileys2([':D',':~)',';~D',':)']))