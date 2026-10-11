import random
import time

name = input("Enter your name: ").strip()
midterm = int(input("Enter your Midterm Note: "))
final = int(input("Enter your Final Note: "))
avg = (midterm * 0.4) + (final * 0.6)
print(f"Your current average: {avg}" )

if avg >= 60:
    print("You've already passed; what business do you have in the professor's office? ")
else:
    print("You failed the course! You have three chances to convince the professor.")

    attempts_left = 3
    prof_mood = random.randint(1, 10) #it gives random number 1 to 10.

    print("\nYou are approaching the professor's door...")
    knock_count = 0
    while knock_count < 3: #it gives door knock effect.
        print("Knock...")
        time.sleep(1)
        knock_count += 1
    print("A voice from inside: 'Come in!'\n")
    print(f"Professor mode: {prof_mood}")
    print(f"What is your problem {name}")
    while attempts_left > 0:
        print(f"\nRemaining attempts: {attempts_left}")
        print("What will you say to the Professor?") #interaction choices for communication with professor.
        print("A) 'I worked really hard on the projects and did all bonus tasks.'")
        print("B) 'I was sick during midterm week, could you consider a makeup assignment?'")
        print("C) 'Can you give me any hints about what to study for retake exams?'")
        print("D) 'I give up, thank you anyway.'")

        choice = input("Your choice (a/b/c/d): ").strip().lower()

        if choice == "a":
            print("The professor is reviewing your project submissions...")
            time.sleep(1)
            if prof_mood > 4:
                print("Professor: 'Impressive dedication! Adding +10 bonus point.'")
                avg = avg + 10
                break
            else:
                print("Instructor: 'The effort is acknowledged, but late submissions cannot get extra credit.'")
                attempts_left -= 1
        elif choice == "b":
            print("The instructor is verifying your medical report...")
            time.sleep(1)
            if prof_mood > 7:
                print("Instructor: 'Get well soon. I will grant you +15 curve points this once.'")
                avg = avg + 15
                break
            else:
                print("Instructor: 'Official report submission deadline has already passed.'")
                attempts_left -= 1
        elif choice == "c":
            print("Instructor: 'Make sure to master while loops and conditional statements for the makeup exam!'")
            attempts_left -= 1

        elif choice == "d":
            print("You politely excused yourself and left the room...")
            break

        else:
            print("Invalid option! Please choose A, B, C, or D.")

print("\nMEETING SUMMARY")
if avg >= 60:
    print(f"Congratulations {name}! New average: {avg:.1f} | Status: PASSED!")
else:
    print(f"{name} negotiation failed. Final average: {avg:.1f} Status: FAILED (Study hard for retakes)!")