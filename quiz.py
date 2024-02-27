import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(" Python Quiz Game")
        self.geometry("900x500")
        
        self.questions = [
            {
                "question": "Who developed Python Programming Language?",
                "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
                "correct_option": "Guido van Rossum"
            },
            {
                "question": "Which type of Programming does Python support?",
                "options": ["object-oriented programming", "structured programming", "functional programming", "all of the mentioned"],
                "correct_option": "all of the mentioned"
            },
            {
                "question": "Is Python case sensitive when dealing with identifiers?",
                "options": ["no", "yes", "machine dependent", "none of the mentioned"],
                "correct_option": "yes"
            },
            {
                "question": "Which of the following is the correct extension of the Python file?",
                "options": [".python", ".pl", ".py", ".p"],
                "correct_option": ".py"
            },
            {
                "question": "Python code compiled or interpreted?",
                "options": [" Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled", " Python code is only interpreted"],
                "correct_option": "Python code is both compiled and interpreted ."
            },
            {
                "question": " All keywords in Python are in _________.",
                "options": [" Capitalized", "lower case", "UPPER CASE", "None of the mentioned"],
                "correct_option": "lower case"
            },
            {
                "question": "What will be the value of the following Python expression? 4 + 3 % 5",
                "options": ["7", "2", "4", "1"],
                "correct_option": "7"
            },
            {
                "question": "Which of the following is used to define a block of code in Python language?",
                "options": ["Indentation", "Key", " Brackets", " All of the mentioned"],
                "correct_option": "Indentation"
            },
            {
                "question": "Which keyword is used for function in Python language?",
                "options": [" Function", "def", "Fun", "Define"],
                "correct_option": "def"
            },
            {
                "question": "Which of the following character is used to give single-line comments in Python?",
                "options": ["//", "!", "#", "/*"],
                "correct_option": "#"
            },
        ]
        
        self.current_question_index = 0
        self.score = 0
        
        self.create_widgets()
        self.display_question()
        
    def create_widgets(self):
        self.question_label = tk.Label(self, text="",justify="left", font=("Times New Roman", 30))
        self.question_label.pack(pady=30)
        
        self.option_widgets = []  # Initialize the list here
        
        self.option_var = tk.StringVar()
        
        for i in range(4):
            option = tk.Radiobutton(self, text="", variable=self.option_var, value="", command=self.enable_submit, font=("Times New Roman", 20))
            option.pack(anchor="w", padx=50, pady=10)
            self.option_widgets.append(option)  # Append each Radiobutton to the list
        
        self.submit_button = tk.Button(self, text="Submit", state="disabled", command=self.check_answer, font=("Times New Roman", 20), bg="white", fg="Green")
        self.submit_button.pack(pady=50)
        
        self.score_label = tk.Label(self, text="", font=("Times New Roman", 20))
        self.score_label.pack()
        
    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        
        options = question_data["options"]
        for i in range(4):
            self.option_widgets[i].config(text=options[i], value=options[i])
        
    def enable_submit(self):
        self.submit_button.config(state="normal")
        
    def check_answer(self):
        selected_option = self.option_var.get()
        correct_option = self.questions[self.current_question_index]["correct_option"]
        
        if selected_option == correct_option:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {correct_option}")
        
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
            self.option_var.set("")
            self.submit_button.config(state="disabled")
        else:
            self.show_final_score()
        
    def show_final_score(self):
        messagebox.showinfo("Final Score", f"Your final score is: {self.score}/{len(self.questions)}")
        self.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
