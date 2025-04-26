# Handle user mood input
# Limited mood selection logic

def get_user_mood(allowed_moods):
    print(f"Select your mood: {', '.join(allowed_moods)}")
    mood = input("Enter mood: ")
    while mood not in allowed_moods:
        print("Invalid mood. Please choose from the list.")
        mood = input("Enter mood: ")
    return mood