# The script scans all program files inside code directory, fethes questions which are the top comments
# and prepares a separate 'questions.txt'

import os
import re

dir = os.path.dirname(os.path.realpath(__file__))
code_dir = dir + '/' + 'codes'
# code_dir = dir 
output_file = dir + '/' + 'problems.txt'

dir_items = os.listdir(code_dir)

if os.path.exists(output_file):
    os.remove(output_file)

q_file = open(output_file, 'a')

with open(output_file, 'a') as q_file:

    programs = {}

    for f in dir_items:

        m = re.match('^program(\d+)\.py$',f)
        if m:
            programs[int(m.group(1))] = m.group(0)
        else:
            continue

    for i in sorted(programs.keys()):
        f = programs[i]
        print("- Question %s\n" % i, file=q_file)
        lines = open(code_dir + '/' + f).readlines()
        ignore_hash = 'n' # ignores code comments 

        for line in lines:
            if re.match('^#',line) and ignore_hash == 'n':
                line = re.sub('^#', '',line)
                if not re.match('^\s*\-+\s*$',line):
                    print(line.lstrip(), end='', file=q_file)
                else:
                    continue
            else:
                ignore_hash = 'y'
                continue

        print('\n', file=q_file)
