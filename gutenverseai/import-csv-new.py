import csv
import json

def create_gemini_content_entry(role, text):
    """Creates a single content entry for Gemini."""
    return {"role": role, "parts": [{"text": text}]}

def csv_to_gemini_single_json(csv_filepath, output_filepath, system_instruction="You are a helpful assistant."):
    """Converts a CSV to a SINGLE Gemini JSON object."""
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csvfile, \
                open(output_filepath, "w", encoding="utf-8") as outfile:

            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            contents = []

            for row in reader:
                input_text = row.get("input", "")
                output_text = row.get("output", "")

                if input_text.strip():
                    contents.append(create_gemini_content_entry("user", input_text))
                if output_text.strip():
                    contents.append(create_gemini_content_entry("model", output_text))

                for fieldname in fieldnames:
                    if fieldname not in ["input", "output"]:
                        text = row.get(fieldname, "")
                        if text.strip():
                            role = "user" if "user" in fieldname.lower() else "model"
                            contents.append(create_gemini_content_entry(role, text))

            gemini_json = {
                "systemInstruction": {
                    "role": "system",
                    "parts": [{"text": system_instruction}]
                },
                "contents": contents
            }

            json.dump(gemini_json, outfile, ensure_ascii=False, indent=2)
            print(f"Single JSON data successfully written to {output_filepath}")
            return True

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filepath}' not found.")
        return False
    except ValueError as e:
        print(f"ValueError: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def csv_to_gemini_jsonl(csv_filepath, output_filepath, system_instruction="You are a helpful assistant."):
    """Converts a CSV to a Gemini formatted JSONL file (multi-turn conversations per line)."""
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csvfile, \
                open(output_filepath, "w", encoding="utf-8") as outfile:

            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames

            if "input" not in fieldnames or "output" not in fieldnames:
                raise ValueError("CSV must contain 'input' and 'output' columns.")

            for row in reader:
                contents = []
                input_text = row.get("input", "")
                output_text = row.get("output", "")

                if input_text.strip():
                    contents.append(create_gemini_content_entry("user", input_text))
                if output_text.strip():
                    contents.append(create_gemini_content_entry("model", output_text))

                for fieldname in fieldnames:
                    if fieldname not in ["input", "output"]:
                        text = row.get(fieldname, "")
                        if text.strip():
                            role = "user" if "user" in fieldname.lower() else "model"
                            contents.append(create_gemini_content_entry(role, text))

                gemini_item = {
                    "systemInstruction": {
                        "role": "system",
                        "parts": [{"text": system_instruction}]
                    },
                    "contents": contents
                }

                outfile.write(json.dumps(gemini_item, ensure_ascii=False) + "\n")

        print(f"JSONL data successfully written to {output_filepath}")
        return True

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filepath}' not found.")
        return False
    except ValueError as e:
        print(f"ValueError: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage:
csv_file = 'data.csv'
system_instruction_text = "You are a specialized assistant trained to generate JSON definitions for WordPress block based on user-provided details. Your response must strictly follow the required JSON structure, adhering to the WordPress block editor standards without any tab just plain JSON."

# Create a single JSON object (for testing a conversation)
single_json_output_file = "output.json" #Use .json for single json
success_single = csv_to_gemini_single_json(csv_file, single_json_output_file, system_instruction_text)
if success_single:
    print("Single JSON conversion complete")
else:
    print("Single JSON conversion has some errors")

# Create a JSONL file (for fine-tuning)
jsonl_output_file = "output.jsonl" #Use .jsonl for jsonl
success_jsonl = csv_to_gemini_jsonl(csv_file, jsonl_output_file, system_instruction_text)

if success_jsonl:
    print("JSONL conversion complete")
else:
    print("JSONL conversion has some errors")