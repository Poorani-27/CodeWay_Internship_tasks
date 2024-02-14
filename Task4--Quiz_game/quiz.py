import tkinter as tk
from PIL import Image, ImageTk
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x400")
        self.title("Quiz_Game")
        self.config(bg="White")
        self.current_question_index = 0
        self.score = 0
        self.selected_option = None

        self.original_img = Image.open("pic.png")
        self.resized_img = self.original_img.resize((200, 200))  
        self.play_image = ImageTk.PhotoImage(self.resized_img)
        self.show_welcome_page()

    def show_welcome_page(self):
        self.clear_window()
        self.Title = tk.Label(self, text="Welcome To Quiz Game", font=("Arial", 20, "bold"), bg="White", width=30)
        self.Title.pack(pady=5)

        self.Rules = tk.Label(self, text="Rules \n1. One point for correct Answer \n2. No point for wrong Answer", font=("Arial", 10), bg="White", width=30)
        self.Rules.pack(pady=5)

        self.play_label = tk.Label(self, image=self.play_image, bd=0)
        self.play_label.pack(pady=20)

        self.Play_btn = tk.Button(self, text="Let's play", bg="Blue", fg="White", width=20, height=2, font=("arial", 10, "bold"), bd=5, command=self.start_quiz)
        self.Play_btn.pack(pady=6)

    def start_quiz(self):
        self.clear_window()
        self.questions = [
          {"question": "What is the extension of python source file", "options": [".py", ".txt", ".exe", ".doc"], "answer": ".py"},
            {"question": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What keyword is used to define function in python?", "options": ["define", "func", "def", "function"], "answer": "def"},
            {"question": "Which of the following is a correct variable name in python?", "options": ["my_var", "1-var", "var-1", "my#var"], "answer": "my_var"},
            {"question": "Which of the following data types is mutable ?", "options": ["string", "list", "tuple", "set"], "answer": "list"}
        ]

        self.current_question_index = 0
        self.score = 0

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question_index]
        question_text = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]

        self.clear_window()

        self.question_label = tk.Label(self, text=question_text, font=("Arial", 10), bg="White")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for option in options:
            button = tk.Button(self, text=option, width=30, bg="light blue", command=lambda o=option: self.check_answer(o, correct_answer))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12), bg="White")
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(self, text="Next", width=20, height=2, bg="Light green", fg="Black", font=("Arial", 10, "bold"), bd=5, command=self.next_question)
        self.next_button.pack(pady=20)

    def check_answer(self, selected_option, correct_answer):
        self.selected_option = selected_option
        for button in self.option_buttons:
            button.config(state="disabled")
        if selected_option == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Your answer is correct!", fg="green")
        else:
            self.feedback_label.config(text="Your answer is incorrect!", fg="red")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result_page()

    def show_result_page(self):
        self.clear_window()

        result_text = f"Quiz Completed!\n\nYour Score: {self.score}/{len(self.questions)}"
        self.result_label = tk.Label(self, text=result_text, font=("Arial", 16, "bold"), bg="White")
        self.result_label.pack(pady=50)

        self.quit_button = tk.Button(self, text="Quit", width=10, height=1, bg="red", fg="white", font=("Arial", 12), command=self.quit)
        self.quit_button.pack(pady=20)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
