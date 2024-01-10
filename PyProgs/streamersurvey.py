#  Task-1: A YouTube streamer decided to conduct a survey where users
#  were asked to provide feedback on what they would like to watch in the
#  next stream. Your job is to create a program that uses the following
# information and prints out the result of what the user chose, along with a
#  thank you message.
#  What shall I stream next?
#  a)    Days Gone
#  b)   Resident Evil 2
#  c)    Fortnite
#  d)   Apex Legends
#  e)    Death Stranding
#  f)      Surprise Us!
#  The ending message should be:
#  You have chosen (option). I appreciate your time and hope to see you in
#  the next one


print("welcome to my survey to choose what to stream next")

print("What shall I stream next? ")
print("a) Days Gone")
print("b) Resident Evil 2")
print("C) Fortnite")
print("d) Apex Legends")
print("e) Death Stranding")
print("f) Surprise Us!")

next_stream = input("What do you think?: ").lower()


if next_stream == "a" or next_stream == "b" or next_stream == "c" or next_stream == "d" or next_stream == "e":
    print(f"You have chosen {next_stream} I appreciate your time and hope to see you in the next one")
else:
    print("Surprise US!")
