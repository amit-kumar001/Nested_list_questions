#********** list understanding with inner list***********


value = ['6','66',["hii","bye",["try",'88']],[['666',"cat","dog"],"how",["final",'666','0']]]

#in this operation, element at a particular index in the nested list is replaced by another list

value[2][1]=["why",5,55]
print(value)

#in these questions , we will find the items according to index

#comment with respect to code ques_1=value[2][1][2]
#[2] index will contain another list ['hii', ['why', 5, 55], ['try', 88] from main list ...............
#and index numbering is  (hii-[0],  ['why', 5, 55]-[1],   [try,88]-[2]) for this list.....................
#so [2][1] contain =('why'-[0],   5-[1],   55-[2]) inner list  ...................
#now we can find last index value [2][1][2], so answer is = 55.

ques_1=value[2][1][2]


#comment with respect to code ques_2=value[2][2][1]
# Again [2] index value contain, another list and it's index numbering is .........
# hii-[0],     ['why', 5, 55]-[1],    [try,88]-[2]).............
# in this list we have to find another [2] index items = (try-[0],   88-[1]) from inner list...........
# last index number is [1],so in this list it will be 88.

ques_2=value[2][2][1]

#comment with respect to code ques_3=value[3][0][2]
# now we have [3] index value and it contain, another list and it's index numbering is .........
# ([666, 'cat', 'dog']-[0],      'how'-[1],        ['final', 666, 0]-[2]).............
# in this list we have to find another [0] index items, it will be =[666-[0], 'cat'-[1], 'dog'-[2]]) inner list .......
# last index number is [1], and at [1] value is dog.

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




