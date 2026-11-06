from flask import Flask, render_template, request, redirect, url_for
from contact_manager import ContactManager

app = Flask(__name__)
manager = ContactManager()


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
        success = manager.add_contact(name, phone,email)
        if success:
            message = f"✅ Contact '{name}' added successfully!"
        else:
            message = f"❌ Error: Contact '{name}' already exists."
    else:
        message = f"⚠️ Please fill in all fields."

    return redirect(url_for('index', msg=message))


@app.route('/delete/<name>')
def delete(name):
    """delete a contact by name"""
    return redirect(url_for('index', msg=f"✅ Contact '{name}' deleted."))


if __name__ == '__main__':
    app.run(debug=True)