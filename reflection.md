# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Hint was backwards. i.e. if guess was higher than secret number, hint would say 'Go Higher' instead of 'Go Lower'.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|Guess of 10 (secret number 35)|"Go HIGHER" hint|"Go LOWER" hint|"None"|
| Total attemps less by 1 (eg. difficulty=normal, attempts=8, actual entries allowed=7|Should allow 8 attempts |Allows only 7 attempts|Out of attempts! Attempts left: 1|
| New game does not reset state|Clicking on new game should reset all state| Resets secret and attempts. Does not reset score and history. Does not allow new attempt/submission|None|
|Submit guess does not clear the textbox |On Sumbit guess button, textbox should be cleared and score, attempts,history should be updated. |Submit guess does not update session state, need to manually clear text box |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude and ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Issue: New game button was not working
*What AI suggested*: 
 I identifed that history and score were not being reset when new game was being started. AI also suggested that status needs to be reset to playing.
*Whether suggestion was correct or misleading*: 
 AI's suggestion was correct and it handled code fix correctly.
*How you verified the result in the code or game*: 
 Verified the fix by running the game and checking Developer Debug Info when new game is clicked. I prompted AI to help write unit tests, but that would need refactoring since current logic is embedded inside streamlit logic. I will handle this as an enhancement. 

2. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Issue: Hint for Go Higher or Go Lower was backwards (bug #1). 
*What AI suggested* :
 When prompted AI to fix it, it suggested fixing the check_guess() function to fix the comparison logic which was reversed in both try and except blocks. 
*Whether suggestion was correct or misleading*:
 It was partially correct. It fixed the comparison logic but did not catch the simulated glitchy code which was sending string input to this method in the first place. i.e. in AI's own words, 'I fixed the symptom without investigating the cause'.
*How you verified the result in the code or game*:
 Verified code and removal of glitchy behavior by runinng the app and testing, and adding unit tests in test_logic_utils.py

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
In most cases, added unit tests. In remaining cases, manually verified by running the app and simulating the old buggy behaviour. 
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  python3 -m pytest test_logic_utils.py -v
  This ran tests for hint backwards bug. It helped me test for all edge cases much easier than running the app.
  
- Did AI help you design or understand any tests? How?
Yes, AI helped me add some edge cases to tests. In fact, it also added a design pattern initially of one function per test case. This was too verbose and spreads logic across entire file. So I prompted it to help combine all related test case into one function eg test_check_guess() checks all check_guess() cases.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
