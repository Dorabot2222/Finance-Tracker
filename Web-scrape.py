from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Function to read data from CSV file
def read_data():
    with open('expenses.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to write data to CSV file
def write_data(data):
    with open('expenses.csv', 'w', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Home route
@app.route('/')
def home():
    expenses = read_data()
    total_expenses = sum(float(expense['amount']) for expense in expenses)
    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)

# Add expense route
@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    amount = request.form['amount']

    expenses = read_data()
    expenses.append({'date': date, 'category': category, 'amount': amount})
    write_data(expenses)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
  
