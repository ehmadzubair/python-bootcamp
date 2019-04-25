# Python Bootcamp - Week 3

# Classes & Objects

# Population -> Classes

class Human:
    def __init__(self, gender, age, name, weight):
        self.gender = gender
        self.age = age
        self.name = name
        self.weight = weight

    def introduce(self):
        print('Im a human. Im going to introduce myself now')
        print('My name is: ' + self.name)
        print('My age is: ' + str(self.age))
        print('My weight is: ' + str(self.weight))
        print('My gender is: ' + self.gender)

    def walk(self):
        print('I am walking')

    def study(self):
        print('I am a simpe human. I dont know what to study')

    def sleep(self):
        print('I sleep 8 hours a day')


class Student(Human):
    def __init__(self, gender, age, name, weight, career_aspirations, subjects, institute_name):
        super().__init__(gender, age, name, weight)
        self.career_aspirations = career_aspirations
        self.subjects = subjects
        self.institute_name = institute_name

    def introduce(self):
        super().introduce()
        print('Student part begins here...')
        print('My aspirations are: {aspirations}'.format(aspirations=self.career_aspirations))






# =====================================================

# human_one = Human('F', 22, 'Qurat ul Ain', 50)
# human_two = Human('M', 12, 'Shahzaib', 65)

student_one = Student(
    gender='M',
    age=27,
    name='Hamza Kamal',
    weight=70,
    career_aspirations='i want to be a millionaire by 35',
    subjects=['Physics', 'Chemistry', 'Biology'],
    institute_name='Beaconhouse School System')

student_one.sleep()
