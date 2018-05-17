#!/usr/bin/env python
# coding: utf-8
"Make programming teams for each day for each week. Format as a markdown table, then save to file."

import os
import random


def make_teams(students: list, weeks: int=6, days: int=2, path: str='teams'):
    "Given a list of students, make programming teams for each session, each day for each week. Save the resulting markdown table."

    n_students = len(students)
    random.seed()
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    for week in range(1, weeks+1):
        for day in range(1, days+1):
            random.shuffle(students)
            file_name = "teams_"+str(week)+"_"+str(day)+".md"
            with open(path+'/'+file_name, 'w') as out_file:
                
                line_break_counter = 0
                
                if n_students % 2 == 0:
                    out_file.write("| Driver | Navigator | \n")
                    out_file.write("|--------|-----------| \n")
                    for i in range(1, n_students, 2):
                        out_file.write('|{}|{}|\n'.format(students[i - 1], students[i]))
                        
                        # Add line break for 4-5 person RAT teams
                        line_break_counter += 1
                        
                        if (line_break_counter % 2 == 0): 
                             out_file.write('| | |\n')
                            
                else: # If there is an odd number of students, add triple "pair" 
                        out_file.write("| Driver | Navigator 1 | Navigator 2 | \n")
                        out_file.write("|--------|-----------|------------| \n")
                        loop_num, total_loops = 0, int(n_students/2)
                        for i in range(1, n_students, 2):
                            loop_num += 1

                            if loop_num != total_loops:
                                out_file.write('| {} | {} | |\n'.format(students[i - 1], students[i]))
                            else:
                                odd_person_out = students[-1:n_students]
                                out_file.write('| {} | {} | {} |\n'.format(students[i - 1], students[i], odd_person_out[0]))
                            
                            # Add line break for 4-5 person quiz teams
                            line_break_counter += 1
                        
                            if (line_break_counter % 2 == 0): 
                                 out_file.write('| | |\n')

                out_file.write("  \n")

if __name__ == '__main__':
    
    with open('students.txt') as f:
        students = f.read().splitlines()

    make_teams(students=students)
