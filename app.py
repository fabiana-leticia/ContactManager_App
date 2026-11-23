# app.py
from flask import Flask, render_template, request, redirect, url_for
from contact_manager import ContactManager
from faker import Faker

app = Flask(__name__)
manager = ContactManager()


def load_sample_contacts(manager, count=100):
    """Generate fake contacts using Faker and add them to the manager"""
    fake = Faker()
    added = 0
    for _ in range(count):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        if manager.add_contact(name, phone, email):
            added += 1
    print(f"✅ Loaded {added} sample contacts")


# loads 100 sample contacts when the app starts
load_sample_contacts(manager, 100)


@app.route('/')
def index():
    """Show all contacts on the main page"""
    contacts = manager.list_all_contacts()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add():
    """Handle adding a new contact from the form"""
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()

    if name and phone and email:
        success = manager.add_contact(name, phone, email)
        if success:
            message = f"✅ Contact '{name}' added successfully!"
        else:
            message = f"❌ Error: Contact '{name}' already exists."
    else:
        message = "⚠️ Please fill in all fields."

    return redirect(url_for('index', msg=message))


@app.route('/search')
def search():
    """search contacts by name, partial matches allowed"""
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('index'))

    all_contacts = manager.list_all_contacts()
    results = [c for c in all_contacts if query.lower() in c.name.lower()]

    return render_template('index.html', contacts=results, search_query=query)


@app.route('/delete/<name>')
def delete(name):
    """Delete a contact by name"""
    manager.delete_contact(name)
    return redirect(url_for('index', msg=f"✅ Contact '{name}' deleted."))


if __name__ == '__main__':
    app.run(debug=True)
    