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
                crime_key = crime_type + "," + crime_id
                self.crime_counter[crime_key] = self.crime_counter.get(crime_key + "", 0) + 1
        for crime in self.crime_counter.keys():
            crime_type_id = crime.split(",")
            self.crime_records.append([crime_type_id[0],crime_type_id[1],self.crime_counter[crime]])



def main():
    filepath = "./Crime.csv"
    crime_lister = CrimeLister(filepath)
    crime_lister.populate_record()
    print(crime_lister.crime_records)

if __name__ == '__main__':
    main()

