# import os
# import csv
# from flask import Flask, render_template

# app = Flask(__name__)

# # Function to read product attributes from CSV file
# def read_product_attributes(product_name):
#     csv_file_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
#     with open(csv_file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Name'].lower() == product_name.lower():
#                 return {
#                     'Category': row['Category'],
#                     'Name': row['Name'],
#                     'Pros': row['Pros'],
#                     'Cons': row['Cons'],
#                     'Description': row['Description'],
#                     'Price': row['Price']
#                 }
#     return None

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/<product_name>')
# def product_attributes(product_name):
#     # Reading attributes for the specified product
#     product_attributes = read_product_attributes(product_name)
    
#     if product_attributes:
#         return render_template('product.html', product=product_attributes)
#     else:
#         return "Product not found!", 404

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Function to read product attributes from CSV file
def read_product_attributes(product_name):
    with open('dataset.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'].lower() == product_name.lower():
                return {
                    'Category': row['Category'],
                    'Name': row['Name'],
                    'Description': row['Description'],
                    'Pros': row['Pros'].split(', '),  # Split into list
                    'Cons': row['Cons'].split(', '),  # Split into list
                    'Price': row['Price']
                }
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<product_name>')
def product_details(product_name):
    # Reading attributes for the specified product
    product_attributes = read_product_attributes(product_name)
    
    if product_attributes:
        return render_template('product.html', product=product_attributes)
    else:
        return "Product not found!", 404

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    product_attributes = read_product_attributes(query)
    
    if product_attributes:
        return render_template('product.html', product=product_attributes)
    else:
        return "Product not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
