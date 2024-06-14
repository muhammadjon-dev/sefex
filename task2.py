from bs4 import BeautifulSoup

with open("phases_soften.html", "r") as f:
    html_content = f.read()
    
soup = BeautifulSoup(html_content, "html.parser")
titles = {2:"Deployment", 0:"Development", 3:"Monitoring", 1:"Testing"}
headers = soup.find_all("h3")
for i in range(4):
    header = headers[i]
    print(f"{header.get_text()} - {titles[i]}")
    print(header.find_next().get_text(), end="\n\n")