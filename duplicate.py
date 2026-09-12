#dictionary of students(id->details)
student_data = {
    "id1": {"name": "sara", "class": "5", "subject": "Math,Science,English"},
    "id2": {"name": "jay", "class": "5", "subject": "Math,Science,English"},
    "id3": {"name": "surya", "class": "5", "subject": "Math,Science,English"},
    "id4": {"name": "sara", "class": "5", "subject": "Math,Science,English"}
}
result = {}
seen_keys=[]#using a list instead of set
for student_id, details in student_data.items():
 unique_key = (details["name"], details["class"], details["subject"])
 if unique_key not in seen_keys:
    seen_keys.append(unique_key)
    result[student_id] = details
    #print output line by line
for k,v in result.items():
      print(k,":",v)
