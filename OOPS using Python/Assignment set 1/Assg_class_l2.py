class Instructor:
    def __init__(self):
        self.__avg_feedback=None
        self.__technology_skill=[]
        self.__instructor_name=None
        self.__experience=None

    def set_experience(self, experience):
        self.__experience = experience
    
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
    
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
    
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
    
# getter functions

    def get_experience(self):
        return self.__experince 
    
    def get_instructor_name(self):
        return self.__instructor_name 

    def get_avg_feedback(self):
        return self.__avg_feedback
    
    def get_technology_skill(self):
        return self.__technology_skill

    def check_eligibility(self) :
        if self.__experience>3 and self.__avg_feedback>=4.5:
            return True
        elif self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
        
    def allocate_course(self,technology):
        if self.check_eligibility()==True:
            if technology in self.__technology_skill:
                return True
            else:
                return False
        else:
            return False
        
obj = Instructor()
obj.set_instructor_name("Kunal")
obj.set_experience(4)
obj.set_technology_skill(["Python", "C++", "Javascript"])
obj.set_avg_feedback(4.2)
print(obj.check_eligibility())
print(obj.allocate_course("C++"))