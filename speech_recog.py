import tkinter as tk
import speech_recognition as sr
import pyttsx3

class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Voice Assistant")
        self.root.geometry("500x300")

        self.engine = pyttsx3.init()
        
        self.create_widgets()

    def create_widgets(self):
        
        self.command_label = tk.Label(self.root, text="Your Command:", font=("Arial", 14))
        self.command_label.pack(pady=10)

        self.command_text = tk.Text(self.root, height=4, width=50, font=("Arial", 12))
        self.command_text.pack(pady=5)

        self.mic_button = tk.Button(self.root, text="🎤 Speak", font=("Arial", 14), command=self.activate_voice_command)
        self.mic_button.pack(pady=20)

        self.response_label = tk.Label(self.root, text="Assistant Response:", font=("Arial", 14))
        self.response_label.pack(pady=10)

        self.response_text = tk.Text(self.root, height=4, width=50, font=("Arial", 12))
        self.response_text.pack(pady=5)

    def activate_voice_command(self):
        """
        Capture user's voice command, process it, and provide a response.
        """
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.update_command_text("Listening...")
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            self.update_command_text(command)
            self.process_command(command)
        except sr.UnknownValueError:
            self.update_response_text("Sorry, I could not understand your command.")
        except sr.RequestError:
            self.update_response_text("Could not request results; check your internet connection.")

    def update_command_text(self, text):
        """
        Update the command text box with the recognized command.
        """
        self.command_text.delete(1.0, tk.END)
        self.command_text.insert(tk.END, text)

    def update_response_text(self, response):
        """
        Update the response text box with the assistant's response.
        """
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)
        self.speak_response(response)

    def process_command(self, command):
        """
        Process the user's command and provide an appropriate response.
        """
        command = command.lower()

        if "hello" in command:
            response = "Hello! How can I assist you today?"
        elif "your name" in command:
            response = "I am your interactive voice assistant."
        elif "weather" in command:
            response = "Currently, I can't check the weather, but I'll be able to do that soon!"
        else:
            response = "I'm not sure how to help with that."

        self.update_response_text(response)

    def speak_response(self, response):
        """
        Use the text-to-speech engine to speak the response.
        """
        self.engine.say(response)
        self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistant(root)
    root.mainloop()
