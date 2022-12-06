import pandas


###################################### Data reading from CSV file ########################################################
data = pandas.read_csv("corelation_input.csv")
A = data['Milk'].tolist()
B = data['Bread'].tolist()
C = data['Butter'].tolist()
##########################################################################################################################

#################################### Function to find correlation between two attributes #################################
def corelation(A,B):
    n = len(A)

    prob_A = 0
    prob_B = 0
    prob_A_B =0

    for i in range(n):
        if  A[i] and B[i]:
            prob_A_B += 1
        
        if A[i]==1:
            prob_A += 1
        
        if B[i]==1:
            prob_B += 1
        
    ans = (prob_A_B)/(prob_A*prob_B)
    #print(ans)
    return ans
##########################################################################################################################

################################### Finding correlation between attributes ###############################################
print("corelation between Milk and Bread is",corelation(A,B))
print("corelation between Milk and Butter is",corelation(A,C))
print("corelation between Bread and Butter is",corelation(B,C))
##########################################################################################################################