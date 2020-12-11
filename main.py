class Expense:
  def __init__(self, expDesc, expAmount, expCategory):
    self.expDesc = expDesc
    self.expAmount = expAmount
    self.expCategory = expCategory
    self.next = None

  def setNext(self, newNext):
        self.next = newNext

  def getNext(self):
    return self.next

class ExpenseList:
  def __init__(self):
      self.head = None
  
  
  def byCat(self, cat):
    #A breakdown of the users spending by category
    cur = self.head
    summary = ""
    while cur:
      if (cur.expCategory == cat):
        summary += "You spent " + str(cur.expAmount) + " on " + cur.expDesc + "\n"
      cur = cur.getNext()
    return summary


  def getAvg():
    #Display average spend per item
    pass
  def total():
    #Display total expenditure
    pass

  def addExpense(self, desc, amount, cat):
    newExpense = Expense(desc, amount, cat)
    newExpense.setNext(self.head)
    self.head = newExpense

def main():
  Expenses = ExpenseList()
  menu = True

  while menu:
    choice = int(input("Expense System\n1. Edit mode\n2. Analysis mode\n3. Exit\n"))
    
    if (choice == 1):

      edit = True

      while edit == True:
        
        choice = int(input("Edit Mode\n1. Add expense\n2. Remove expense\n3. Exit\n"))
        
        if (choice == 1):
          #Add expense to linked list
          desc = input("Description of expense: ")
          amount = float(input("Enter the cost of this expense: "))
          cat = input("Enter the category this expense falls under: ")
          Expenses.addExpense(desc, amount, cat)
          print(Expenses.head.expDesc)
        if (choice == 2):
          pass

        if (choice == 3):
          #Exit to main menu
          edit = False

    elif (choice == 2):

      analysis = True
    
      while analysis == True:
        cat = input("Enter a category to summarise: ")
        print(Expenses.byCat(cat))
    elif (choice == 3):

      menu = False

main()
