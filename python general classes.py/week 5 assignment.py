

from collections import Counter
list_of_max = []
 
def most_frequent(list_of_num, k):
    count = Counter(list_of_num)
    ans = count.most_common()
    print(ans)
    for i in range(0, k):
        list_of_max.append(ans[i][0])
        print(f"top {i+1} most frequent element is: {list_of_max}")
   
    print(f"top {i+1} most frequent element is: {list_of_max}")
  
   
k = 3
list_of_num = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 15, 140, 140, 140, 140]
(most_frequent(list_of_num, k))

# On Frequency Algorithm Mr. Desmond Nnebue gave an assignment which says, Given an integer array nums and an integer k, return 
# the k most frequent elements. in runing this program,from python, i imported collections importer counter, The counter function is a Dictionary subclass for counting
# hashable items, Sometimes called a bag or multiset, Elements are stored as dictionary keys and their counts 
# are stored as dictionary values. using the module to work on my solutions, which a list of data was
# created for sample and was called list_of_num=[10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 15, 140, 140, 140, 140]
#  as list of data assigned to it.
# Then a function was created and was named 'most_frequent' to which caries an arguments (list_of_num) and a Parameter (k),
# first we were asked to return how many times an item apears in the list so we first of all created an empty string
# that will carry the returning value that will be printed out as output. assigning diffent arguments to the veriables
#  'count' and 'ans' then print it using the veribles "list_of_max" to adding 'i+1' to enble 'k' veriable produce complete index 
# desired output as the question requires above to get the result of how many times each values return.
# to return the three most apeared value, we then introduce a loop, a for loop was introduced using a range to specify the parameters to be selected,appending
# the (ans) veriable with parameter (i), then Prints the values to a stream. 
# conclusively, added that we explain our solution which i just did and check if there is a better way of going about it.
# ofcours theres always alternative way of solving it and this can be done withuout calling a function but rather using a rabdom
# startistical method to manipulate the algorithm and produce vital resuls, note; this means can be called a short cut to what was 
# displayed in my illustrations. 
# with this few points of mine, i hope i have  been able to explain in details the sequence and algorithm used in solving the problems,
# Thanks Rechi.
