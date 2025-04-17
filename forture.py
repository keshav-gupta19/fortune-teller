# fortune.py (v1.1)
import random

print("🔮 Welcome to Keshav Gupta's Fortune Teller (21JE0467) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        "Great things await you, Keshav! Keep smiling.",
        "Your joy is contagious. Spread it!",
    ],
    "sad": [
        "Even the darkest night ends with dawn.",
        "Keshav, you're stronger than your sorrow.",
    ],
    "neutral": [
        "Balance is a blessing in disguise.",
        "Your calm brings clarity.",
    ],
    "stressed": [
        "Breathe, Keshav. This too shall pass.",
        "Stress fades when you believe in yourself.",
    ]
}

fortune = random.choice(fortunes.get(mood, ["Emotions guide growth. You're on a path."]))
print(f"✨ Your fortune: {fortune} ✨")
