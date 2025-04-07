#input nhw 
#kernel size k*k
#stride 1, padding 0
import numpy 
def convolution(kernel,data):
    #读取形状数据
    d_n, d_h, d_w = data.shape
    k,_ = kernel.shape
    #构造最终结果，边长为：h-k+1,w-k+1
    ans = []
    for n in range(0,d_n):
        tmp = numpy.ones((k,k))
        new_mat = numpy.ones(((d_h-k+1),(d_w-k+1)))
        for h in range(0,d_h-k+1):
            for w in range(0,d_w-k+1):
                for kh in range(0,k):
                    for kw in range(0,k):
                        tmp[kh,kw] = data[n,h+kh,w+kw] * kernel[kh,kw]
                new_mat[h,w] = numpy.sum(tmp)
        ans.append(new_mat)
    ans = numpy.array(ans)
    return ans 