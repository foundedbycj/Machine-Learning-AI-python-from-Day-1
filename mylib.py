import FastML_lib.FastMl as cj

#initalize the datasets (use 2 vars only)
x = [1,2,3,4,5,6]
y=[2,4,4,5,7,8]
# linear regression  
a = cj.SimpleLinRegression(x,y)
#calculate the values
ypred= a.predict_y()
#plot up the values 
a.plotup(x,y,ypred)
