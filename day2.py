print("Shridevi Institute of Engineering and Technology")
print("Student Feedback Collector\n")

feedbacks = []

while True:
    name = input("Enter student name: ")
    feedback = input("Enter feedback: ")

    feedbacks.append((name, feedback))

    choice = input("Do you want to add more feedback? (yes/no): ")
    if choice.lower() != "yes":
        break

print("\n----- All Student Feedbacks -----")
for i, f in enumerate(feedbacks, start=1):
    print(f"{i}. {f[0]} : {f[1]}")

print("\nThank you for your feedback!")
