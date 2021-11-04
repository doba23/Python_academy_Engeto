file_handler = open('._FL_insurance_sample.csv','r+', newline='\n')



# file_path = input ('Which file to open?')

# header
# data, data, dat\n


with open ('._FL_insurance_sample.csv') as fh:
    for nl, line in enumerate(fh):
        in nl == 0:
            print (f'Line {nl}:{line} end ')