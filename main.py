from flashcards.engine import show_random_flashcard, study_mode

def main():
    print("\n🧠 Welcome to Py-Syntax Flashcards!")
    print("Choose a mode:")
    print("  r → Regular Mode (one random flashcard)")
    print("  s → Study Mode (go through all flashcards)")
    print("  q → Quit")

    choice = input("\n👉 Your choice: ").strip().lower()

    if choice == "r":
        show_random_flashcard()
    elif choice == "s":
        study_mode()
    elif choice == "q":
        print("\n👋 Goodbye, see you next session!")
    else:
        print("\n❌ Invalid input. Please try again.")

if __name__ == "__main__":
    main()


