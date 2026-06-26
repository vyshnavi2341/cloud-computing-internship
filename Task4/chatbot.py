responses = {

"hello":"Hi, Welcome",

"hi":"Hello",

"how are you":"I am Fine",

"course":"Cloud Computing Internship",

"bye":"Good Bye"

}


while True:

    user = input("You : ").lower()

    if user in responses:
        print("Bot :",responses[user])

    else:
        print("Bot : Sorry I don't understand")

    if user=="bye":
        break
