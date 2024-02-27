This Python project is a simple quiz game implemented using the Tkinter library for creating a graphical user interface (GUI). Here's a brief description of the project:

1. **Title and Interface**: The title of the application is "Python Quiz Game". The GUI window is set to a specific size (900x500 pixels) using the `geometry()` method.

2. **Questions and Options**: The quiz consists of multiple-choice questions stored as dictionaries in the `questions` list. Each dictionary contains the question, options, and correct answer. 

3. **Widgets**: The GUI elements are created using Tkinter widgets such as `Label`, `Radiobutton`, and `Button`. 
   - The question label (`question_label`) displays the current question.
   - Four radio buttons (`option_widgets`) are used to display the options.
   - A submit button (`submit_button`) allows the user to submit their answer.
   - A label (`score_label`) shows the current score.

4. **Functionality**:
   - `display_question()`: Updates the question label and option buttons with the current question and its options.
   - `enable_submit()`: Enables the submit button after the user selects an option.
   - `check_answer()`: Compares the selected option with the correct answer and updates the score accordingly. Shows a message box indicating if the answer is correct or incorrect. Proceeds to the next question if available or shows the final score if all questions have been answered.
   - `show_final_score()`: Displays a message box showing the final score.

Overall, this project demonstrates the use of Tkinter for creating a basic quiz game interface with interactive functionality for answering questions and keeping track of scores.
