from pyArango.connection import *

def top_scores(col, gpa):
   print("Top Soring Students:")
   for student in col.fetchAll():
      if student['gpa'] >= gpa:
         print("- %s" % student['name'])

conn = Connection(arangoURL='http://db:8529', username="root", password="pass")
db = conn.createDatabase(name="school")
studentsCollection = db.createCollection(name="Students")
students = [('Oscar', 'Wilde', 3.5), ('Thomas', 'Hobbes', 3.2), 
('Mark', 'Twain', 3.0), ('Kate', 'Chopin', 3.8), ('Fyodor', 'Dostoevsky', 3.1), 
('Jane', 'Austen',3.4), ('Mary', 'Wollstonecraft', 3.7), ('Percy', 'Shelley', 3.5), 
('William', 'Faulkner', 3.8), ('Charlotte', 'Bronte', 3.0)]
for (first, last, gpa) in students:
   doc = studentsCollection.createDocument()
   doc['name'] = "%s %s" % (first, last)
   doc['gpa'] = gpa 
   doc['year'] = 2017
   doc._key = ''.join([first, last]).lower() 
   doc.save()

top_scores(studentsCollection, 3.5)