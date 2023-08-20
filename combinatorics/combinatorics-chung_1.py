# Exercises from "Elementary Probability Theory: 
# With Stochastic Processes and an Introduction to Mathematical Finance", 
# K.L. Chung, Farid AitSahlia

# Importing basic math functions
# Make sure math_functions.py is in the same folder 

from math_functions import *

print("# ================================================================")
print("") 
print("Solution for ex. 1")
print("3 waistcoats and 2 suit jackets, possible variants of choice:")
print("")

res1_1 = a_or_b(3, 2)
res1_2 = a_or_b(res1_1, a_and_b(3,2))

print("for wearing only one of them: {}".format(res1_1)) # 3 + 2 = 5
print("for wearing both of them: {}".format(res1_2)) # 3 + 2 + (3 x 2) = 11
print("")
print("") 

print("# ================================================================")
print("") 
print("Solution for ex. 2")
print("You can buy 3 types of shirts.")
res2_1 = get_power(3, 2)
print("Count variants: 2 men buying each option once: {}".format(res2_1)) # 3^2 = 9
print("")
print("") 

print("# ================================================================")
print("") 
print("Solution for ex. 4")
print("Menu options, you can choose one option from each category: thus, 3, 4, 3, 2, 3 options.")
print("Assume there are 3 types of ice-cream and 2 types of pies (4th category, 2 becomes 5).")

original_menu_options = [3, 4, 3, 2, 3]
new_menu_options = [3, 4, 3, 5, 3]
res4_1 = multiply_list(new_menu_options)

print("Count all options for this new set menu: {}".format(res4_1)) # 3 x 4 x 3 x 5 x 3 = 540
print("")

omit_veggies_option = a_or_b(3, 1)
omit_dessert_option = a_or_b(2, 1)
original_menu_options[2] = omit_veggies_option
original_menu_options[3] = omit_dessert_option
res4_2 = multiply_list(original_menu_options)

print("Back to original menu.") 
print("Now you can omit vegetables and/or a dessert.")
print("Count all options for this set menu: {}".format(res4_2)) # 3 x 4 x (3 + 1) x (2 + 1) x 3 = 432
print("")
print("") 

print("# ================================================================")
print("") 
print("Solution for ex. 5")
res5_1 = a_or_b(get_power(26, 2), get_power(26, 3))
print("Calculate all possible variants for initials") 
print("with groups of 2 or 3 letters (for Latin alphabet): {}".format(res5_1)) # 18252.0
print("")

population = 1000000
res5_2 = get_power(population, 1/3)

print("Given an abstract language, 1,000,000 people can have initials with groups of 3 letters.")
print("What`s the number of letters? {}".format(round(res5_2))) #100
print("")
print("") 


print("# ================================================================")
print("") 
print("Solution for ex. 6")
print("Count all integers in range (1 million, 10 millions)")
print("without similar adjustent numbers using decimal notation.") 

res6_1 = get_power(9, 7)  # 0..9 in each position, 7 positions
print("")
print("Result: {}".format(res6_1)) # 4782969.0
print("")
print("") 


print("# ================================================================")
print("") 
print("Solution for ex. 8")

res8_1 = get_factorial(4)
print("How can 4 boys and 4 girls be divided into pairs? {}".format(res8_1)) # 24
print("") 

res8_2 = "2 * " + str(res8_1) + " " + str(res8_1)
res8_2 = 2 * res8_1 * res8_1  # of order is important
print("How can they be aligned, alternating by gender: {}".format(res8_2)) # 1152
print("")
print("") 

print("# ================================================================")
print("") 
print("Solution for ex. 12")
print("Condition: The door has 2 locks. You had 2 required keys and 4 others in your pocket.") 
print("But you`ve lost one of your keys. Can you still open the door? What`s the probability?") 
print("")

res12_1 = get_simple_probability(4, 6) 
print("Solution: one key was lost. 5 keys left. One of them is the right one. 4 keys in question.") 
print("The probability: {}".format(res12_1)) # 2/3
print("")

res12_2 = get_simple_probability(get_factorial(4), get_factorial(6)) 
print("What`s the probability of the first 2 keys being enough?:")
print("Result: {}".format(res12_2)) # 4!/6! = 0.003
print("")
print("") 
