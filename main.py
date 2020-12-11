class Expense:
  def __init__(self, expDesc, expAmount, expCategory):
    self.expDesc = expDesc
    self.expAmount = expAmount
    self.expCategory = expCategory
    self.next = None

  def set_next(self, newNext):
        self.next = newNext

class ExpenseList:
  def __init__(self):
      self.head = None
  def byCat():
    #A breakdown of the users spending by category
    pass
  def getAvg():
    #Display average spend per item
    pass
  def total():
    #Display total expenditure
    pass

  def addexpense(self, desc, amount, cat):
    newExpense = Expense(desc, amount, cat)
    newExpense.set_next(self.head)
    self.head = new_node

def main():
  menu = True

  while menu:
    choice = int(input("Expense System\n1. Edit mode\n2. Analysis mode\n3. Exit\n"))
    
    if choice == 1:

      edit = True

      while edit == True:
        
        choice = int(input("Edit Mode\n1. Add expense\n2. Remove expense\n3. Exit\n"))
        
        if choice == 1:
          #Add expense to linked list
          desc = input("Description of expense: ")
          amount = float(input("Enter the cost of this expense: "))
          cat = input("Enter the category this expense falls under: ")
          ExpenseList.addexpense()

        if choice == 2:
        

        if choice == 3:
          #Exit to main menu
          edit = False

    elif choice == 2:

      analysis = True
    
      while analysis == True:

        print("analysis")
        analysis = False

    elif choice == 3:

      menu = False

main()
