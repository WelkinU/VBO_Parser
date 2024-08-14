import pandas as pd
import re

class VBO_Parser:

    def __init__(self, vbo_filepath: str):

        with open(vbo_filepath, 'r') as file:

            block_header = None
            self.header, self.comments = [], []
            self.channel_units = []
            self.module_information = []
            column_names = []

            for line_num, line in enumerate(file):
                line = line.rstrip()

                if len(line) == 0:
                    continue

                if line.startswith('[') and line.endswith(']'):
                    block_header = line
                    continue

                elif block_header == '[header]':
                    self.header.append(line)
                    continue

                elif block_header == '[channel units]':
                    self.channel_units.append(line)
                    continue

                elif block_header == '[comments]':
                    self.comments.append(line)
                    continue

                elif block_header == '[module Information]':
                    self.module_information.append(line)

                elif block_header == '[column names]':
                    assert column_names == [], 'Malformed VBO file, expected only 1 line containing column names.'
                    column_names = re.split(r'\s+',line)

                    #Handle duplicate column names
                    if len(column_names) > len(set(column_names)):
                        counter = {}
                        for i, name in enumerate(column_names):
                            if name not in counter:
                                counter[name] = 1
                            else:
                                counter[name] += 1
                                column_names[i] += f'_{counter[name]}'
                                print(f'Duplicate column name detected "{name}"  -- Replacing with "{column_names[i]}"')

                elif block_header == '[data]':
                    first_line = line.split(' ')
                    header_length = line_num

                    channel_names = [var for var, val in zip(column_names, first_line) if 'E' in val]
                    self.channel_units_map = {var: unit for var, unit in zip(channel_names, self.channel_units)}
                    break

            #make comments all 1 string
            self.comments = '\n'.join(self.comments)

            #read data as pandas dataframe
            self.data = pd.read_csv(vbo_filepath, names = column_names, sep = ' ',
                header = header_length, index_col = False, skip_blank_lines=True)


if __name__ == '__main__':
    pass