# with mail.record_messages() as outbox:

#     mail.send_message(subject='testing',body='test',recipients=emails)

#     assert len(outbox) == 1
#     assert outbox[0].subject == "testing"