import argparse
import csv

def read_team_map(file_path):
    # team_map is a dictionary that holds the data read from TeamMap.csv
    team_map = {}
    with open (file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            team_map[row[0]] = row[1]
    return team_map

def read_product_master(file_path):
    # product_master is a dictionary that holds the data read from ProductMaster.csv
    product_master = {}
    with open(file_path, 'r') as f:
        reader=csv.reader(f)
        for row in reader:
            product_master[row[0]] = {'ProductId': row[0], 'Name': row[1], 'Price': float(row[2]), 'LotSize': row[3]}
    return product_master

def read_sales(file_path):
    # sales is a dictionary that holds the data read from Sales.csv
    sales = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            sales[row[0]] = {'ProductId': row[1], 'TeamId': row[2], 'Quantity': row[3], 'Discount': float(row[4])}
    return sales

def generate_team_report(team_map, product_master, sales):
    # Create a new dictionary, this will hold team name
    # And the total gross revenue associated with each team
    team_report = {}
    for sale in sales:                        
        # team_id is a variable that holds the team id found in each row
        # team_name is set to the name of the associated team id in team_map
        team_id = sales[sale]['TeamId']
        team_name = team_map[team_id]
        # add team_id into team_report, will not add if already added
        if team_id not in team_report:
            team_report[team_id] = {'Team': team_name, 'GrossRevenue': 0.0}
        # The GrossRevenue is caluclated by checking the quantity and ProductId in the sales dictionary
        # Then multiplying the quantity by the price of the associated ProductId found in product_master 
        team_report[team_id]['GrossRevenue'] += float(sales[sale]['Quantity']) * product_master[sales[sale]['ProductId']]['Price']
    # sorts the dictionary in descending order
    sorted_team_report = sorted(team_report.items(), key=lambda x:x[1]['GrossRevenue'], reverse=True)
    return sorted_team_report

def generate_product_report(product_master, sales):
    # Create a new dictionary that holds 
    # Product name, product gross revenue, total units sold, and how much money customers saved on discounts
    product_report = {}
    for sale in sales:
        product_id = sales[sale]['ProductId']
        # add product_id in product_report, will not add if already added
        if product_id not in product_report:
            product_report[product_id] = {'Name': product_master[product_id]['Name'], 'GrossRevenue': 0.0, 'TotalUnits': 0, 'DiscountCost': 0.0}

        # initialize new variables from values stored in existing dictionaries
        quantity = int(sales[sale]['Quantity'])
        discount = sales[sale]['Discount']
        price = product_master[product_id]['Price']

        # Sum up all the values in product_report and organize them into their respective spots in the dictionary
        product_report[product_id]['TotalUnits'] += quantity
        product_report[product_id]['GrossRevenue'] += quantity * price
        product_report[product_id]['DiscountCost'] += quantity * price * (discount/100)
    # sorts the dictionary in descending order
    sorted_product_report = sorted(product_report.items(), key=lambda x:x[1]['GrossRevenue'], reverse=True)
    return sorted_product_report

def write_team_report(file_path, sorted_team_report):
    # These write the output of each sorted dictionary to a new CSV file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Team','GrossRevenue'])
        for team_id, team_data in sorted_team_report:
            writer.writerow([team_data['Team'], team_data['GrossRevenue']])

def write_product_report(file_path, sorted_product_report):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost'])
        for product_id, product_data in sorted_product_report:
            writer.writerow([
                product_data['Name'],
                product_data['GrossRevenue'],
                product_data['TotalUnits'],
                product_data['DiscountCost']
            ])



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate sales reports')
    parser.add_argument('-t', '--team-map', type=str, required=True, help='Path to team mapping CSV file')
    parser.add_argument('-p', '--product-master', type=str, required=True, help='Path to product master CSV file')
    parser.add_argument('-s', '--sales', type=str, required=True, help='Path to sales CSV file')
    parser.add_argument('--team-report', type=str, required=True, help='Path to output team report CSV file')
    parser.add_argument('--product-report', type=str, required=True, help='Path to output product report CSV file')

    args = parser.parse_args()
    file_path_team_map = args.team_map
    file_path_product_master = args.product_master
    file_path_sales = args.sales
    file_path_team_report = args.team_report
    file_path_product_report = args.product_report

    team_map = read_team_map(file_path_team_map)
    product_master = read_product_master(file_path_product_master)
    sales = read_sales(file_path_sales)

    sorted_team_report = generate_team_report(team_map, product_master, sales)
    sorted_product_report = generate_product_report(product_master, sales)

    write_team_report(file_path_team_report, sorted_team_report)
    write_product_report(file_path_product_report, sorted_product_report)