

def numUniqueEmails(emails):
    # have an empty set
    clean_email = set()
    # try to separate the name from the domain
    # iterate over the emails
    for email in emails:
        # split the into two parts
        name, domain = email.split('@')
        # check if the name has a +
        if '+' in name:
            name = name[:name.index('+')]

        # add the cleaned up email
        clean_email.add(email.replace('.', '') + '@' + domain)

    return len(clean_email)


list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


answer = numUniqueEmails(list)

print(f"There are {answer} emails")


