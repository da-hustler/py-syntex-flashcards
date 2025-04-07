from flashcards.data_categorized import flashcards
import tkinter as tk
import tkinter.ttk as ttk
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Py Flashcards")
        self.current_card = {}
        self.correct_count = 0
        self.total_count = 0
        self.selected_category = "All"
        self.filtered_cards = flashcards  # 👈 Start with all cards

        # Category dropdown
        self.category_label = tk.Label(root, text="Choose a category:", font=("Helvetica", 12))
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, state="readonly")
        self.category_dropdown['values'] = self.get_unique_categories()
        self.category_dropdown.current(0)
        self.category_dropdown.bind("<<ComboboxSelected>>", self.on_category_change)
        self.category_dropdown.pack(pady=5)

        # Flashcard UI
        self.question_text = tk.Text(root, height=4, width=50, font=("Helvetica", 16), wrap="word")
        self.question_text.config(state="disabled", bg=root.cget("bg"), relief="flat")
        self.question_text.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack()

        self.answer_button = tk.Button(root, text="Show Answer", command=self.check_answer)
        self.answer_button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next Flashcard", command=self.next_card)
        self.next_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0/0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.next_card()

    def get_unique_categories(self):
        categories = {"All"}
        for card in flashcards:
            if "category" in card:
                categories.add(card["category"])
            else:
                categories.add("Uncategorized")
        return sorted(categories)

    def on_category_change(self, _=None):
        self.selected_category = self.category_var.get()
        self.load_cards_by_category()
        self.next_card()

    def load_cards_by_category(self):
        if self.selected_category == "All":
            self.filtered_cards = flashcards
        else:
            self.filtered_cards = [
                card for card in flashcards
                if card.get("category", "Uncategorized") == self.selected_category
            ]

    def next_card(self):
        if not self.filtered_cards:
            self.question_text.config(state="normal")
            self.question_text.delete(1.0, tk.END)
            self.question_text.insert(tk.END, "No flashcards available.")
            self.question_text.config(state="disabled")
            return

        self.current_card = random.choice(self.filtered_cards)
        self.question_text.config(state="normal")
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(tk.END, self.current_card['question'])
        self.question_text.config(state="disabled")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        user_input = self.answer_entry.get().strip()
        correct_answer = self.current_card['answer'].strip()

        self.total_count += 1
        if user_input.lower() == correct_answer.lower():
            self.correct_count += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Incorrect! Correct answer: {correct_answer}", fg="red")

        self.score_label.config(text=f"Score: {self.correct_count}/{self.total_count}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()



