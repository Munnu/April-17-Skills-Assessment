class Student(object):
    """ Student class holds the first name,
        last name, and address of a student """
    

    def __init__(self, first_name, last_name, address):
        """ initialize Student object parameters """

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = 0
        self.student_assessments = {}
        self.student_assessments['exams'] = {}
        self.student_assessments['quizzes'] = {}
        
    def associate_assessment_with_student(self, assessment, score):
        """ add the assessment (quiz, exam) and score to a dictionary """
  
        # sets the score and gets the assessment_type
        self.score = score
        assessment_type = assessment.assessment_type

        # doing dictionary construction stuff
        if assessment_type == 'Exam':
            self.student_assessments['exams'][assessment.name] = {
                                                                  'exam object': assessment, 
                                                                  'score': self.score 
                                                                 }
        elif assessment_type == 'Quiz':
            self.student_assessments['quizzes'][assessment.name] = {
                                                                    'quiz object': assessment, 
                                                                    'score': self.score 
                                                                   }



class Question(object):
    """ Question class holds each 
        question and its correct answer """

    def __init__(self, question, correct_answer):
        """ initialize Question object parameters """

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate_user_answer(self):
        """ ask_and_evaluate_user_answer 
            take a Question object type,
            print the self.question, then
            check the user's answer against self.answer """

        # get the user input and ask the question
        user_input = raw_input(self.question + " ")
        user_input = user_input.strip()

        if user_input == self.correct_answer:
            return True
        return False



class Exam(object):
    """ Exam class holds the exam name and 
        all the questions contained in that exam"""

    def __init__(self, name, assessment_type = None): 
        """ initialize Exam object parameters """

        # will store a list of question object types
        # assuming each exam object type  will have 
        # its own unique set of questions
        self.questions = [] 
        self.name = name

        if assessment_type:
            self.assessment_type = assessment_type

    def insert_an_exam_question(self, individual_question, correct_answer):
        """ create a Question object then 
            insert it into 'question' list 
            passes in individual_question and its correct_answer """

        # instantiate a Question object
        exam_question = Question(individual_question, correct_answer)

        # append the exam_question to the questions list
        self.questions.append(exam_question)

    def administer(self):
        """ method to administer exam questions
            one by one to the user, tally the exam score """

        number_of_correct_answers = 0 
        score_percentage = 0

        # loop through each exam question 
        for question in self.questions:
            # and ask the user each question
            is_correct_answer = question.ask_and_evaluate_user_answer()

            # when correct, update the number_of_correct_answers
            if is_correct_answer:
                number_of_correct_answers = number_of_correct_answers + 1

        score_percentage = float(number_of_correct_answers)/len(self.questions)
        return score_percentage
            


class Quiz(Exam):
    """ Quiz inherits Exam's functionality """
    
    # Hey, I have a question: 
    # I want to make this nicer, so, I thought it would be better
    # if I passed in something that checks to see what type of obj
    # is being passed into exam, and if it is an exam, it's a decimal percentage
    # value being returned to administer. If not, return a True/False
    # for passing... Is this the right step? How should I consider this part
    # in a more elegant way?
    def administer(self):
        """ administer method checks to see if user passes quiz 
            inherits Exam's administer method"""

        # inheritance
        quiz_score = super(Quiz, self).administer()

        # quiz is a pass/fail thing
        if quiz_score < 0.5:
            return False
        else:
            return True



def take_test(assessment, student):
    """ uh oh, it's exam time.
        function starts the exam for the student """

    # administer exam
    student_score = assessment.administer()

    # put the student's exam and score into a dict
    student.associate_assessment_with_student(assessment, student_score)

    # print the dictionary out
    print student.student_assessments



def example():
    """ creates an exam, then adds questions,
        then creates a student and administers the exam """

    # create a new student
    andrea = Student('Andrea', 'Pineapple', '1234 Street, Dallas, TX 74209')

    # -------------------------------------------------------
    # creates a new exam object
    new_exam = Exam('basic math exam', assessment_type='Exam')

    # add a question and a correct answer to the exam
    new_exam.insert_an_exam_question("What's 1+1?", "2")
    new_exam.insert_an_exam_question("What's 2+2?", "4")
    new_exam.insert_an_exam_question("What's 3+3?", "6")

    # administer exam
    take_test(new_exam, andrea)

    # -------------------------------------------------------
    # creates a new quiz object
    new_quiz = Quiz('basic math quiz 2', assessment_type='Quiz')

    # add a question and a correct answer to the exam
    new_quiz.insert_an_exam_question("What's 1*1?", "1")
    new_quiz.insert_an_exam_question("What's 2*2?", "4")
    new_quiz.insert_an_exam_question("What's 3*3?", "9")

    print "This is the list of quiz questions:", new_quiz.questions

    # administer exam
    take_test(new_quiz, andrea)


example()
