import sys
import csv

def set_max_field_size():
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

def fix_comment(row):
    no_of_columns = 42
    comment_col_ind = 18
    if len(row) > no_of_columns:
        no_of_cols_with_comment = len(row) - no_of_columns
        comment_text = ' '.join([row[comment_col_ind+i] for i in range(no_of_cols_with_comment)])
        
        for i in range(no_of_cols_with_comment-1):
            row.pop(comment_col_ind)
        row[comment_col_ind] = comment_text
    row[comment_col_ind] = row[comment_col_ind].replace('\t', '')
    return row

def main():
    max_row_to_scan = 100
    no_of_column = (len(row) for i_row, row in enumerate(csv.reader(open('input_file.txt', 'r'), delimiter='\t')) if i_row <= max_row_to_scan)
    max_column_no = sum(no_of_column) / max_row_to_scan
    count_error = 0
    with open('input_file.txt', 'r') as f_in, open('output_file.txt', 'w', newline='') as f_out:
        reader = csv.reader(f_in, delimiter='\t')
        writer = csv.writer(f_out, delimiter='\t')
        tmp_row_data = []
        for row in reader:
            if len(row) == 0:
                continue
            if len(row) + len(tmp_row_data) < max_column_no:
                if len(row) > 0:
                    count_error += 1
                    tmp_row_data += row
            else:
                if tmp_row_data:
                    row = tmp_row_data + row
                    row = fix_comment(row)
                    writer.writerow(row)
                    tmp_row_data = []
                else:
                    row = fix_comment(row)
                    writer.writerow(row)
    print("total errors : {}".format(count_error))

set_max_field_size()
main()
