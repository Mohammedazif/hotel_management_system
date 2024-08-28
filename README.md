# Hotel Management System

This project is a simple Hotel Management System built using Python and MySQL. The system allows you to manage hotel room bookings, customer information, and room availability.

## Features
- **Room Management**: Add, update, and delete room information.
- **Customer Management**: Manage customer check-ins, check-outs, and booking details.
- **Database Integration**: Uses MySQL to store room and customer data.
- **GUI**: A simple graphical user interface using Tkinter.

## Installation

### Prerequisites
- Python 3.x
- MySQL server

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohammedazif/hotel_management_system.git
   cd hotel_management_system
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup the MySQL database:**
   - Ensure your MySQL server is running.
   - Update the `username` and `password` in `setup.py` to match your MySQL credentials.
   - Run the `setup.py` script to create the database and tables:
     ```bash
     python setup.py
     ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. Use the GUI to manage room bookings, customer details, and room availability.
3. The `Room Management` section allows you to add, update, and delete room information.
4. The `Customer Management` section allows you to manage check-ins, check-outs, and view booking details.

## Project Structure

- `main.py`: The main script to run the application.
- `setup.py`: The setup script for initializing the MySQL database and tables.
- `logo.ico`: The icon file for the application's GUI.
- `requirements.txt`: A file listing all the Python dependencies required to run the project.
