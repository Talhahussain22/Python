import win32com.client as wincom

import time

speak=wincom.Dispatch("SAPI.SpVoice")
text="Are you ready to speak"
speak.Speak(text)

time.sleep(3)
text2="This is speaking after a pause of 3 seconds"
speak.Speak(text2)

l=["Talha","Nabeed","Awwab","Abyaz"]
for i in l:
    speak.Speak(f"Shout out to {i} ")