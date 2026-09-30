AI Tool Used: Gemini,
Prompt Used: ValueError: invalid literal for int() with base 10: 'a' how can i fix this error.
I added .isdigit() function for value error.
tests: input name:Ali, age:12, day:weekend, student:yes output: Ali: 150.00 TRY (Child), Mehmet, Age: 65, Day: weekday, Student: no Output: Mehmet: 100.00 TRY (Senior)
Name: Can, Age: 5, Day: weekday, Student: no Output: Can: 0.00 TRY (Free)
python checks conditions in order and applies only the first matching discount. If the student rule came before the child rule, a 10 year old student would receive only a %30 discount instead of the intended 40% child discount.
