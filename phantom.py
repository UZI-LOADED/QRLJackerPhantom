import os
import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def command_center():
    print("👁️  PhantomBot Activated")
    speak("Phantom Bot Activated")
    while True:
        cmd = input("PhantomBot > ").strip().lower()
        if cmd == "!help":
            print("""
!help              → Show this menu
!deploy discord    → Deploy Discord QR clone
!deploy paypal     → Deploy PayPal QR clone
!speak <message>   → Phantom speaks it
!exit              → Exit bot
            """)
        elif cmd.startswith("!speak"):
            _, *words = cmd.split()
            speak(" ".join(words))
        elif cmd == "!deploy discord":
            print("[*] Launching Discord clone...")
            speak("Launching Discord clone.")
            os.system("start http://localhost:5000/discord")
        elif cmd == "!deploy paypal":
            print("[*] Launching PayPal clone...")
            speak("Launching PayPal clone.")
            os.system("start http://localhost:5000/paypal")
        elif cmd == "!exit":
            speak("Phantom departing.")
            break
        else:
            print("Unknown command. Type !help.")

if __name__ == "__main__":
    command_center()
