class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.total = 0.0
    
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.total += amount   

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": amount*-1, "description": description})
      self.total -= amount
      return True
    else:
      return False   

  def get_balance(self):
    return self.total
    
  def transfer(self, amount, category_object):
    transfer_withdraw = "Transfer to " + category_object.name
    transfer_deposit = "Transfer from " + self.name
    if self.check_funds(amount) == True:
      self.withdraw(amount,transfer_withdraw)
      category_object.deposit(amount, transfer_deposit)
      return True
    else:
      return False
      
  def check_funds(self, amount):
    if amount > self.total:
      return False
    else:
      return True
      
  def __repr__(self):
    category_name = self.name.center(30,"*")
    category_ledger = ""
    for item in self.ledger:
      ledger_description = item["description"][:23]
      format_amount = "{:.2f}".format(item["amount"])
      ledger_amount = str(format_amount[:7]).rjust(30-len(ledger_description))
      category_ledger += ledger_description + ledger_amount + "\n" 
    category_total = ("Total: "+ str(self.total))
    everything = ""
    everything += category_name+"\n"+category_ledger+category_total
    return everything

  
def create_spend_chart(categories):
  all_category_spent = []
  total_spent = 0.0
  for category in categories:
    category_spent = 0.0
    for item in category.ledger:
      if item["amount"] < 0:
        total_spent = total_spent + abs(item["amount"])
        category_spent = category_spent +abs(item["amount"])
        category_spent_formatted = "{:.2f}".format(category_spent)
    all_category_spent.append(float(category_spent_formatted))
  percent_spent = []
  for item in all_category_spent:
    formatted_percent = "{:.2f}".format((item/total_spent)*100)
    percent_spent.append(float(formatted_percent))

  percent_tenths = []
  for percent in percent_spent:
    if percent < 10.0:
      percent_tenths.append(0)
    else:
      string_percent = str(percent)
      tenths = int(string_percent[0])*10
      percent_tenths.append(tenths)
  
  #appending printing list with each percentage and o if <= percent in percent_tenths  
  all_number_list = ["100"," 90"," 80"," 70"," 60"," 50"," 40"," 30"," 20"," 10","  0"]
  printing_list = ["Percentage spent by category"]
  for number in all_number_list:
    print_num = str("{}|"+" "*(3*len(categories)+1)).format(number)
    list_num = []
    for i in print_num:
      list_num.append(i)
    index = 5
    for i in percent_tenths:
      if i >= int(number):
        list_num[index] = "o"
        index += 3
      else:
        list_num[index] = " "
        index += 3
    printing_list.append("".join(list_num))

  lines = [" "]*(3*len(categories)+5)
  for i in range(len(lines)):
    if i >= 4:
      lines[i] = "-"
  printing_list.append("".join(lines))

  max_length = 0
  for item in categories:
    max_length = max(max_length,len(str(item.name)))
  
  for i in range(max_length):
    index2 = 5
    name_spaces = [" "]*(3*len(categories)+5)
    for item in categories:
      name = item.name
      if i < len(name):
        name_spaces[index2] = name[i]
        index2 += 3
      else:
        name_spaces[index2] = " "
        index2 += 3
    printing_list.append("".join(name_spaces))

  return "\n".join(printing_list)

