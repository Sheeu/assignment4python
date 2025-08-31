file1=open('output.txt','w')
write_to_file=file1.write(input("Enter data to write to 'output.txt' file: "))
file1.close()

file1=open('output.txt','a')
append_to_file=file1.write('\n')
append_to_file=file1.write(input("Enter data to append to 'output.txt' file: "))
file1.close()

file1=open('output.txt','r')
print("Final content of 'output.txt' is:\n")
read_file=file1.read()
print(read_file)
file1.close()