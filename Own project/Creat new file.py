import os
'''
for n in range(n1, n2):
    par_dir = "(Location)"
    dir = str(n)
    path = os.path.join(par_dir, dir)
    mode = 0o666
    os.mkdir(path, mode)
'''

par_dir = "(Location)"
dir = "(New folder name)"
path = os.path.join(par_dir, dir)
mode = 0o666
os.mkdir(path, mode)

#C:/Users\Tymon\Pictures\給100分
