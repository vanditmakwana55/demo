#!/usr/bin/env python3
"""
Test Snippets with Various Code Issues
Use these to test the PR Review Agent
"""

# ==========================================
# SNIPPET 1: SQL Injection Vulnerability
# ==========================================

SNIPPET_1_SQL_INJECTION = """
def get_user_by_email(email):
    # ❌ VULNERABLE: SQL Injection
    query = f"SELECT * FROM users WHERE email = '{email}'"
    user = db.execute(query)
    return user
"""

# ==========================================
# SNIPPET 2: Hardcoded Secrets
# ==========================================

SNIPPET_2_HARDCODED_SECRETS = """
# ❌ SECURITY ISSUE: Hardcoded API Key
API_KEY = "sk-1234567890abcdef"
DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"
JWT_SECRET = "super-secret-key"

def call_api():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://api.example.com/data", headers=headers)
    return response
"""

# ==========================================
# SNIPPET 3: Improper Exception Handling
# ==========================================

SNIPPET_3_EXCEPTION = """
def divide(a, b):
    try:
        return a / b
    except:
        # ❌ BAD PRACTICE: catching all exceptions
        return None
"""

# ==========================================
# SNIPPET 4: Mutable Default Argument
# ==========================================

SNIPPET_4_MUTABLE_DEFAULT = """
def add_item(item, items=[]):
    # ❌ BUG: mutable default argument
    items.append(item)
    return items
"""

# ==========================================
# SNIPPET 5: Insecure Random
# ==========================================

SNIPPET_5_RANDOM = """
import random

def generate_token():
    # ❌ NOT SECURE
    return str(random.random())
"""

# ==========================================
# SNIPPET 6: Missing Input Validation
# ==========================================

SNIPPET_6_VALIDATION = """
def process_age(age):
    # ❌ No validation
    return 100 / age
"""

# ==========================================
# SNIPPET 7: Logging Sensitive Data
# ==========================================

SNIPPET_7_LOGGING = """
def login(user, password):
    # ❌ SECURITY ISSUE
    print(f"User: {user}, Password: {password}")
"""

# ==========================================
# SNIPPET 8: Inefficient Loop
# ==========================================

SNIPPET_8_PERFORMANCE = """
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                duplicates.append(lst[i])
    return duplicates
"""

# ==========================================
# SNIPPET 9: File Handling Issue
# ==========================================

SNIPPET_9_FILE = """
def read_file():
    f = open("data.txt", "r")
    data = f.read()
    # ❌ file not closed
    return data
"""

# ==========================================
# SNIPPET 10: Command Injection
# ==========================================

SNIPPET_10_COMMAND = """
import os

def run_command(cmd):
    # ❌ DANGEROUS
    os.system("echo " + cmd)
"""

# ==========================================
# SNIPPET 11: Weak Password Check
# ==========================================

SNIPPET_11_PASSWORD = """
def is_valid(password):
    # ❌ Weak validation
    return len(password) > 3
"""

# ==========================================
# SNIPPET 12: Unused Variable
# ==========================================

SNIPPET_12_UNUSED = """
def calculate():
    x = 10
    y = 20
    z = 30  # ❌ unused
    return x + y
"""
