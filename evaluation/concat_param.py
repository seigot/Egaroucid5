data = ''
for i in range(15):
    for j in range(2):
        with open('learned_data/' + str(i) + '_' + str(j) + '.txt', 'r') as f:
            data += f.read()
with open('param.txt', 'w') as f:
    f.write(data)