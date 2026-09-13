# part1: create two fruit basket as sets
from array import array


basket1={"apple", "banana", "orange", "kiwi", "apple"}
basket2 ={"mango", "kiwi", "grapes", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)
# part2: add new fruit to basket1
basket1.add("orange")   
print("Basket 1 after adding orange:", basket1)
# part3: find fruits common in both baskets
common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets:", common_fruits)
#part 4:create an array of fruits counts using array module
import array as arr
fruit_counts = arr.array('i', [3,5,2,4]) 
print("Fruit counts array:", fruit_counts)
#part5:add new fruit counts to the array
fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("Fruit counts array after adding new counts:", fruit_counts)
#part 6:count how many times the number 4 appears in the array
count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears :", count_of_4)
#part 7: reverse the fruit counts array
fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)
#part 8:print the final fruit counts array
print("")
print("===== CLASS FRUIT ORGANIZER =====")
print("basket 1:", basket1)
print("basket 2:", basket2)
print("common fruits:", common_fruits)
print("Fruit counts :", fruit_counts)
print("==================================")
