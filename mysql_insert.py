import mysql.connector
import pandas
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bestday13",
  database="reddit_health"
)

with open("sample_genome.csv") as csv_file:
  csvf = csv.reader(csv_file, delimiter=",")
  all_values = []
  for i, row in enumerate(csvf):
    if i == 0:
      continue
    val = [row[0], row[1], row[2], row[3]]
    all_values.append(val)



mycursor = mydb.cursor()

for i in range(len(all_values)):
  sql = """INSERT INTO genome
          (rsid,
            chromosome,
            position,
            genotype) 
            VALUES 
            (%s, 
            %s,
            %s,
            %s)"""

  # print(all_values[i][2])
  
  if i % 10000 == 0:
    print(i)
    
  indiv_val = (
    all_values[i][0],
    all_values[i][1],
    all_values[i][2],
    all_values[i][3]
  )
  mycursor.execute(sql, indiv_val)
  mydb.commit()

print(mycursor.rowcount, "record inserted.")