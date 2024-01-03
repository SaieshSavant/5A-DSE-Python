import random
import matplotlib.pyplot as plt

def lineargradient(x,y,theta):
    m,b=theta
    predicted=m*x+b
    error=predicted-y
    grad=[2*error*x,2*error]
    return grad


def meangradient(data,theta):
    gradients=[lineargradient(x,y,theta) for x,y in data]
    return [sum(gradient[i] for gradient in gradients) / len(gradients) for  i in range(len(theta))]

def gradietdecent(data,theta,learningrate,epochs):
    plt.figure(figsize(10,5))
    
    for epoch in range(epochs):
        grad=meangradient(data,theta)
        theta=[theta[i]-learningrate*grad[i] for i in range]
        
        xvalues=[x for x,_ i data]
        yvalues=[y for _,y i data]
        plt.scatter(xvalues,yvalues,label='original data')
        linex=[min(xvalues),max(xvalues)]
        liney=[theta[0]*x+theta[1] for x i linex]
        
        plt.plot(linex,liney,color='red',label='linear regression line')
        plt.quiver(theta[0]+theta[1],-grad[0],-grad[1],angles='xy',scaleunits='xy',scale=1,color='green',width=0.01)
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Epoch {epoch+1}')
        plt.legend()
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()
    return thetaaaaaaa

def main():
    data=[(1,3),(2,5),()]
        
