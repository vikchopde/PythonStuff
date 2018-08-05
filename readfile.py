import os
import re
import pandas as pd


column_names=('ccy_pair', 'bid', 'ask', 'tick_id')
data = pd.DataFrame()


# Regex used to match relevant loglines (in this case, a specific IP address)
reuters_regex = re.compile(r".*reuters::OnTick.*$")

# Output file, where the matched loglines will be copied to
output_filename = os.path.join(os.getcwd(), "new.log")
input_filename = os.path.join(os.getcwd(), 'account.log')

# Overwrites the file, ensure we're starting out with a blank file
with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open(input_filename, "r") as in_file:
        # Loop over each log line
        for line in in_file:
            # If log line matches our regex, print to console, and output file
            m = reuters_regex.match(line)
            if m:
                first = line.find("reuters::OnTick") + len('reuters::OnTick(')
                second = line.find(")", first)
                ls = [line[first:second].split(' ')]
#                csv_line = '{},{},{},{}'.format(ls[0], ls[1], ls[2], ls[3])

                data = data.append(pd.DataFrame(ls,columns=['a','b','c','d']), ignore_index=True)
#                out_file.write(csv_line + '\n')

print(data[(data.a == 'EURJPY')])