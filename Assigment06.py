# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Then add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MBruce,08.14.2022, Modified code to add functions for Assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name_str, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        # TODO: Add Code Here!

        list_of_rows.append(row)
        # Add it to the current task list of dictionary objects- "lstTable"

        return list_of_rows


    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        lst_of_all_values = [task for elem in list_of_rows for task in elem.values()]  # Used List comprehension to create list of
                                                                                       # only task values for easier task matching

        if task not in lst_of_all_values:                             # If this evaluates to true (task not in list)
            IO.output_task_not_in_list(task=task)                     # Inform user task in not in list- call function to print message

        else:
            for row in list_of_rows:                                  # Loop through lstTable to find task match
                if row["Task"].lower() == task.lower():               # Check for match
                    list_of_rows.remove(row)                          # When match is found, Remove task
                    IO.output_task_removed(task=task)                 # Inform user task is removed- call function to print out message


        return list_of_rows


    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        objFile = open(file_name, "w")                                     # Open file ToDoList.txt for write
        for row in list_of_rows:                                           # Loop through dictionary objects (row) in list table
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")      # Write each one to file
        objFile.close()
        return list_of_rows                                                # Need to return the list_of_rows after write to file, else task list will not print


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        # TODO: Add Code Here!

        strTask = input("Please input a new task name:")                     # Prompt user for new task- assign to string "strTask"
        strPriority = input("Please input its priority:")                    # Prompt user for priority- assign to string "strPriority"

        return (strTask, strPriority)                                        # Return user entered task and priority values

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        #TODO: Add Code Here!

        strRemoveTask = input("Enter name of task you want to remove?")      # Prompt user for task to be removed

        return strRemoveTask                                                 # Return user entered task value

    ######################################################################
    ### Some additional functions ###
    ######################################################################
    @staticmethod
    def output_task_removed(task):
        """  outputs the task name that was removed from the list

        :return: nothing
        """

        print("The task: '" + task + "' has been removed")               # Inform user task is remove
        print("*******************************************")             # decoration
        print()                                                          # Add an extra line for looks


    @staticmethod
    def output_task_not_in_list(task):
        """  outputs that task name that was not found in the list

        :return: nothing
        """

        print("The task: '" + task + "' is not in current list")         # Inform user task was not in list
        print("*******************************************")             # decoration
        print()                                                          # Add an extra line for looks



# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
