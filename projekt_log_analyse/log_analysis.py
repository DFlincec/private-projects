#Aufgabe 1
with open("apache_logs", "r") as file:
    apache_logs = file.readlines()
#print(apache_logs[0])
   
    
#The log is build like this: ip address, date:time, request type and resource being requested, HTTP response status code,size of the object returned to the client,HTTP referrer,information about the browser that the client is using

#Aufgabe 2
first_line = apache_logs[0].split()
#print(first_line[8])
# 200 means the operation was successful

#Aufgabe 3
status_codes = [line.split()[8] for line in apache_logs]
status_200 = status_codes.count("200")
#print(status_200)
status_404 = status_codes.count("404")
#print(status_404)

from collections import Counter
c = Counter(status_codes)
#print(c.most_common(3))

#Aufgabe 4
lines_with_404 = list(filter(lambda x : x.split()[8] == "404" , apache_logs))
resource_list = [line.split()[6] for line in lines_with_404]
#print(len(set(resource_list)))
c_l = Counter(resource_list)
#print(c_l.most_common(3))

#Aufgabe 5
from log_pdf import PDF
import seaborn as sns

sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})
status_sns = sns.histplot(data = status_codes)
status_sns.set_title("HTTP Status Codes")
status_sns.set_xlabel("Status Codes")
status_sns.figure.savefig("status_codes.png")
status_sns.figure.clf()

resource_sns = sns.histplot(y = resource_list)
resource_sns.set_title("Error Resources")
resource_sns.set_ylabel("Resources")
resource_sns.figure.savefig("resource_list.png")
resource_sns.get_figure().set_figwidth(8)
resource_sns.get_figure().set_figheight(11)
resource_sns.get_figure().savefig("resource_list.png", bbox_inches="tight")
resource_sns.figure.clf()

plots = ["status_codes.png", "resource_list.png"]
log_report= PDF()
for plot in plots:
    log_report.print_page(plot)
log_report.output("LogReport.pdf", "F")