# Enhancement One – Software Design and Engineering

## Briefly describe the artifact. What is it? When was it created?

This artifact is the final project I submitted for IT-140 in August 2023. The program is a text-based adventure written in Python where the player explores a castle to collect items that will help you defeat the dragon hiding somewhere within. While this program is relatively simple, it has useful features such as navigation, an inventory system, win/lose conditions, and more.

## Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in software development? How was the artifact improved?

This was the first full program I ever created, and I selected it for all three capstone enhancements to showcase how my skills have grown since entering the computer science program. Using this project gives me the opportunity to revisit my work from my first term and explore how I would do things differently in my final term with the knowledge I’ve acquired throughout the program.

The focus of this milestone is software design and engineering. For my first enhancement, I chose to implement a start menu that would separate menu and gameplay functionality while improving the user experience and laying the groundwork for future feature expansion. The menu code block can be seen here:

This code now includes the show_instructions() method that previously was included in the main gameplay loop. This menu supports a larger refactoring effort to increase modularity by separating gameplay, menu, and program logic. To further this effort, I implemented a new run_game() method that will handle only the gameplay. Gameplay logic was previously built into main(), which does not follow best practices. The new main function is now much cleaner and modular, calling the menu and run_game() methods when applicable and also laying the groundwork for the load game/database enhancement that will be included in enhancement 3.

I also made some minor enhancements and code changes as a bit of house cleaning separate from the main enhancement. These include adding .strip() to better handle user input values and removing some redundant global variable definitions

## Did you meet the course outcomes you planned to meet with this enhancement in Module One? Do you have any updates to your outcome-coverage plans?

During assignment one, I identified that this enhancement would best align with course outcomes numbers 2, 3, and 4 and I think that remains true. This change most strongly aligns with course outcome 4 and my goal was to showcase software design and engineering principles. These principles are exemplified in my effort to modularize my code, separate concerns (gameplay/menu logic), and improve the overall flow of the program while laying foundational work for future enhancements.

Outcome 2 is also met with the menu, as the new menu-driven gameplay improves program flow, communication with the user, and a much more intuitive user experience while improving overall technical soundness. Outcome 3 will be more thoroughly covered in enhancement 2 but is touched upon here during management of scope creep and design decision trade-offs.

I would add outcome 5 to this enhancement as well. Although a small change, adding strip() to the menu input logic mitigates design flaws and demonstrates a security mindset by anticipating potential exploits of incorrect user input.

## Reflect on the process of enhancing and modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face?

This was a wonderful experience with many lessons learned. An important takeaway was the realization that what you may envision as a relatively self-contained change may need a much larger refactoring and organization of the codebase. While I had a vision for the code and implementation of the start menu, defining the new start_menu() method was only one piece. Since the user would now have the option to start a game or view instructions when desired, these previously merged functions needed to be separated. This ultimately led to needing to create the run_game() method and then an update to main() to handle the newly modularized functions.

During my code review, I couldn’t help but notice all the areas I wanted to improve. It was difficult to leave those be for now and focus on the menu. I tried to limit any additional code changes outside of this enhancement’s scope to ones that would better support the program in relation to the menu option and that would also lay some foundational work for the next two enhancements.
