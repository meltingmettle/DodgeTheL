"""
Hello!

A question was recently raised on the point of higher-order functions on some source code from the Hog project, and I 
gave, in my opinion, a sub-par response, so here's a bit of clarification/explanation. 


Tried to keep it simple, but it got extremely long. XD Should still be fairly understandable. 
"""

#Off the top of my head, there are two primary types of HOFs.  (That's what it stands for)
#   1. A function which needs more information than the input allows. (Usually recursive)
#   2. A function which returns another function. 


#Example of #1

#This problem is straight from a job interview! Let's take a look!

#Let's say you have an array p and a number x and you want to find as many arrays of length x as you can in p.
#You will return an array of arrays.

#>>> x = [1,2,3,4,5,6]
#>>> function(x, 5)
#    [[1,2,3,4,5], [2,3,4,5,6]]
#>>> function(x, 3)
#    [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]

def finder_function(array, x):
  def helper_function(input_array, n, results):
       if we're done going through the array:
          return results
       else:
          increment = input_array[number:n]  #list splicing and such. tldr'd
          return helper_function(input_array, n, results + increment)
       
      #Basically, note that the helper recursivly calls itself with more function input data"" and then returns the result at the end.
      #Each call adds more and more info to the "results" input until it gets returned at the end.
return helper_function(array, x, []) #All finder function does is pass in an array and an empty list to start off. 

#Helper_function could technically be outside of finder_function, but it's cleaner to put it inside. :P 
#There's times where it does matter, but you'll see them later on. XD




#Example of #2 (same example as the dice function on Hog) (Less important, you won't see this as much in exams)

#Let's say we are part of a mortar team and we have 62mm, 80mm, 120mm, and 155mm rounds, and we have a function which will calculate trajectory and flight path to target.
#However, the calculations for each round are different, and we need custom functions for each.
#We also don't want to have to keep inputting the round size every time we change target, since we are only assigned to one gun.

#Note that 62mm and 80mm are written differently to highlight how useful these are. 
def artillery_targeting(round, wind, humidity):   #Specify the round first.  
  some_coefficient = .... #account for wind and air factors.  This doesn't change.
  def sixty_two(external_factors):
    coordinatesX = input("x-grid")    #Don't worry about input() for now.  Just assume it prompts the user for input.
    coordinatesY = input("y-grid")
    #complex calculations
    print(result_angle)
    return sixty_two(external_factors)
  
  def eighty(x,y):
    x-grid = None
    y-grid = None
    #complex calculations
    return "Fire 80mm round at settings" + str(x-grid) " , and " + str(y-grid)
   
  #PYTHON READS THIS PART FIRST.  Environment diagram, bro.
  if round == 62:
    return sixty_two(some_coefficient)  #This is a function call. 
  elif round == 80:
    return eighty  #NOTE: this returns a function.  No function call. 

# A call to 80mm would look like this:
#>>> settings = artillery_targeting(80, "30, south", 0.133)
#>>> settings(13434.290, 32204.29943)
#     450 North and 34 East
#>>> settings(132.1, 332.30)
#     450 North and 334 East

#And so on and so forth.  See the difference? A lot of time saved by the function "storing" the settings 
#and returning a fine-tuned function.

# A call to 62mm would look like this:
#>>> artillery_targeting(62, "30, south", 0.133)
#>>> x grid? : 
#>>> y grid? :
# 293 North and 23 East
#(Shell presumed to be fired)
#>>> x grid? : 
#>>> y grid? :
# 122 North and 34 East

#And so on an so forth.
    
#Same idea, just a different way of doing input. Calculations are stored, and a "pure" function which takes in only
#what you need is returned.
  
  
  
  
