is_weekend = input("Is it the weekend? (yes/no): ").lower() == "yes"
is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"
homework_done = input("Is homework done? (yes/no): ").lower() == "yes"

if is_sunny and homework_done:
    print("Go outside!")

if is_weekend or is_sunny:
    print("Good day to relax.")

if not homework_done:
    print("Finish your homework first.")

if not is_weekend and homework_done:
    print("You are ready for school tomorrow.")
elif not homework_done and not is_sunny:
    print("Stay inside and complete your work.")
    