import csv

count_error=0
# open the input file
with open('input_file.txt', 'r') as f_in:
    # create a CSV reader with tab delimiter
    reader = csv.reader(f_in, delimiter='\t')
    # open the output file
    with open('output_file.txt', 'w',newline='') as f_out:
        # create a CSV writer with tab delimiter
        writer = csv.writer(f_out, delimiter='\t')
        # iterate over each row in the input file
        tmp_row_data=[]
        for row in reader:
        # if the row has more than the expected number of fields
            #print(len(row))
            #print(row)
            if len(row) > 40:
                
                if tmp_row_data :
                    #print(tmp_row_data )
                    
                    row[-1] = tmp_row_data[-1] + row[0] 
                    if(len(row)>0) :
                        row.pop(0)
                    row = row + tmp_row_data
                    #print( row)
                    writer.writerow(tmp_row_data + row) 
                    tmp_row_data=[]
                else:
                    writer.writerow(row)

                
            else:
                if len(row) > 0 :
                    count_error = count_error + 1
                    tmp_row_data= tmp_row_data + row
                # else:
                #     writer.writerow(row)
print("total errors : {}".format(count_error))
