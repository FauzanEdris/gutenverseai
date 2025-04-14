import csv
import json

def create_gemini_1_5_jsonl_data(data):
    """Creates JSONL data in the Gemini 1.5 format."""
    jsonl_data = ""
    for item in data:
        jsonl_data += json.dumps(item, ensure_ascii=False) + "\n"
    return jsonl_data

def convert_input_output_to_gemini_format(input_output_data, system_instruction="You are a helpful assistant."):
    """Converts input/output data to the Gemini 1.5 format."""
    gemini_data = []
    for item in input_output_data:
        gemini_item = {
            "systemInstruction": {
                "role": "user",
                "parts": [{"text": system_instruction}]
            },
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": item["input"]}]
                },
                {
                    "role": "model",
                    "parts": [{"text": item["output"]}]
                }
            ]
        }
        gemini_data.append(gemini_item)
    return gemini_data

def csv_to_input_output(csv_filepath, input_column, output_column):
    """Reads a CSV file and returns a list of input/output dictionaries."""
    input_output_data = []
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    input_text = row[input_column]
                    output_text = row[output_column]

                    if input_text is None or input_text.strip() == "":
                        print(f"Warning: Missing input in row: {row}")
                        continue
                    if output_text is None or output_text.strip() == "":
                        print(f"Warning: Missing output in row: {row}")
                        continue

                    input_output_data.append({"input": input_text, "output": output_text})
                except KeyError as e:
                    print(f"Error: Column '{e}' not found in CSV. Check column names.")
                    return None  # Return None to indicate an error
        return input_output_data
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filepath}' not found.")
        return None  # Return None to indicate an error


# Example usage:
csv_file = 'data.csv'  # Replace with your CSV file path
input_col = 'input'       # Replace with your input column name
output_col = 'output'    # Replace with your output column name
system_instruction_text = "You are a specialized asistant trained to generate JSON definitions for WordPress block based on user-provided details. Your response must strictly follow the required JSON structure, adhering to the WordPress block editor standards without any tab just plain JSON."

input_output_data_from_csv = csv_to_input_output(csv_file, input_col, output_col)

if input_output_data_from_csv: # Check if csv reading was successful
    gemini_formatted_data = convert_input_output_to_gemini_format(input_output_data_from_csv, system_instruction_text)
    jsonl_output = create_gemini_1_5_jsonl_data(gemini_formatted_data)

    # Save to file
    output_file_path = "output.jsonl"
    try:
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(jsonl_output)
        print(f"JSONL data successfully written to {output_file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

else:
    print("CSV processing failed. No JSONL file created.")