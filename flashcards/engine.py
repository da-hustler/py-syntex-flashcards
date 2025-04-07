import random
from flashcards.data import flashcards  # ✅ CORRECT

# 🔁 Regular Mode — Show 1 random flashcard
def show_random_flashcard():
    card = random.choice(flashcards)
    input(f"\n❓ {card['question']} (press Enter to see the answer...)")
    print(f"✅ Answer: {card['answer']}\n")

# 🧠 Study Mode — Loop through ALL flashcards
def study_mode():
    print("\n🎓 Study Mode Activated! Type 'q' at any time to quit.\n")

    for card in flashcards:
        user_input = input(f"❓ {card['question']} (press Enter to see the answer, or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("\n👋 Exiting Study Mode. Great work today!\n")
            break
        print(f"✅ Answer: {card['answer']}\n")
