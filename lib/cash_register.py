#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.prev_total = total
    self.items = []
    
  def add_item(self, title, price, quantity = 1):
    self.quantity = quantity
    for i in range(quantity):
      self.items.append(title)
    self.prev_total = self.total
    self.total = self.total + (price * quantity)
  
  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total - (self.total * (float(self.discount) / 100.0)))
      print(f'After the discount, the total comes to ${self.total}.')
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total = self.prev_total