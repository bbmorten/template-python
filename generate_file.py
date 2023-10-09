import csv

# The template
template = """
interface Ethernet0/0
 ip address {ip_address} {subnet_mask}
"""

def generate_config_from_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        # Assuming the CSV has a header, skip it
        next(reader)

        # Loop through rows and generate config
        for row in reader:
            ip_address, subnet_mask = row
            config = template.format(ip_address=ip_address, subnet_mask=subnet_mask)
            
            # Create a filename from the IP address
            file_name = "h_" + ip_address.replace('.', '_') + ".txt"
            
            # Write the configuration to the file
            with open(file_name, 'w') as output_file:
                output_file.write(config)

# Sample usage
generate_config_from_csv('addresses.csv')
