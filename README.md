# PythonAntiScamTool
This tool ist a quick an dirty programm to confuse phishing sites. 

# The Story
A reddit user postet in the /csgo thread. 
```
"[PSA] Fishing csgo website!!
Hello, i don't know if this is the best place for posting this. 
I have been a victim of phising in the following website: https://csgoxxmagic.pro/. 
I'm trying to recover my Steam account and i would like to advise everyone about this website. 
Definitly not legit ;(."
```
So i decidet to take a look at the phishing site.
And OMG! Probs to the guy who codet this! OMFG this looks so damn real! His Idea to build a frame inside hist Page so he can fake the Valve SSL picture is amazing! I am very impressed about the creativity this scammer uses!
But at least he steal accounts with this page so it is crap. So sad...
But i was so amazed that i decidet to write a code where i try my thousands steam accounts... because i reaaaalllyyy didnt knew exactly my email an password i tried a lot of them ;)

# The "Magic"
It is very simple. I use a txt file of round about 4000 first names wich i found on github. I read the file in a list and generate a email (name@gmail.com) and a passwort (nameXXXX) and start a urllib open with the GET request wich i scanned on the website by typing in some test data on the login field.

# Installation
You only need urllib. The rest is simplest Python.

# Disclaimer
ONLY use this for yourself. NEVER bomb websites with login fields! Hacking ist illegal!
