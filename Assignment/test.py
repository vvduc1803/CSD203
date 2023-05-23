with open('library_info.txt', 'r') as file:
    file = file.readlines()[1:]
    file = [ele.split('|') for ele in file]
    file.reverse()
    for bid, title, author, status in file:
        print(f'{bid}{title}{author}{status[0]}')