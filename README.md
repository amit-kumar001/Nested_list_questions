# Working_with_nested_lists
## Key feature of this code 
<ol>
  <li> We will play a game, to find exact item at particular index in nested list.</li>
  <li> List is a collection which is ordered and mutable. List allows duplicate items.</li>
  <li> Nested list is a list which appears as an element in another list. We have a list with multiple inner list.</li>
  <li> With the help of <strong>if-else condition</strong>, we will set the conditions for questions and corresponding answers.</li>
  </ol>
  
  
 ## Implementing ways with code
 ~~~
 value = ['6','66',["hii","bye",["try",'88']],[['666',"cat","dog"],"how",["final",'666','0']]]
 value[2][1]=["why",5,55]
 print(value)
    
 ques_1=value[2][1][2]https://www.tutorialspoint.com/sql/sql-expressions.htm
 ques_2=value[2][2][1]
 ques_3=value[3][0][2]
    
 print("According to given list we will ask some questions")

f_ques=int(input("\n 1st question [2][1][2] = "))
if f_ques==ques_1:
    print("correct answer " )
else:
    print("incorrect, answer is 55 ")


s_ques=(input("\n 2nd question [2][2][1] = "))
if s_ques==ques_2:
    print("correct answer " )
else:
    print("incorrect, answer is 88 ")

t_ques=(input("\n 3rd question [3][0][2] = "))
if t_ques==ques_3:
    print("correct answer " )
    print("\n")
    print("Thanks for playing game")

else:
    print("incorrect, answer is dog ")
    print("Thanks for playing game")
~~~

   
  
 ## How to run this file
 
  Since this is a python file, hence it can be run using following command
~~~
  python list_prog.py
  python3 list_prog.py
~~~
