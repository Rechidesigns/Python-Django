from datetime import datetime

today = datetime.now()

w = today.isoformat()
d = {"f": datetime.fromisoformat(w)}

print(d)