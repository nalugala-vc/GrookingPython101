import pandas as pd
def generate_emails(class_list,class_sheet):

    #creating an empty set to store already used emails
    email_set = set()
    emails_data = []

    for index, row in class_list.iterrows():

        # spliting the names
        names = row['Student Name'].split()

        email_name = ''

        # if there is more than 1 name
        if len(names) >= 2:
            email_name = names[0][0].lower() + names[-1].lower()
        else:
            email_name = names[0].lower()

        # checking and removing special charactes
        email_name = ''.join(e for e in email_name if e.isalnum())

        # checking for uniqueness
        original_email_name = email_name
        counter = 1

        while email_name in email_set:
            email_name = original_email_name + str(counter)
            counter += 1

        # add new emailname  to the set
        email_set.add(email_name)

        # create full email address
        email_address = email_name + "@gmail.com"

        # Add email address the list
        emails_data.append({email_address})


        print(f"Student Name: {row['Student Name']} - Email address: {email_address}")

     # Convert to a DataFrame and save to TSV and CSV
    class_list_out = pd.DataFrame(emails_data)

    if class_sheet == "3B":
        class_list_out.to_csv("student_emails3B.csv", index=False)

    else:
        class_list_out.to_csv("student_emails3C.csv", index=False)