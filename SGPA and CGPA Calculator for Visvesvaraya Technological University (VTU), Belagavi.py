"""
# Python Program to find CGPA or SGPA calcultor according to VTU norms
# Written By: Niranjan Hegde
# Reference: https://vtu.ac.in/wp-content/uploads/2019/12/becbcs2017-18.pdf
"""

#Class for SGPA
class SGPA:
    marks_list = []                     #List to store Marks for each subject
    credits_list = []                   #List to store Credits for each subject
    grade_points = []                   #List to store Grade point for each subject
    credit_points = []                  #List to store Credit Point for each subject
    
    #Initialising variables
    total_marks, total_credits, total_credit_points = 0, 0, 0
    maximum_marks = 100                 #Maximum marks for each subbject
    sgpa, percentage = 0.0, 0.0

    #Letter grades based vtu normas and which is related to marks
    letter_grade = {10 : 'O', 9 : 'S', 8 : 'A', 7 : 'B', 6 : 'C', 5 : 'D', 4 : 'E', 0 : 'F'}
    
    #Abrivations for corresponding Grade letters
    letter_grade_abrivation = {'O' : 'Out-standing', 'S' : 'Excellent', 'A' : 'Very Good', 'B' : 'Good', 'C' : 'Above Average', 'D' : 'Average', 'E' : 'Poor', 'F' : 'Fail'}

   
    #Methos to get Data i.e. marks and credit for each Subject
    def getData(self):

        #Loop until get correct input(number of subjects) and prompt corresponding message for wrong input
        while(True):
            subjects = input("\nEnter number of Subjects: ").strip()

            try:
                subjects = int(subjects)
                if subjects > 0:
                    break
                else:
                    print('Invalid Input...!')
                    print('Number of Subjects should be grater than 0')
            except ValueError:
                print("Invalid Input...!")


        print("\nEnter Marks Obtained and Credit for", subjects, "subjects")
        
        #Example to provide input in required format
        print("Input Format: If marks = 99 and credit = 4 then type as '99 4'")

        print()
        print('-' * 4)
        print("MM C")
        print('-' * 4)

        #Loop until get correct input(marks and credit for each subjects) and prompt corresponding message for wrong input
        while(subjects > 0):
            #Variables to hold valid flags
            valid_marks, valid_credit = True, True
            try:
                marks, credit = input().strip().split()
            except ValueError:
                print("\nInvalid Input Format...!")
                print('\nPlease Re-Enter Marks and Credit\n')
                continue

            try:
                marks = int(marks)
                if marks < 0 or marks > 100:
                    valid_marks = False
                    print('\nInvalid Marks...!')
                    print('Marks should be in between 0 - 100')
            except ValueError:
                valid_marks = False
                print('\nInvalid Marks...!')
                
            try:
                credit = int(credit)
                if credit <= 0:
                    valid_credit = False
                    print('\nInvalid Credit...!')
                    print('Credit must be non-negetive')
            except:
                valid_credit = False
                print('\nInvalid Credit...!')

            #Continue to next iteration if input is not correct
            if not valid_marks or not valid_credit:
                print('\nPlease Re-Enter Marks and Credit\n')
                continue                                            
            
            #Store the inputs in corresponding class attributes
            self.setData(marks, credit)

            #Decrement the subject count
            subjects -= 1


    #Method to convert and store the corresponding values into class attributes
    def setData(self, marks, credit):
        #Store the marks in marks_list
        self.marks_list.append(marks)

        #Converting marks into corresponding grade point according to VTU Norms and store in grade_points list
        if marks >= 90 and marks <= 100:
            self.grade_points.append(10)
        elif marks >= 80:
            self.grade_points.append(9)
        elif marks >= 70:
            self.grade_points.append(8)
        elif marks >= 60:
            self.grade_points.append(7)
        elif marks >= 45:
            self.grade_points.append(6)    
        elif marks >= 40:
            self.grade_points.append(4)
        else:
            self.grade_points.append(0)

        #Store the credit into credits_list
        self.credits_list.append(credit)

        #Calculating total marks and total credits
        self.total_marks += marks
        self.total_credits += credit

   
    #Method to calculate SGPA
    def calculateSGPA(self):

        #Iterate through each subjects grade points and credits
        for gp, c in zip(self.grade_points, self.credits_list): 
            credit_point = gp * c
            self.credit_points.append(credit_point)

            self.total_credit_points += credit_point

        #Calculation for SGPA
        self.sgpa = self.total_credit_points / self.total_credits

        #Calculation for Percentage
        self.percentage = (self.total_marks * 100) / (len(self.marks_list) * self.maximum_marks)


    #Method to Display data along with SGPA and percentage in proper manner
    def dispaly(self):

        #Table format to display Subject, Marks, Credit, Grade Point, Credit Point, Grade Letter for each Subject
        print()
        print('-' * 72)
        print('| Subject | Marks | Credit | Grade Point | Credit Point | Grade Letter |')
        print('-' * 72)

        for i in range(len(self.marks_list)):
            print('|', end = " ")
            print(str(i+1).rjust(4) + '|'.rjust(5) , end = " ")
            print(str(self.marks_list[i]).rjust(4) + '|'.rjust(3) , end = " ")
            print(str(self.credits_list[i]).rjust(4) + '|'.rjust(4) , end = " ")
            print(str(self.grade_points[i]).rjust(6) + '|'.rjust(7) , end = " ")
            print(str(self.credit_points[i]).rjust(7) + '|'.rjust(7) , end = " ")
            print(str(self.letter_grade[self.grade_points[i]]).rjust(6) + '|'.rjust(8))

        #Display letter grade information for users
        print('-' * 72)
        print()
        print('Note:')
        for k, v in self.letter_grade_abrivation.items():
            print('', k, ":", v)

        print()
        print('-' * 22)
        print('Total marks =', self.total_marks)                        #Display total marks obtained
        print('Total Credits =', self.total_credits)                    #Display total credits erned
        print('Percentage = {:.2f}%'.format(self.percentage))           #Display percentage corrected to two decimal point
        print('SGPA = {:.2f}'.format(self.sgpa))                         #Display SGPA correced to two decimal point
        print('-' * 22)
        print()


