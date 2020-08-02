water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
def coffee_result():
  print('I have enough resources, making you a coffee!')

def rem_coffee():
  print('The coffee machine has: ')
  print(water,'of water')
  print(milk,'of milk')
  print(coffee_beans,'of coffee beans')
  print(disposable_cups,'of disposable cups')
  print('$',money,'of money')

def buy_coffee():
  global water
  global milk
  global coffee_beans
  global disposable_cups
  global money
  
  if water > 0 and coffee_beans > 0 and disposable_cups > 0 and money > 0 and milk > 0:
    type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    if type == '1' and water >= 250 and coffee_beans >= 16 and disposable_cups >= 1:
      water -= 250
      coffee_beans -=  16
      disposable_cups -= 1
      money += 4
      coffee_result()
    elif type == '2' and water >= 350 and milk >= 75 and coffee_beans >= 20 and disposable_cups >= 1:
      water -= 350
      milk -= 75
      coffee_beans -= 20
      disposable_cups -= 1
      money += 7
      coffee_result()
    elif type == '3' and water >= 200 and milk >= 100 and coffee_beans >= 12 and disposable_cups >= 1:
      water -= 200
      milk -= 100
      coffee_beans -= 12
      disposable_cups -= 1
      money += 6
      coffee_result()
    elif water < 350:
      print('Sorry, not enough water!')
    elif coffee_beans < 20:
      print('Sorry, not enough coffee beans')
    elif milk < 100:
      print('Sorry, not enough milk')
    elif disposable_cups < 1:
      print('Sorry, not enough disposable cups')
    elif money < 7:
      print('Sorry, not enough money')

def fill_coffee():
  global water
  global milk
  global coffee_beans
  global disposable_cups
  global money
  add_water = input('Write how many ml of water do you want to add: ')
  water += int(add_water)
  add_milk = input('Write how many ml of milk do you want to add: ')
  milk += int(add_milk)
  add_coffee_beans = input('Write how many grams of coffee beans do you want to add: ')
  coffee_beans += int(add_coffee_beans)
  add_disposable_cups = input('Write how many disposable cups of coffee do you want to add: ')
  disposable_cups += int(add_disposable_cups)

while True:
  action = input('Write action (buy, fill, take, remaining, exit): ')
  if action == 'buy':
    buy_coffee()
  if action == 'fill':
    fill_coffee()
  if action == 'take':
    print('I gave you $',money)
    money = 0
  if action == 'remaining':
    rem_coffee()
  if action == 'exit':
    break