import csv
import whois

#This defangs the domains to pass through who is
def defang(domain):
    return domain.replace("[.]", ".").replace("hxxp", "http")

#Runs the who is check against the domain for the selected values (Registrar, Creation Date)
def whois_check(domain):
    try:
        w=whois.whois(domain)
        return  w.creation_date, w.registrar
    except Exception as e:
        return "N/A", "N/A"

#This is teh function to read the input and write the output as CSV
def process_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Domain', 'Creation Date', 'Registrar'])

        next(reader, None) #Skip the header
        for row in reader:
            domain = defang(row[0])
            creation_date, registrar = whois_check(domain)
            writer.writerow([domain, creation_date, registrar])

#This is the main section that runs the script
if __name__ == "__main__":
    input_csv = 'test_domains.csv'
    output_csv = 'whois_output.csv'
    process_csv(input_csv, output_csv)