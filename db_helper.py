import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger
import os
from dotenv import load_dotenv

# This line loads the variables from your .env file
load_dotenv()

logger = setup_logger("db_helper_logger", log_file="db_helper_server.log")

@contextmanager
def get_db_cursor(commit=False, dict_cursor=True):
    connection = None
    cursor = None
    try:
        db_password = os.getenv("DB_PASSWORD")
        if not db_password:
            raise ValueError("Database password not found. Please set DB_PASSWORD in your .env file.")

        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=db_password,
            database=os.getenv("DB_NAME", "expense_manager")
        )

        cursor = connection.cursor(dictionary=dict_cursor)
        yield cursor

        if commit:
            connection.commit()

    except mysql.connector.Error as e:
        logger.error(f"Database error: {e}")
        if connection and connection.is_connected():
            connection.rollback()
        raise
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
    return f"Expenses Deleted for {expense_date}."

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense was called with date: {expense_date}, amount: {amount}, category: {category}, note: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))
        return cursor.lastrowid

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary was called with start date: {start_date} and end date: {end_date} ")
    with get_db_cursor() as cursor:
        cursor.execute('''
                       SELECT category, SUM(amount) as total
                        FROM expense_manager.expenses
                        WHERE expense_date BETWEEN %s and %s
                        GROUP by category
                       ''', (start_date, end_date,))
        expenses = cursor.fetchall()
        return expenses

def fetch_analytics_by_month():
    logger.info(f"fetch_analytcis_by_month was called.")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month,
                        SUM(amount) AS total_expenses FROM expense_manager.expenses
                        GROUP BY month ORDER BY month
                       ''')
        expenses = cursor.fetchall()
        return expenses