import csv

term_array = []
with open('C:/Users/User/Desktop/descriptions801-1200.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        term_array.append(row)

current_number = term_array[0][0]
current_id =  term_array[1]
current_desc = term_array[2]

print(current_desc)








# unique_term_array = list(set(term_array))
# for i in range(len(unique_term_array)):
#     print(i)
#     print(unique_term_array[i])





# term_array = []
#
# with open('C:/Users/User/Desktop/text/csvs/terms.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     for row in csv_reader:
#         term_array.append(row[1])
#
#
#
# unique_term_array = list(set(term_array))
#
# for i in range(len(unique_term_array)):
#     print(i)
#     print(unique_term_array[i])
#

#
# unique_term_array = remove_duplicates(term_array)
#
# print(len(term_array))
# print(len(unique_term_array))
#
# for term in range(len(unique_term_array)):
#     print(term)
