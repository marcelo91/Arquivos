import os
import re

path = os.listdir("E:\Cursos e Aulas\Python Scripts\Embaralhar_img")
real_path = os.getcwd()
print(real_path)
os.chdir("E:\Cursos e Aulas\Python Scripts\Embaralhar_img")
for i in path:
    print(i)
    os.rename(i,re.sub('[0-9]', '', i))

