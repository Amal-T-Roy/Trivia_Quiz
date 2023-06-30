from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Handles the tkinter UI.Quiz_brain is passed as parameter"""

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # set size of window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # create score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Create True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=50, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)
        # create False button
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(
            image=false_image, highlightthickness=50, command=self.false_pressed
        )
        self.true_button.grid(row=2, column=1)

        self.get_next_question()  # get next question
        # start main loop
        self.window.mainloop()

    def get_next_question(self) -> None:
        """Update score,Change bg to white,Get next question from quiz_brain"""
        if self.quiz.still_has_questions():    
            self.canvas.config(bg="white")  # Update bg of question to white
            self.score_label.config(text=f"Score: {self.quiz.score}")  # update score in UI
            q_text = self.quiz.next_question()  # get question
            self.canvas.itemconfig(
                self.question_text, text=q_text
            )  # display question in canvas
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the questions!!")

    def true_pressed(self):
        """Called when true button is pressed"""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Called when false button is pressed"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Turns bg green if answer is true,else red"""
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(
            1000, self.get_next_question
        )  # call next question after 1 sec
