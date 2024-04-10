import subprocess
import json
import csv

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        data = output.decode('utf-8')
        beta = json.dumps({"output": data.strip()})
        return beta
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    filename = "numbers.txt"  # Change this to the path of your text file containing phone numbers
    
    with open(filename, 'r') as file:
        phone_numbers = file.readlines()
    
    with open('truecaller_data.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'e164Format']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for number in phone_numbers:
            number = number.strip()  # Remove any leading/trailing whitespace or newline characters
            command = f"truecallerjs -s {number}"
            print(f"Executing command: {command}")
            deta = execute_command(command)
            parsed_data = json.loads(deta)
            output = parsed_data['output']
            formatted_output = {}
            for line in output.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    formatted_output[key.strip()] = value.strip()
            parsed_data['output'] = formatted_output
            formatted_json_data = json.dumps(parsed_data, indent=4)
            jetha = formatted_json_data
            
            if jetha:
                parsed_output = json.loads(jetha)
                name = parsed_output['output'].get("name", "")
                e164Format = parsed_output['output'].get("e164Format", "")
                writer.writerow({'name': name, 'e164Format': e164Format})


        
if __name__ == "__main__":
    main()
