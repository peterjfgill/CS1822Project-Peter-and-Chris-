class Expense:
  def __init__(self, expDesc, expAmount, expCategory):
    self.expDesc = expDesc
    self.expAmount = expAmount
    self.expCategory = expCategory

class Expenses:
  def __init__(self):
        self.Expenses = []

  def byCat():
    #A breakdown of the users spending by category
 
  def getAvg():
    #Display average spend per item

  def total():
    #Display total expenditure
   
#------------------------------------------------------------------------- Menu
def main():
  menu = True

  while menu:
    choice = int(input("1. Edit mode\n2. Analysis mode\n3. Exit\n"))
   
    if choice == 1:

      edit = True

      while edit == True:

        print("edit")
        edit = False

    if choice == 2:

      analysis = True
   
      while analysis == True:

        print("analysis")
        analysis = False

    if choice == 3:

      menu = False

