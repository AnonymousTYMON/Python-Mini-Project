import os

for n in range(0, 40):
    par_dir = "C:/Users\Tymon\Pictures\給100分\畫家\荻pote (ogipote)"
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
'''
