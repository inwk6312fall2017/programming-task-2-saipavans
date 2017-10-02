class CrimeLister():

    crime_records = []

    def __init__(self, filename):
        self.fin = open(filename)

    def populate_record(self):
        for line in self.fin:
            if line.find("DATE") == -1: ## NOT THE HEADER

