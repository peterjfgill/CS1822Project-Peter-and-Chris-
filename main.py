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
    total = 0
    while cur != None:
      if (cur.expCategory == cat):
        total += cur.expAmount
      cur = cur.getNext()
    return "You spent " + str(total) + " on " + cat + "\n"


  def getTotalAvg(self):
    #Display average spend per item
    cur = self.head
    length = 0
    total = 0
    avg = 0
    while cur != None:
        length += 1
        total += cur.expAmount
        cur = cur.getNext()
    avg = total/length
    return "Your average spend per item was " + str(avg) + " and your total expenditure was " + str(total) + ".\n"


  def addExpense(self, desc, amount, cat):
    #Add new expense to linked list
    newExpense = Expense(desc, amount, cat)
    newExpense.setNext(self.head)
    self.head = newExpense

  def delExpense(self, data):
    cur = self.head
    previous = None
    found = False
    while (cur.getNext() != None) and (found is False):
        if (cur.expDesc == data):
            found = True
        else:
            previous = cur
            cur = cur.getNext()
    if (cur is None):
        print("No expense with this description is recorded.")
    if (previous is None):
        self.head = cur.getNext()
    else:
        previous.setNext(cur.getNext())
def main():
  ExpenseCategories = []
  Expenses = ExpenseList()
  menu = True

  while menu:
    choice = int(input("Expense System\n1. Edit mode\n2. Analysis mode\n3. Exit\n"))
    
    if (choice == 1):

      edit = True

      while edit == True:
        
        choice = int(input("Edit Mode\n1. Add expense\n2. Remove expense\n3. Exit\n"))
        
        if (choice == 1):
          #Calls addExpense with parameters given by user
          desc = input("Description of expense: ")
          amount = float(input("Enter the cost of this expense: "))
          cat = input("Enter the category this expense falls under: ")
          if(cat not in ExpenseCategories):
            ExpenseCategories.append(cat)
          Expenses.addExpense(desc, amount, cat)
        if (choice == 2):
          #calls delExpense with description of item to be deleted
          desc = input("Describe the expense you wish to remove")
          Expenses.delExpense(desc)

        if (choice == 3):
          #Exit to main menu
          edit = False

    elif (choice == 2):

      analysis = True
    
      while analysis == True:
        for cat in ExpenseCategories:
          print(Expenses.byCat(cat))
        print(Expenses.getTotalAvg())
        analysis = False
    elif (choice == 3):

      menu = False

main()
