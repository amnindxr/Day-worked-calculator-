import json

print('Working Days Calculator')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

myList = {}

for day in range(0, 7):
    while True:

        print(f' Did you work on {days[day]} ?')
        user_input = input("Enter an answer: ").lower()

        if user_input in ['yes', 'no']:
            myList.update({days[day]: user_input == 'yes'})
            print(f'you worked {sum(myList.values())} days')
            break
        else:
           print('Sorry, I didn\'t understand your answer')

with open('workweek.json', 'w') as f:
    json.dump(myList, f)

print(f'Your list {myList}')

print(f'you worked {sum(myList.values())} days')
