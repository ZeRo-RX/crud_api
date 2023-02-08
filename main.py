while True:
    host_ip = input('Welcome to setup page\n\nEnter your Host IP: ')
    database_name = input('Enter your Database Name: ')
    database_username = input('Enter your Database Username: ')
    while True:
        database_password = input('Enter your Database Password: ')
        database_password_again = input('Enter your Database Password again: ')
        if database_password == database_password_again:
            break
        else:
            print("### Passwords doesn't match! try again")

    user_ifo_correct = input("""
    Host IP: %s
    Database Name: %s
    Username: %s
    Password: %s

Confirm the database information. Need to be edited? (N/y):""" % (
        host_ip, database_name, database_username, "*" * len(database_password))
                             )
    user_ifo_correct.strip()
    if user_ifo_correct == 'N' or user_ifo_correct == 'n' or user_ifo_correct == '':
        database_credentials = "postgresql://%s:%s@%s/%s" % \
             (database_username, database_password, host_ip, database_name)
        break

with open('app/database.txt', 'w') as f:
    f.write(database_credentials)
