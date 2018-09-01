#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in# random order, along with the answer key.

import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'AlaBama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
            'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files.
for quizNum in range(35):

    #Create the quiz and anwser key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    #Write out the header for the quiz.
    quizFile.write('Name: \n\nDate:\n\nPeriod:\n\n')
    quizFile.write( (' ' * 20 ) + 'State Capitals Quiz ( Form %s )' %(quizNum + 1 ) )
    quizFile.write( '\n\n')
    
    #Shuffle the order of the states.
    states = list( capitals.keys() )
    random.shuffle( states )
    print( states )

    #Loop through all 50 states. makeing a question for each.
    for questionNum in range(len(capitals)):

        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        #print(correctAnswer)
        wrongAnswers =  list( capitals.values())
        #print(wrongAnswers)

        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)        
        #print(wrongAnswers)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle( answerOptions )

        #Write the question  and answer options to the quiz files .
        quizFile.write('%s. What is the capital of %s?\n' % ( questionNum + 1, states[questionNum]))
    
        for i in range(4):
            quizFile.write( '%s. %s' % ( 'ABCD'[i], answerOptions[i]) ) 
            quizFile.write('\n')
        quizFile.write('\n')

        #Write the answer key to a file.
        answerKeyFile.write( '%s.%s ' % ( questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
