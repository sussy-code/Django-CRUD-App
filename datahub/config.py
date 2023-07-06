"""
  Having vue list with name pointing sql dictionary or csv dictionary or ldap dictionary
  
  Having sql dictionnary with key:vue_name pointing to sql table name -> will be used in the hub.py
"""

VIEW_LIST = {
  "view_1": {
    "method": "sql",
    "table_name": "students_app_student",
    "database_url": "studentsDB.sqlite3",
    "identifier_name": "username",
  },
  "view_2": {
    "method": "sql",
    "table_name": "teachers",
    "database_url": "studentsDB.sqlite3",
    "identifier_name": "username",
  },
  "view_3":{
    "method": "csv",
    "database_url": "view1.csv",
  },
}