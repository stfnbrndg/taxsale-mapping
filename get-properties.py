import requests
import tabula
import urllib.request
import csv
import pandas
import pathlib

url = "https://www.knoxcounty.org/trustee/taxsale23/taxsale23.pdf"

# // Scrape addresses from tax sale

# Download PDF with address list

pdf = "taxsale.pdf"
file = pathlib.Path(pdf)

if not file.exists():
    urllib.request.urlretrieve(url, pdf)

# Convert PDF to CSV

csv = "taxsale.csv"
file = pathlib.Path(csv)

if not file.exists():
    tabula.convert_into(pdf, csv, pages = "all")

# // Clean up addresses (if necessary)

# Read addresses into dataframe
df = pandas.read_csv(csv, delimiter = ',', index_col=[0])
print(df)

for col in df.columns:
    print(col)