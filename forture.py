# fortune.py (v1.0)
print("🔮 Welcome to Keshav Gupta's Fortune Teller (21JE0467) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Keshav! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Tough times don't last, but tough people like you do. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Peace of mind leads to great clarity. ✨")
else:
    print("✨ Your fortune: Every feeling is valid. Take time to reflect. ✨")
