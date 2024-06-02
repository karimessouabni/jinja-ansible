- hosts: localhost
  gather_facts: no

  vars:
    mysql_user: 'your_mysql_username'
    mysql_password: 'your_mysql_password'
    db_name: 'your_database_name'

  tasks:
    - name: Show all tables in the database
      shell: |
        mysql -u{{ mysql_user }} -p'{{ mysql_password }}' -e "SHOW TABLES FROM {{ db_name }};"
      register: show_tables

    - name: Print all tables
      debug:
        msg: "{{ show_tables.stdout_lines }}"
