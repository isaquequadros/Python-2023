import  win32com.client as win32

outlook = win32.Dispatch('outlook.application')

cash = 1000
products = 100
media = cash / products

email = outlook.CreateItem(0)

email.To = "example@gmail.com; pyexample@gmail.com"
email.Subject = "auto E-mail with Python"
email.HTMLBody = f"""
<p>hello user</p>
<p>the store's revenue was USD{cash}</p>
<p>we sell {products} products</p>
<p>the average was USD{media}</p>

<p>Thank You</p>
<p>Kadima</p>
"""

# annex = "C://Users/user/Downloads/arquivo.xlsx" 
# email.Attachments.Add(annex)

email.send()
print("Email successfully sent")