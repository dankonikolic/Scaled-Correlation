

#Scaled correlation


from scipy import stats

#Consider these two arrays

x = [2,1 ,3 ,4, 5,6,7,8]
y = [2,1,13,14, 1,2,3,4]



#They are not strongly correlated
r, _ = stats.pearsonr(x, y)
print(r)



#Here is a function to compute scaled correlation between two variables

def ScaledCorrelation(a, b, scale):
    sc = scale
    SumCorr = 0
    Count   = 0
    for i in range(len(a)//sc):
        r, _ = stats.pearsonr(a[i*sc: (i+1)*sc],b[i*sc: (i+1)*sc])
        SumCorr += r
        Count += 1
    return SumCorr/Count



#At this shorter scale correlation is strong
print(ScaledCorrelation(x, y, 4))



#And when the scale is even shorter, each individual segment is perfectly correlated
#and so is thus the overall all correlation

print(ScaledCorrelation(x, y, 2))
