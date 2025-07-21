# ✅↓ Write your code here ↓✅
def sing():
    lyrics = ""
    for count in range(11):
        if count == 4:
            lyrics = lyrics + "there will be an answer,\n"
        elif count == 10:
            lyrics = lyrics + "whisper words of wisdom, let it be"
        else:
            lyrics = lyrics + "let it be,\n"
    return lyrics

print(sing())

