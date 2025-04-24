from sklearn.datasets import load_diabetes
x,y = load_diabetes(return_X_y=True , as_frame=True)
x.head() 
print (x.shape)