# Sales Report Generator:
This program generates sales reports based on data from 3 CSV files:
- TeamMap.csv: A mapping of team ID's to team names
- ProductMaster.csv: A list of products and their prices
- Sales.csv: A list of sales, including the team ID, product ID, quantity sold, and discount applied (if any)

# The program generates two reports:
- TeamReport.csv: A report of total gross revenue associated with each team
- ProductReport.csv: A report of total units sold, gross revenue,and discount cost for each product

# Usage:
- To run the program, use the following command:
python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv
- Ensure you have a recent version of Python installed on your computer
- Ensure that the report.py file and all .csv files are in the same directory

# Arguments:
- -t, --team-map: The path to the team mapping CSV file. (Required)
- -p, --product-master: The path to the product master CSV file. (Required)
- -s, --sales: The path to the sales CSV file. (Required)
- --team-report: The path to the output team report CSV file. (Required)
- --product-report: The path to the output product report CSV file. (Required)

# CSV file format
- The CSV files must have the following format:

# TeamMap.csv
- The first row should contain the column headers, which must be:
- TeamId: The ID of the team.
- TeamName: The name of the team.
- Each subsequent row should contain data for a single team, with the TeamId in the first column and the TeamName in the second column.

# ProductMaster.csv
- A header is not needed in this file, however it must be formatted in this order from left to right:
- ProductId: The ID of the product.
- Name: The name of the product.
- Price: The price of the product.
- LotSize: The lot size of the product.
- Each subsequent row should contain data for a single product, with the ProductId in the first column, the Name in the second column, the Price in the third column, and the LotSize in the fourth column.

# Sales.csv
- A header is not needed in this file, however it must be formatted in this order from left to right:
- SaleId: The ID of the sale.
- ProductId: The ID of the product.
- TeamId: The ID of the team.
- Quantity: The quantity sold.
- Discount: The discount applied (if any).
