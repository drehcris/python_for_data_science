'Creating a Numpy Array
import numpy as np
 arr = np.array([1, 2, 3])
print(arr)
 
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
 
arr = np.array((1, 3, 2))
print(arr)

Output
[1 2 3]
[[1 2 3]
 [4 5 6]]
[1 3 2]

------------------------------------------------------

'Accessing the Array Index
import numpy as np
 arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
​
arr2 = arr[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", arr2) 
#Pegue as 2 primeiras linhas e, nelas, selecione as colunas de 2 em 2”
 
arr3 = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", arr3)

Output
first 2 rows and alternate columns(0 and 2):
 [[-1.  0.]
 [ 4.  6.]]

Elements at indices (1, 3), (1, 2), (0, 1), (3, 0):
 [0. 6. 2. 3.]


'Basic Array Operations
import numpy as np
 a = np.array([[1, 2],
              [3, 4]])
 
b = np.array([[4, 3],
              [2, 1]])
               
print ("Adding 1 to every element:", a + 1)
print ("\nSubtracting 2 from each element:", b - 2)
print ("\nSum of all array elements: ", a.sum())
print ("\nArray sum:\n", a + b)

Output
Adding 1 to every element: [[2 3]
 [4 5]]

Subtracting 2 from each element: [[ 2  1]
 [ 0 -1]]

Sum of all array elements:  10

Array sum:
 [[5 5]
 [5 5]]

------------------------------------------------------

'Data Types in Numpy
'Constructing a Datatype Object
import numpy as np
 x = np.array([1, 2])  
print(x.dtype)         
 
x = np.array([1.0, 2.0]) 
print(x.dtype)  
 
x = np.array([1, 2], dtype = np.int64)   
print(x.dtype)

Output
int64
float64
int64

-----------------------------------------------------------

'Math Operations on DataType array
import numpy as np
 arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
​
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
Sum = np.add(arr1, arr2)
print(Sum)
​
Sum1 = np.sum(arr1)
print(Sum1)
 
Sqrt = np.sqrt(arr1)
print(Sqrt)
​
Trans_arr = arr1.T
print(Trans_arr)

Output
[[ 7. 13.]
 [ 4. 14.]]
19.0
[[2.         2.64575131]
 [1.41421356 2.44948974]]
[[4. 2.]
 [7. 6.]]

----------------------------------------------------------
