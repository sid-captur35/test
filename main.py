"""
import os

def make_commit(days: int):
    if days < 1:
        # push
        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

            # Staging
            os.system('git add data.txt')

            # Commit
            os.system('git commit --date="'+dates+'" -m "First Commit"')

            return days * make_commit(days-1)

make_commit(365)
"""

import os
from random import randint

for i in range(1, 365):

    for j in range(0, randint(1,10)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')