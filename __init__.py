from rhg import *

if __name__ == "__main__":
    client = RHGClient("team_11", "wz2mrzmc")
    questions = client.get_question_status()
    print questions
    info = PayloadInfo()
    a = Payload()
    a.set_crash("zx1c32zx1c32")
    b = Payload()
    b.set_crash("asdasdasdasd")
    info.add_payload(80, a)
    info.add_payload(81, b)
    print client.submit_payload(info)