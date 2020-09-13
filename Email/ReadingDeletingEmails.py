import imaplib
import datetime
import time


def read_email_from_aol():
    mail = imaplib.IMAP4_SSL('imap.aol.com')
    print("Connecting to AOL...")
    mail.login('nesteck01@aol.com', '1n2e3s')
    print("Logged In!")
    mail.list()
    mail.select('Inbox')
    print("Checking Inbox...")

    before_today = (datetime.date.today() - datetime.timedelta(30)).strftime("%d-%b-%Y")
    typ, data = mail.search(None, '(BEFORE {0})'.format(before_today))

    if data != [b'']:
        print(data)
        no_of_msgs = data[0].split()[-1]
        print("Needs to be read:\t", no_of_msgs, "messages found with date before", before_today)
        mail.store("1:{0}".format(no_of_msgs), '+Flags', '\\Seen')
        print("Seen {0} messages. Disconnecting and logging out...".format(no_of_msgs))
    else:
        print("Nothing to read. Disconnecting and logging out...")

    mail.close()
    mail.logout()


def delete_email_from_aol():
    mail = imaplib.IMAP4_SSL('imap.aol.com')
    print("Connecting to AOL...")
    mail.login('nesteck01@aol.com', '1n2e3s')
    print("Logged In!")
    mail.list()
    mail.select('Inbox')
    print("Checking Inbox...")

    before_today = (datetime.date.today() - datetime.timedelta(60)).strftime("%d-%b-%Y")
    typ, data = mail.search(None, '(BEFORE {0})'.format(before_today))

    if data != [b'']:
        print(data)
        no_of_msgs = data[0].split()[-1]
        print("To be removed:\t", no_of_msgs, "messages found with date before", before_today)
        mail.store("1:{0}".format(no_of_msgs), '+Flags', '\\Deleted')
        print("Deleted {0} messages. Let me check Trash real quick...".format(no_of_msgs))
    else:
        print("Nothing to remove. Let me check Trash real quick...")

    mail.select('Trash')
    print("Checking Trash...")
    if data != [b'']:
        mail.store("1:*", '+Flags', '\\Deleted')
        print("Cleaning...")
        mail.expunge()
        print("Done cleaning! Disconnecting and logging out...")
    else:
        print("Nothing to remove. Disconnecting and logging out...")

    mail.close()
    mail.logout()


print("Reading Emails First")
read_email_from_aol()
time.sleep(2)
print()
print("Now Deleting Emails")
delete_email_from_aol()