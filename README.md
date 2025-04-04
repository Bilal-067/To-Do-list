Name: Mohammed Bilal M

Intern id: CS25RY20902

Domain name: Codsoft

Stream: Python Programming

Task 1: To-Do list

It is a, simple "To-Do List" application using the tkinter library for a graphical user interface (GUI). The application allows users to add, update, delete, and view tasks. Below is a detailed description of the components and functionalities of the code:

1. Window Setup
The application window is created using tkinter.Tk(), and the title of the window is set to "TO DO LIST".

The background color of the window is set to dark green using root.config(bg="darkgreen").

The window size is specified as 400x500 pixels.

2. Global Variables
is_updating: A flag to determine whether the user is updating an existing task.

input_var: A StringVar used to store and handle the text input from the user (task name).

output_var: A StringVar used to display messages (success or error).

3. Functions
clear_output: Clears the message shown in the output field after a delay of 1.5 seconds.

add_or_update_task: Adds a new task to the list if the input is valid, or updates an existing task if the user is updating it. It checks whether the input task already exists before adding it and handles the update by replacing the old task.

select_task_for_update: Allows the user to select a task from the list to edit it. If a task is selected, it appears in the input field for updating.

delete_task: Deletes a selected task from the list if one is selected, otherwise, it notifies the user if no task is selected.

handle_button_click: This function handles the actions triggered by clicking the buttons (CREATE, UPDATE, DELETE, QUIT). It checks the text on the button and calls the respective function accordingly.

4. GUI Components
Heading: A label displaying "TO DO LIST" at the top of the window with a white font on a dark green background.

Listbox: A scrollable listbox where the tasks are displayed. It is connected to a scrollbar for easy navigation when there are many tasks.

Input Section:

A label prompts the user to input a task.

A text entry field is provided for the user to enter a task.

A readonly output entry field displays success or error messages.

Buttons:

Four buttons are created using the create_button function: "CREATE", "UPDATE", "DELETE", and "QUIT". The "CREATE" button adds a task, the "UPDATE" button lets the user update an existing task, the "DELETE" button removes a selected task, and the "QUIT" button closes the application.

5. Event Handling

The button labels ("CREATE", "UPDATE", "DELETE", "QUIT") are mapped to their respective functions using event handling with the bind method. The handle_button_click function is invoked when any of the buttons are clicked.

6. Main Event Loop
The root.mainloop() starts the Tkinter event loop, making the application interactive and ready for user input.

Overall Functionality:

The user can input tasks, view the list of tasks, update an existing task, and delete tasks.

The interface provides feedback through the output field, showing messages like "Task added successfully", "Task updated successfully", "No task selected", or "List is empty".

The application also prevents the user from adding duplicate tasks and handles empty inputs gracefully.

This is a functional and user-friendly To-Do List application with a clear, simple interface built using tkinter.

Thanks for the Codsoft Team for giving this opportunity to be a part of this journey.

Output-> 

![Project1](https://github.com/user-attachments/assets/092e5803-7b74-4672-a8c3-e98770e37e95)
