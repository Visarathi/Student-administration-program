import csv

#open a new file in excel file formate
def write_into_csv(info_list):
    with open('student_info1.csv' , 'a' , newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Address", "E-mail Id"])
        
        writer.writerow(info_list)

#starting point of the program
if __name__ == "__main__":
    
    condition = True
    student_num = 1
    
    while(condition):
        student_infomation = input("enter some information for student #{} in the form of name age address e-mail id\t".format(student_num))

        student_info = student_infomation.split(' ')

        print("\nThe entered info is - \nName:{} \nAge:{} \nAddress:{} \nE-mail Id:{}"
             .format(student_info[0],student_info[1],student_info[2],student_info[3]))
        
        choice_check = input("Is the entered information is correct?(yes/no)")

        if choice_check =='yes':
            write_into_csv(student_info)
            condition_check = input("do you want to enter some more info yes or no?\t")
            if condition_check=='yes':
                condition = True
                student_num += 1
            elif condition_check=='no':
                condition = False

        elif choice_check =='no':
            print("\nRe-enter the information:")
