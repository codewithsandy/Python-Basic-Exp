import re
str ='''
2
'''
str = '''

Resume
SANDESH DADASO POL
Phone: +91-9730726208 E-mail: sandeshpol123@gmail.com
Career Objective:
 To be a part of an enthusiastic work environment, where I can enhance my knowledge and apply my technical skills to accomplish organizational goals
Professional Skills:
 Good communication skills
 Quick learner
 Digital Innovative
 Good in Teamwork
Technical Skills:
 Programming Languages: C, C++, Java , ASP.NET, C#, Android
 Technologies : Firebase
 Database: MSSQL Server, Oracle
 IDE : Visual Studio, Android Studio
 Currently learning Python(Machine Learning) and Data Visualization Techniques
Academic Background:
Qualification
Passing Year
Institution
Marks in %
B.E.
(Computer Science)
2020-21 (Pursuing)
SMSMP Institute of Technology & Research, Akluj
79.52%
Diploma
(Computer Science)
2015-16
Shriram Institute of Engineering & Technology, Paniv
60.13%
SSC
2010-11
SMV, Akluj
(Pune Divisional Board)
70%
Projects Undertaken:
 E-Commerce - Android
An android app that recommended e-commerce solution built in Java using Firebase.
SMSMP@gmail.com
 Hotel Management Systa Asp.Net
Designing a web solution to reduce human efforts using asp.net and MS SQL database.
 Vehicle Transportation Monitoring – vb.net
Built a monitoring system when vehicle interacted with transport system using VB.NET
Extra-Curricular Activities:
 Participated and won prizes in various IT fests
 Participated in cultural event
 Candidate of NSS(National Social Service)
 Published research paper on E-Commerce
 Organize Technical workshops
Hobbies:
 Internet Surfing
 Managing Events
 Cycling
Personal Profile:
Date of Birth : 12-August-1994
Gender : Male
Marital Status : Single
Languages : English, Hindi, Marathi
Alternative no. : +91 8669067004
Address : Akluj, Solapur, Maharashtra (413101)
Nationality : India
Declaration: I hereby declare that all above information is true and correct to the best of my
knowledge.
Mr. Sandesh Dadaso Pol
sandy@gmail.com

'''

# email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][0-9a-zA-Z]+", str)
email = re.findall(r'\w+@\S+\w', str)
print(email)