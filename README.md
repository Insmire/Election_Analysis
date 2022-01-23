# Election_Analysis

<!-- Overview of Election Audit: Explain the purpose of this election audit analysis. -->
## Overview
The purpose of this audit is to read a simulated election results from csv file, analyze data with a separate py file, then write the results of analysis to a txt file. Project objectives include calculations of 
  1. Total vote count
  2. Number and percentage of votes per county
  3. County with the largest turnout
  4. Number and percentage of votes percandidate
  5. Winning candidate based on popular vote

## Resources
Data source: election_results.csv

Software: Python 3.9.7, Visual Studio Code (VSCode) 1.63.2

<!-- Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
- How many votes were cast in this congressional election?
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes? -->
## Results
- A total of 369,711 votes were cast for the election. 
- The counties
  - Jefferson county
  - Denver county
  - Arapahoe county
- The county results
  - Jefferson county cast roughly 10.5% of the vote and 38,855 of votes;
  - Denver county cast roughly 82.8% of the vote and 306,055 of votes;
  - Arapahoe county cast roughly 6.7% of the vote and 24,801 of votes.
- The largest turnout of the election
  - Denver county that cast 82.8% of the vote and 306,055 of votes.
- The candidates
  - Charles Casper Stockham 
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results
  - Charles Casper Stockham received about 23.0% of the votes and 85,213 of votes;
  - Diana DeGette received about 73.8% of the vote and 272,892 of votes;
  - Raymon Anthony Doane received about 3.1% of the vote and 11,606 of votes. 
- The winner of this election
  - Diana DeGette, who received 73.8% of the vote and 272,892 of votes.
  
Initialized variables are shown below.
![election_analysis_initialize_variables](https://user-images.githubusercontent.com/96349090/150667614-7c52521e-e752-445a-8079-3193395cdc3c.png)

File opened and analysis calculations are shown below.
![election_analysis_read_to_file](https://user-images.githubusercontent.com/96349090/150667660-5f57a42d-9d47-44de-856d-3ca12a0afc3f.png)

Write-to file and result calculations are shown below.
![election_analysis_write_to_file](https://user-images.githubusercontent.com/96349090/150667666-d4caef76-6a7a-4773-8822-811295dcfa1c.png)

Analysis results are shown below.
![election_analysis_output](https://user-images.githubusercontent.com/96349090/150668286-b09ca0d7-a916-4744-8143-01c70e6da6b6.png)

<!-- Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections. -->
## Summary
With some modifications, codes for this election may be adapted for any election. One such modification is to use Jupyter Lab/Notebook to confirm calculations are executed smoothly with every line of code. Another modification is to streamline the script by reading the file only once to effectuate all ouputs. Notice calculations and printing for counties are similar to that of the candidates, implying that the script can be simplified with either [built-in functions, constructed generators, or list comprehensions](https://www.geeksforgeeks.org/tips-to-improve-the-performance-of-python-application/). More efficient codes take up less memory space. Lastly, the variables may benefit from [re-naming](https://www.python.org/dev/peps/pep-0008/#naming-conventions) to maintain readability and ensure style consistency.
