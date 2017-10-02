class CrimeLister():

    crime_records = []
    crime_counter = dict()

    def __init__(self, filename):
        self.fin = open(filename)

    def populate_record(self):
        for line in self.fin:
            if line.find("DATE") == -1: ## EXCLUDE HEADER
                line_content = line.strip()
                line_content = line_content.split(",")
                crime_type = line_content[len(line_content)-1]
                crime_id = line_content[len(line_content)-2]
                self.crime_counter[crime_type] = self.crime_counter.get(crime_type, 0) + 1
                crime_record = [crime_type, crime_id]
                self.crime_records.append(crime_record)
        for crime in self.crime_records:
            crime.append(self.crime_counter[crime[0]])



def main():
    filepath = "./Crime.csv"
    crime_lister = CrimeLister(filepath)
    crime_lister.populate_record()
    print(crime_lister.crime_records)

if __name__ == '__main__':
    main()

