with (open('output_file_neg_100.txt', encoding='utf8') as f1, 
      open('output_file_pos_100.txt', encoding='utf8') as f2, 
      open('output_file_100.txt', 'w') as dest):
    while True:
        data = f1.readline() + f2.readline()
        if not data:
            break
        dest.write(data)

with (open('output_file_neg_10.txt', encoding='utf8') as f1, 
      open('output_file_pos_10.txt', encoding='utf8') as f2, 
      open('output_file_10.txt', 'w') as dest):
    while True:
        data = f1.readline() + f2.readline()
        if not data:
            break
        dest.write(data)

with (open('output_file_neg_300.txt', encoding='utf8') as f1, 
      open('output_file_pos_300.txt', encoding='utf8') as f2, 
      open('output_file_300.txt', 'w') as dest):
    while True:
        data = f1.readline() + f2.readline()
        if not data:
            break
        dest.write(data)

