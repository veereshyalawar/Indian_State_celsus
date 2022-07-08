import csv


class Csv_Reader:
    def reading_csv_file(self, check):
        try:
            with open('indian_state_census.csv') as file:
                reader = csv.reader(file)
                # length = len(reader)
                # print(length)
                count = 0
                for row in reader:
                    print(row)

                    if count > check:
                        break
                    count += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    csv1 = Csv_Reader()
    csv1.reading_csv_file(check=30)