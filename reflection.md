# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

*The first thing I noticed was that the first attempt didn't decrement after my first guess, it was only after the second that it started to go down. Next, the feedback is backwards, and prompts me to go higher when the actual secret is lower.*

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

*I used Copilot and Claude for this project, and they correctly identified the issues with the check_guess() functions, and performed a refactor without any issues. I ran into an issue where Claude suggested a fix so that the "attempts left" info correctly decrements with each submission, but it created another bug in the process, where the hints would no longer show*

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

*I decided a bug was fixed by looking at the code myself, and determining whether the logic made sense. For example, after the agent refactored the check_guess() function, I reread the code and made sure the imports were logical. Additionally, I performed manual tests in the streamlit app by playing the game and noticing whether the hints were accurate. I also ran tests using pytest, which Copilot also refactored to see if the hints were correct. This enhanced the effectiveness of the tests, as they weren't simply checking for correctness, but also the accuracy of the hints*

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - *The secret number kept changing in the original app, as it would alternate between an int and a string each attempt, making the check for guess inconsistent*
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - *I'd describe sessions state and reruns similar to how React handles state. Regular variables will reset when the app reruns, and not be preserved. As a result, session state variables are necessary to preserve variable values for functions like incrementing and updating values*
- What change did you make that finally gave the game a stable secret number?
  - *In the refactored check_guess function, I casted both the guess and the secret number to an int the ensure consistent checking*



## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - *One habit I'd like to reuse is to remain skeptical about AI suggestions, and to check and test all the code proposed*
- What is one thing you would do differently next time you work with AI on a coding task?
  - *Something I'd like to do do differently next time I work with AI on a coding task is to welcome agentic programming, now that I have a better understanding of how to properly use it. I used to never rely on agents, out of fear that it'd inhibit my understanding*
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - *This project changed the way I think about AI generated code, as although it reinforced that AI can certainly make mistakes, that doesn't mean it's use should be entirely omitted. AI can serve as a powerful debugging and comprehension tool for unfamiliar codebases, and can serve as an essential component in the debugging process*
