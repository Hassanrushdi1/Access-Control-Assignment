import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_recognize():
    with sr.Microphone() as source:
        print("Clearing noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("Hmm, I'm not sure how to respond to that.")

        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")


def conversation():
    not_end = True
    while not_end:
        user_input = speech_recognize()
        if user_input is not None:
            print(f"You Said: {user_input}")
            if "hello" == user_input.lower():
                print("Hello! How can I help you?")

            elif "what is your name" == user_input.lower():
                print("You can call me Chatbot!")

            elif "what can you do" == user_input.lower():
                print("I can answer your questions!")

            elif user_input.lower() == "exit":
                print("Goodbye! It was nice talking with you. Have a great day!")
                not_end = False

            else:
                print("Hmm, I'm not sure how to respond to that.")
conversation()