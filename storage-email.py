import imaplib

mail = imaplib.IMAP4_SSL('mail.example.com')
mail.login('username@example.com', 'pass')
mail.select('INBOX')
typ, data = mail.search(None, 'ALL')
mail_ids = data[0].split()

total_size = 0
for num in mail_ids:
    typ, msg_data = mail.fetch(num, '(RFC822.SIZE)')
    size = int(msg_data[0].split()[2].strip(b')'))
    total_size += size

print(f"Total size: {total_size / (1024*1024):.2f} MB")
mail.logout()
