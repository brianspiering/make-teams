#!/usr/bin/env python
# coding: utf-8
"Make programming teams for each day for each week. Format as a markdown table. Then save to files."

import os
import collections
import random
from typing import List

def make_teams(students: List, weeks: int=6, days: int=2, path: str='teams', pair_labels: bool=True):
    "Given a list of students, make programming teams for each session, each day for each week. Save the resulting markdown table."

    n_students = len(students)
    random.seed()

    if not os.path.exists(path):
        os.makedirs(path)
    
    for week in range(1, weeks+1):
        for day in range(1, days+1):
            
            random.shuffle(students)
            filename = "teams_"+str(week)+"_"+str(day)+".md"
            
            with open(path+'/'+filename, 'w') as out_file:
                
                line_break_counter, team_counter, pair_counter = 0, 0, 0
                range_current = range(1, n_students, 2)
                
                if n_students % 2 == 0:

                    for i in range_current:


                        if (line_break_counter % 2 == 0) and pair_labels:
                            out_file.write(f"|     | Team {team_counter}|     |\n")
                            out_file.write("|:----:|:---:|:---:| \n")
                        elif (line_break_counter % 2 == 0) and not pair_labels:
                            out_file.write(f"|Team {team_counter}|     |\n")
                            out_file.write("|:---:|:---:| \n")

                        if pair_labels:
                            pair_string = f'Pair {pair_counter}'
                            out_file.write(f'| {pair_string} |{students[i - 1]}|{students[i]}|\n')
                            pair_counter += 1
                        else:
                            out_file.write(f'|{students[i - 1]}|{students[i]}|\n')

                        line_break_counter += 1 # Add line break for 4-5 person teams

                        if (line_break_counter % 2 == 0) and (i != range_current[-1]): 
                             out_file.write('\n')
                             team_counter += 1
                            
                else: # If there is an odd number of students, add triple "pair" 
                    loop_num, total_loops  = 0, int(n_students/2)
                    
                    for i in range_current:
                        

                        if (line_break_counter % 2 == 0):
                            out_file.write(f"|     | Team {team_counter} |     |     |\n")
                            out_file.write("|:----:|:---:|:---:|:---:| \n")
                        
                        loop_num += 1

                        if pair_labels:
                            pair_string = f'Pair {pair_counter}'
                        else:
                            pair_string = ''

                        if loop_num != total_loops:
                            out_file.write(f'| {pair_string} | {students[i - 1]} | {students[i]} | |\n')
                           
                        else:

                            odd_person_out = students[-1:n_students]
                            out_file.write(f'| {pair_string} | {students[i - 1]} | {students[i]} | {odd_person_out[0]} |\n')
                        
                        pair_counter += 1
                        line_break_counter += 1 # Add line break for 4-5 person  teams
                    
                        if (line_break_counter % 2 == 0) and (i != range_current[-1]): 
                             out_file.write('\n')
                             team_counter += 1

                out_file.write("  \n")

def horizontal_layout(filename: str, path: str='teams', n_cols: int=5):
    "Convert vertical list to tiled"
    
    with open(path+'/'+filename) as f:
        orginal = [line.strip() for line in f.readlines()]

    # Slice into component parts
    team_nums = orginal[::5]
    line_breaks = orginal[1::5]
    people_row_1 = orginal[2::5]
    people_row_2 = orginal[3::5]

    row_counter = 0

    with open(path+'/'+filename, 'w') as f:
    
        for table_row in range(1, n_cols+1):
            s = slice(row_counter, n_cols+row_counter)
            row_1 = ' '.join(team_nums[s])
            row_2 = ':---:'.join(line_breaks[s])
            row_3 = ' '.join(people_row_1[s])
            row_4 = ' '.join(people_row_2[s])

            f.write(row_1 + '\n')
            f.write(row_2 + '\n')
            f.write(row_3 + '\n')
            f.write(row_4 + '\n')
            f.write('\n')
            
            row_counter += n_cols



if __name__ == '__main__':
    
    with open('students.txt') as f:
        students = f.read().splitlines()

    # Make sure there are no extact duplicate students    
    assert len(students) == len(set(students)), f"Duplicate students names: {[item for item, count in collections.Counter(students).items() if count > 1]})"

    make_teams(students, 
               weeks=1,
               days=1,
               pair_labels=False)

    horizontal_layout(filename='teams_1_1.md')
