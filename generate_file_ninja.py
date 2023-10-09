import csv
from jinja2 import Environment, FileSystemLoader

def generate_config_from_csv(file_name):
    # Set up the Jinja2 environment and loader
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('config_template.j2')

    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        # Assuming the CSV has a header, skip it
        next(reader)

        # Loop through rows and generate config
        for row in reader:
            ip_address, subnet_mask, hostname = row
            config = template.render(param1=ip_address, param2=subnet_mask, hostname = hostname)
        
            # Create a filename from the IP address
            file_name = "h_" + ip_address.replace('.', '_') + ".txt"
            
            # Write the configuration to the file
            with open(file_name, 'w') as output_file:
                output_file.write(config)

# Sample usage
generate_config_from_csv('addresses.csv')
