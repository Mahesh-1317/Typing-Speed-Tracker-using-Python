import time
import random

sentences = [
    "Python is easy to learn",
    "Coding improves logical thinking",
    "Mogembo khush hua",
    "Billo bagge billiya da ki karegi",
    "Salman Khan wants to smoke cigeratte",
    "Why did Katappa kill Bahubali?"
]

type_text = random.choice(sentences)
print("Type the following sentence: ")
print(type_text)
print()

start_time = time.time()

typed = input("Enter text: ")
print()

end_time = time.time()
time_taken = end_time - start_time
print(f"Time Taken: {round(time_taken,2):>10} sec")

words = len(type_text.split())
print(f"Word Typed: {words:>6}")

if time_taken > 0:
    WPM = words / (time_taken / 60)
    print(f"Typing Speed: {round(WPM):>5} WPM")


original_words = type_text.split()
typed_words = typed.split()
mistakes = 0
for i in range (min(len(original_words), len(typed_words))):
    if original_words[i] != typed_words[i]:
        mistakes += 1
mistakes += abs(len(original_words) - len(typed_words))
print(f"Mistakes: {mistakes:>8}")


correct = 0
for i in range (min(len(type_text), len(typed))):
    if type_text[i] == typed[i]:
        correct += 1
accuracy = (correct / len(type_text)) * 100
print(f"Accuracy: {round(accuracy):>9}%")