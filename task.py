

class CrimeLister():

    crime_records = []
    crime_counter = dict()

    def __init__(self, filename):
        self.filename = filename

    def populate_record(self):
        with open(self.filename) as f:
            lines = f.readlines()
            for line in lines:
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


    def print_crime_records(self):
        print("CRIME TYPE".ljust(30) + "CRIME ID".ljust(10) + "CRIME COUNT".ljust(10)) ## HEADER PRINT
        print("-"*50)
        for record in self.crime_records:
            print(str(record[0]).ljust(30) + str(record[1]).ljust(10) + str(record[2]).ljust(10))

def main():
    filepath = "./Crime.csv"
    crime_lister = CrimeLister(filepath)
    crime_lister.populate_record()
    crime_lister.print_crime_records()

if __name__ == '__main__':
    main()

