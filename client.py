from clientserver import DuplicationClient

dc = DuplicationClient()
print("Socket check",dc.check_if_duplicate_and_add("Test filename"))