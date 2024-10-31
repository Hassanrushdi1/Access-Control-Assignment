import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_recognize():
    with sr.Microphone() as source:
        print("Clearing noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("Hmm, I'm not sure how to respond to that.")
            return None

        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service.")
            return None


users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}


def check_access(user, password):
    if user in users and users[user]["password"] == password:
        return users[user]["role"]
    else:
        return None


def main():
    username = input("Enter Username ")
    password = input("Enter Password ")
    role = check_access(username, password)
    if role:
        print(f"Access for {role}")
        not_end = True
        while not_end:
            command = speech_recognize()
            print(f"You Said: {command}")
            if command:

                if role == "admin":
                    if command == "reset":
                        print(" Reseting now .....")

                    elif command == "delete file":
                        print("deleting file")

                    elif command == "status":
                        print("System is running smoothly.")

                    elif command == "add profile":
                        print("Please provide a username and password to add a new user.")

                    elif command == "change profile":
                        print("Please provide a username and new password.")    

                    elif command == "exit":
                        print("Good Bay!")
                        not_end = False    
                    else:
                        print("Not known Command")

                elif role == "user":
                    if command == "open":
                        print("Opening profile...")

                    elif command == "update":
                        print("Please provide the details to update your profile.")

                    elif command == "view profile":
                        print("Displaying your profile information...")

                    elif command == "send message":
                        print("Please provide the message to send.")

                    elif command == "list command":
                        print("Available commands: Open, Update Profile, View Profile, Send Message, Exit.")
                        
                    elif command == "exit":
                        print("Good Bay!")
                        not_end = False  
                    else:
                        print("Not known command")
    else:
        print("denied access")

main()      