#Class for CGPA
class CGPA:
    sgpa_list = []                      #List to store SGPA
    credit_points_list = []             #List to store credit points

    #Initialising variables
    total_credit_points = 0
    sgpa, percentage = 0.0, 0.0
    
    #Methos to get Data i.e. SGPA and credit point for each Semester 
    def getData(self):

        #Loop until get correct input(number of semesters) and prompt corresponding message for wrong input
        while(True):
            semesters = input("\nEnter number of Semesters: ").strip()

            try:
                semesters = int(semesters)
                if semesters > 0:
                    break
                else:
                    print('Invalid Input...!')
                    print('Number of Semesters should be grater than 0')
            except ValueError:
                print("Invalid Input...!")


        print("\nEnter SGPA and Credit points for", semesters, "semesters")

        #Example to provide input in required format
        print("Input Format: If SGPA = 9.13 and credit point = 24 then type as '9.13 24'")

        print()
        print('-' * 7)
        print("S.SS CC")
        print('-' * 7)

        #Loop until get correct input(SGPA and credit point) and prompt corresponding message for wrong input
        while(semesters > 0):
            ##Variables to hold validity flags
            valid_sgpa, valid_credit = True, True
            try:
                sgpa, credit = input().strip().split()
            except ValueError:
                print("\nInvalid Input Format...!")
                print('\nPlease Re-Enter SGPA and Credit points\n')
                continue

            try:
                sgpa = float(sgpa)
                if sgpa < 1 or sgpa > 10:
                    valid_sgpa = False
                    print('\nInvalid SGPA...!')
                    print('SGPA should be in between 1 - 10')
            except ValueError:
                valid_marks = False
                print('\nInvalid SGPA...!')
                
            try:
                credit = int(credit)
                if credit <= 0:
                    valid_credit = False
                    print('\nInvalid Credit Point...!')
                    print('Credit Point must be non-negetive')
            except:
                valid_credit = False
                print('\nInvalid Credit Point...!')

            #Continue to next iteration if input is wrong
            if not valid_sgpa or not valid_credit:
                print('\nPlease Re-Enter SGPA and Credit Point\n')
                continue
            
            #Store the inputs in corresponding class attributes
            self.setData(sgpa, credit)

            #Decrement the semester count
            semesters -= 1

    #Method to store the corresponding values into class attributes
    def setData(self, sgpa, credit_point):
        #Store the SGPA into sgpa_list 
        self.sgpa_list.append(sgpa)

        #Store the credit point into credit_points_list
        self.credit_points_list.append(credit_point)

        #Calculating total credit points
        self.total_credit_points += credit_point
        

    #Method to calcuate CGPA
    def calculateCGPA(self):
        numerator = 0.0

        #Iterate through each semesters SGPA and credit points
        for sgpa, c in zip(self.sgpa_list, self.credit_points_list):
            numerator += (sgpa * c)

        #Calculation for CGPA
        self.cgpa = numerator / self.total_credit_points

        #Calculation for Percentage
        self.percentage = (self.cgpa - 0.75) * 10

    
    #Method to Display data along with cgpa and percentage in proper manner
    def dispaly(self):
        print()
        print('-' * 34)
        print('| Semester | SGPA | Credit Point |')
        print('-' * 34)

        for i in range(len(self.sgpa_list)):
            print('|', end = " ")
            print(str(i+1).rjust(5) + '|'.rjust(5) , end = "")
            print(str('{:.2f}'.format(self.sgpa_list[i])).rjust(5) + '|'.rjust(2) , end = " ")
            print(str(self.credit_points_list[i]).rjust(7) + '|'.rjust(7))

        print('-' * 34)
        print()
        print('-' * 22)
        print('CGPA = {:.2f}'.format(self.cgpa).center(22))                     #Display CGPA corrected to two decimal point
        print('Percentage = {:.2f}%'.format(self.percentage).center(22))        #Display percentage corrected to two decimal point
        print('-' * 22)
        print()



if __name__ == '__main__':

    #Display VTU SGPA and CGPA Calculator
    print()
    print(' VTU SGPA and CGPA Calulator '.center(72, '*'))


    #Loop until get correct input and prompt corresponding message for wrong input
    while(True):
        print()
        choice = input("Enter your Choice: \n'sgpa' for SGPA calculator\n'cgpa' for CGPA calculator\n'exit' to Exit the program\n\n")

        #Converting input to lowercase to aviod mismatching
        choice = choice.lower()
        
        #Create objet for sgpa if user want to calculate SGPA
        if choice == 'sgpa':
            print()
            print('Welcome to SGPA Calulator'.center(72, '-'))
            sgpa = SGPA()

            #Calling corresponding methods
            sgpa.getData()
            sgpa.calculateSGPA()
            sgpa.dispaly()

            #Exit program
            quit()

        #Create objet for sgpa if user want to calculate CGPA
        elif choice == 'cgpa':
            print()
            print('Welcome to CGPA Calulator'.center(72, '-'))
            cgpa = CGPA()

            #Calling corresponding methods
            cgpa.getData()
            cgpa.calculateCGPA()
            cgpa.dispaly()

            #Exit program
            quit()
        
        #Exit program if choice is exit
        elif choice == 'exit':
            print("Exiting the Program...")
            quit()
        else:
            print('Invalid Input...')
