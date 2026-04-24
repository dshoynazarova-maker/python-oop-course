class InterviewError(Exception):
    pass

class ApplicantAlreadyRegisteredError(InterviewError):
    def __init__(self,name):
        self.name = name
        super().__init__(f"applicant already registered: {self.name}")

class ApplicantNotRegisteredError(InterviewError):
    def __init__(self,name):
        self.name = name
        super().__init__(f'applicant not registered: {self.name}')

class InvalidCategoryError(InterviewError):
    def __init__(self,category,valid_categories):
        self.category = category
        self.valid_categories = valid_categories
        super().__init__(f'invalid category {self.category}. valid categories: {self.valid_categories}')

class InterviewScorer:
    def __init__(self, max_scores):
        self.max_scores = max_scores
        self.applicants = {}

    def register_applicant(self, name):
        if name in self.applicants:
            raise ApplicantAlreadyRegisteredError(name)
        self.applicants[name] = {}

    def record_score(self, name, category, score):
            try:
                scores = self.applicants[name]
            except KeyError:
                raise ApplicantNotRegisteredError(name) from None
            
            if not category in self.max_scores:
                raise InvalidCategoryError(category, list(self.max_scores.keys()))        
            scores[category] = score

    def evaluate(self, name):
        try:
            score = self.applicants[name]
        except KeyError:
            raise ApplicantNotRegisteredError(name) from None
        
        if not score:
            return 0
        
        total_recorded = sum(self.applicants[name].values())
        total_possible = sum(self.max_scores.values())

        return int(total_recorded / total_possible * 100)


categories = {"python": 20, "sql": 15, "communication": 10, "problem_solving": 25}
scorer = InterviewScorer(categories)   # max_scores stored, applicants = {}

scorer.register_applicant("Nodira")    # applicants = {"Nodira": {}}
scorer.register_applicant("Rustam")    ## applicants = {"Nodira": {}, "Rustam": {}}

scorer.record_score("Nodira", "python", 18)   
scorer.record_score("Nodira", "sql", 12)
scorer.record_score("Nodira", "communication", 9)
scorer.record_score("Nodira", "problem_solving", 20)
#{"Nodira": {"python":18, "sql":12, "communication":9, "problem_solving":20}}
scorer.record_score("Rustam", "python", 10)
scorer.record_score("Rustam", "sql", 5)
#{"Rustam": {"python":10, "sql":5}}

print(f"Nodira: {scorer.evaluate('Nodira')}%")
#(18+12+9+20) / (20+15+10+25) * 100 -> int
print(f"Rustam: {scorer.evaluate('Rustam')}%")
#(10+5) / 70 * 100 -> int
tests = [
    lambda: scorer.register_applicant("Nodira"),
    lambda: scorer.record_score("Temur", "python", 15),  
    lambda: scorer.record_score("Rustam", "java", 10),
]

for test in tests:
    try:
        test()
    except InterviewError as e:
        print(e)


            



        

        
