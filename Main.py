import csv
import whois

def defang(domain):
    return domain.replace("[.]", ".").replace("hxxp", "http")

def whois_check(domain):
    try:
        w=whois.whois(domain)
        return  w.creation_date, w.registrar
    except Exception as e:
        return "N/A", "N/A"

def process_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Domain', 'Creation Date', 'Registrar'])

        next(reader, None) #Skip the header
        for row in reader:
            domain = defang(row[0]0)
            creation_date, registrar = whois_check(domain)
            writer.writerow([domain, creation_date, registrar])

if __name__ == "__main__":
    input_csv = 'test_domains.csv'
    output_csv = 'whois_output.csv'
    process_csv(input_csv, output_csv)