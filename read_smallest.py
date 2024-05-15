from typing import TextIO
import time_series
# def smallest_value(reader: TextIO) -> int:
#     """Read and process reader and return the smallest value after the
#     time_series header.
#     report erratum • discuss
#     Writing Algorithms That Use the File-Reading Techniques • 189
#     >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
#     >>> smallest_value(infile)
#     1
#     >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
#     >>> smallest_value(infile)
#     1
#     """
#     line = time_series.skip_header(reader).strip()
#     # Now line contains the first data value; this is also the smallest value
#     # found so far, because it is the only one we have seen.
#     smallest = int(line)
#     for line in reader:
#         line = line.strip()  # removes trailing and beginning spaces.
#         if line != '-':
#             value = int(line)
#             smallest = min(smallest, value)
#     return smallest
# if __name__ == '__main__':
#     with open('hopedale.txt', 'r') as input_file:
#         print(smallest_value(input_file))


def smallest_value(reader: TextIO) -> int:
    """Read and process reader and return the smallest value after the
    time_series header.
    report erratum • discuss
    Writing Algorithms That Use the File-Reading Techniques • 189
    >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
    >>> smallest_value(infile)
    1
    """
    line = time_series.skip_header(reader).strip()
    if line:
        # Now line contains the first data value; this is also the smallest value
        # found so far, because it is the only one we have seen.
        smallest = int(line)
        for line in reader:
            line = line.strip()
            if line == '-':
                continue
            value = int(line)
            # If we find a smaller value, remember it.
            # if value < smallest:
            #     smallest = value
            smallest = min([value, smallest])
        return smallest
    else:
        return 0
if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))