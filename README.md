# mis203-basic-programming
Mehmet
2404109070
Managament Information Systems
Basic-Programming
Week 2 grade_calculator.py
    -AI Tool Used: None
    -Promt Used: None
    -I didn't change anything i wrote  my own knowledge.
    -'BREAK' terminates the loop.

Week 3 ticket_office.py
    AI Tool Used: Gemini,
    Prompt Used: ValueError: invalid literal for int() with base 10: 'a' how can i fix this error.
    I added .isdigit() function for value error.
    tests: input name:Ali, age:12, day:weekend, student:yes output: Ali: 150.00 TRY (Child), Mehmet, Age: 65, Day: weekday, Student: no Output: Mehmet: 100.00 TRY (Senior)
    Name: Can, Age: 5, Day: weekday, Student: no Output: Can: 0.00 TRY (Free)
    
    python checks conditions in order and applies only the first matching discount. If the student rule came before the child rule, a 10 year old student would receive only a %30 discount instead of the intended 40% child discount.
Week 4 surprise.py
    AI Tool Used: Codex
    Promt Used: how can i use random and time library tell me syntax then added into code.
     
    its a communication simulator between student and professor. The student who want to pass lecture. I used random library for professor mood dynamics and time library for the door knocking effect. If the student fails the initial threshold, they get three attempts to negotiate and raise their average during office hours. 
    Test:   Enter your name: mehmet
            Enter your Midterm Note: 50
            Enter your Final Note: 60
            Your current average: 56.0
            You failed the course! You have three chances to convince the professor.

            You are approaching the professor's door...
            Knock...
            Knock...
            Knock...
            A voice from inside: 'Come in!'

            Professor mode: 9
            What is your problem mehmet

            Remaining attempts: 3
            What will you say to the Professor?
            A) 'I worked really hard on the projects and did all bonus tasks.'
            B) 'I was sick during midterm week, could you consider a makeup assignment?'
            C) 'Can you give me any hints about what to study for retake exams?'
            D) 'I give up, thank you anyway.'
            Your choice (a/b/c/d): a
            The professor is reviewing your project submissions...
            Professor: 'Impressive dedication! Adding +10 bonus point.'

            MEETING SUMMARY
            Congratulations mehmet! New average: 66.0 | Status: PASSED!