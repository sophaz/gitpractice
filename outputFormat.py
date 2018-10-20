#!/usr/bin/env python
import os

with open("input.txt", "r+") as f:
    lines = f.readlines()

    # Create a new file to write messsages to
    with open("output.txt", "w") as output:
        # Wipe whatever was previously in this file, if any
        output.truncate()

        for line in lines:
            path = os.path.basename(line)
            violation_type = ""
            violation_split = []

            if ' error:' in path:
                violation_type = "Error: "
                violation_split = path.split(' error: ')
            elif ' warning:' in path:
                violation_type = "Warning: "
                violation_split = path.split(' warning: ')

            colon_split = violation_split[0].split(':')
            file_name = colon_split[0]
            line_number = 'Line ' + colon_split[1]
            full_message = violation_split[1]
            short_message = full_message.split(': ')[1].split(' (')[0]
            message = violation_type + short_message

            comment = '\n'.join([file_name, line_number, message])
            output.write('\n' + comment + '\n')
        output.seek(0)
        # Uncomment the line below to dump contents of output file
        #print(output.read(),end="")