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
