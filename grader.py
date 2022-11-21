#!/usr/bin/python3
import os
import stat

test = open('test.txt','r')
answer = open('ans.txt','r')
students = open('../id.txt','r')
input_lines = [l.rstrip() for l in  test.readlines()]
answer_lines = [l.strip() for l in answer.readlines()]

for id in students.readlines():
    print(f'id:{id.strip()}')
    try:
       os.chmod('../code/'+id.strip()+'_4.py',0o775)
    except:
        with open('score_paper_4.txt','a') as score:
            score.write('{:10} {:10}\n'.format(id.strip(),'unexcutable file!!!'))
        continue
    for i in range(len(answer_lines)):
        #print(f'test case: {i}')
        try:
             os.system('(echo '+input_lines[i]+')'+' | '+'python ../code/'+id.strip()+'_4.py'+' >> result.txt')
        except:
            with open('result.txt','a') as fh:
                fh.write('@@@\n')
    id_output = open('result.txt','r')
    output_lines = [l.strip() for l in id_output.readlines()]
    
    points = 0
    warning = False
    for idx in range(len(answer_lines)):
        try:
             if output_lines[idx] == answer_lines[idx]:
                 print(f'{idx}:AC')
                 points += 10
             else:
                 print(f'{idx}:WA')
        except:
            with open('score_paper_4.txt','a') as score:
                score.write('{:10} {:10}\n'.format(id.strip(),'unexcutable file!!!'))
            warning = True
            break
    print('\n')
    if warning:
        os.system('rm result.txt')
        continue
    with open('score_paper_4.txt','a') as score:
        score.write('{:10}  {:10}\n'.format(id.strip(),str(points)))
    os.system('rm result.txt')
print('Done grading!!')
