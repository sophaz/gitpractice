#!/usr/bin/python
import sys
import os

with open("input.txt", "r+") as f:
    lines = f.readlines()
    with open("output.txt", "r+") as output:
        output.truncate()
        for line in lines:
            path = os.path.basename(line)
            type = ""
            violation_split = []
            if ' error:' in path:
                type = "Error"
                violation_split = path.split(' error: ')
            elif ' warning:' in path:
                type = "Warning"
                violation_split = path.split(' warning: ')

            colon_split = violation_split[0].split(':')
            file_name = colon_split[0]
            line_number = 'line ' + colon_split[1]
            message = violation_split[1]

            comment = '\n'.join([file_name, line_number, message])
            output.write(comment + '\n')
        output.seek(0)
        print(output.read(),end="")
        output.close()
    f.close()
