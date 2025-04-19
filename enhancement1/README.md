# Enhancement One Narrative – Software Design and Engineering

---

## Artifact Overview  
**What is it? When was it created?**

This artifact is the final project I submitted for IT-140 in August 2023. The program is a text-based adventure written in Python where the player explores a castle to collect items that will help you defeat the dragon hiding somewhere within. While this program is relatively simple, it has useful features such as navigation, an inventory system, win/lose conditions, and more.

---

## Why This Artifact?  
**Why did you select this item? What specific components showcase your skills and how was it improved?**

This was the first full program I ever created, and I selected it for all three capstone enhancements to showcase how my skills have grown since entering the computer science program. Using this project gives me the opportunity to revisit my work from my first term and explore how I would do things differently in my final term with the knowledge I’ve acquired throughout the program.

The focus of this milestone is **software design and engineering**. For my first enhancement, I chose to implement a **start menu** that would separate menu and gameplay functionality while improving the user experience and laying the groundwork for future feature expansion.  


> This start menu code now includes the `show_instructions()` method that previously was included in the main gameplay loop.  
> This menu supports a larger refactoring effort to increase modularity by separating gameplay, menu, and program logic.  
> To further this effort, I implemented a new `run_game()` method that will handle only the gameplay.  
> Gameplay logic was previously built into `main()`, which does not follow best practices.  
> The new `main()` function is now much cleaner and modular, calling the menu and `run_game()` methods when applicable and also laying the groundwork for the load game/database enhancement that will be included in enhancement 3.

I also made some minor enhancements and code changes as a bit of house cleaning separate from the main enhancement. These include:

- Adding `.strip()` to better handle user input values
- Removing some redundant global variable definitions

---

## Alignment to Course Outcomes  
**Did you meet the course outcomes you planned?**

During assignment one, I identified that this enhancement would best align with **Course Outcomes 2, 3, and 4**, and I think that remains true.

- **Outcome 2** is demonstrated through improvements in user experience and technical flow.
- **Outcome 3** is lightly touched here through design trade-off decisions, but will be more prominent in Enhancement Two.
- **Outcome 4** is most strongly aligned: My goal was to showcase software design and engineering principles through modularization and separation of concerns.
- **Outcome 5** should also be included now, as adding `.strip()` helps mitigate input flaws and supports a security mindset.

---

## 🔁 Reflection on the Process  
**What did you learn? What challenges did you face?**

This was a wonderful experience with many lessons learned. An important takeaway was the realization that what you may envision as a relatively self-contained change may need a much larger refactoring and organization of the codebase.

While I had a vision for the code and implementation of the start menu, defining the new `start_menu()` method was only one piece. Since the user would now have the option to start a game or view instructions when desired, these previously merged functions needed to be separated. This ultimately led to needing to create the `run_game()` method and then an update to `main()` to handle the newly modularized functions.

During my code review, I couldn’t help but notice all the areas I wanted to improve. It was difficult to leave those be for now and focus on the menu. I tried to limit any additional code changes outside of this enhancement’s scope to ones that would better support the program in relation to the menu option and that would also lay some foundational work for the next two enhancements.

---
