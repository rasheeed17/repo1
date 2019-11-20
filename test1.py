line 1


Question:  How can we revert a change which is already committed and pushed to git hub repository?
Answer:
"GIT revert" is used to revert the changes
GIT push origin master
If an automatic CI is deployed using Jenkins then there is a chance that code deployed is already deployed by Jenkins.

Question:  Have you made mistakes and corrected?
Answer:
- Inconsistent code is pushed because of insufficient testing, reverted the code and
- automate testing functionality to test code after every gitcommit
- use Docker for same environment
- use micro services to reduce the impact on  functionalities other than updated one
- overcome risks to avoid failure before pushing the code

