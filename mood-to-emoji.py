# Mood to Emoji Converter

print("How are you feeling today?")
mood = input("Type a word to describe your mood: ").lower()

emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "tired": "😴",
    "excited": "🤩",
    "bored": "😐",
    "anxious": "😰",
    "loved": "❤️"
}

if mood in emoji_dict:
    print("Here’s your mood in emoji form:", emoji_dict[mood])
else:
    print("I don't know that mood yet, but ask my developer, Sagan, to add it.")
