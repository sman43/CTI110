#Kenneth Annan
#3/1/25
#P2HW2
#Grade Averaging
import math
keep_going='yes'
num_scores=int(input('How many scores do you want to collect? '))
scores_counted=[]
for i in range(num_scores):
    while True:

        score = float(input(f'Enter score {i + 1}: '))

        if score >= 0 and score <= 100:
            scores_counted.append(score)   
            break
        else:
            print('Enter a score between 0 and 100.') 

print('Scores Entered: ', scores_counted)

low=min(scores_counted)
high=max(scores_counted)
tot=sum(scores_counted)
av=float(tot/len(scores_counted))

print('-----------results-----------')
print(f'{'Lowest Grade:':<20} {low:.2f}')
print(f'{'Highest Grade:':<20} {high:.2f}')
print(f'{'Sum of Grades:':<20} {tot:.2f}')
print(f'{'Average:':<20} {av:.2f}')

print('-----------'*4)