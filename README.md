# University Admissions Automater

This script takes a file of potential university candidates (or candidates of anything that take exam scores, really) and automatically selects the highest performing ones based on their interest level and test scores. The script will attempt to place students in their top departments based on how many students the department will be selecting. Students rank their top 3 departments in order. Departments factor in different test scores, and different combinations of scores.

## File Layout

The submitted file should be in the following format:

FirstName LastName PhysicsScore ChemistryScore MathScore ComputerscienceScore FinalScore Choice1 Choice2 Choice3

with FinalScore being a final exam that, if higher than the average of the other required tests, will be used for admission.

## Outcome

The final results will be output in a .txt file with the department name and top performing students. Sample files have been included for a trial run.
