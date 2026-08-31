import csv

def main():
    try:
        with open("../data/messy_data.csv") as file:
            file_dict = csv.DictReader(file)
            enumerated_dict = enumerate(file_dict)
            parsed_row_count = 0
            skipped_row_count = 0
            clean_data = ""
            row_report = ""
                        
            for i, row in enumerated_dict:
                try:
                    if None in row:
                        raise KeyError(f"Row {i + 1}: extra column detected — skipped")
                    
                    data = float(row["amount"])
                    clean_data += f"{row['name']} | {row['category']} | ${data:.2f}\n"
                    parsed_row_count += 1
                    
                except ValueError as value_error:
                    row_report += f"Row {i + 1}: ValueError — {str(value_error)}\n"
                    skipped_row_count += 1
                except KeyError as key_error:
                    row_report += str(key_error) + "\n"
                    skipped_row_count += 1
                
            print(f"""
=== CSV Report ===
Rows attempted:   {skipped_row_count + parsed_row_count}
Rows parsed:      {parsed_row_count}
Rows skipped:     {skipped_row_count}

Skipped rows:
{row_report}
  
Clean data:
{clean_data}
""")            
    except FileNotFoundError as e:
        print("The file \"messy_data.csv\" was not found. Please check the file exists before running the program.")
        return
    
if __name__ == "__main__":
    main()