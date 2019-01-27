# Ask_Media
Python version - 3.7<br />
Step 1 :<br />
Created an environment called env<br />
Step 2 : <br />
Installed flask<br />
Step 3:<br />
Created app.py-the controller file which contains the source code of the program<br />
Problem:<br />
Default case: <br />
Takes in repository_name and user_name as the input as arguments then it makes a request to the github api to get the commit_activity data. <br />The response
is passed and we get the most active day of the week and the average number of commits for that day over thr last year of activity.<br />
Bonus 1:<br />
Additional to the repository_name and the user_name, takes raquest_range as the input for calculating the per-day average commits or by default takes a year.
Bonus 2:<br />
Takes the input arguments as repository_name, user_name and sort_order and output all the days of the week with the average commit value.<br />
If the sort_order = 1 then the output is in Descending order else ascending order.<br />
Tested the api-calls with Postman and the screenshots are included in the TEST CASES.docx file<br />
