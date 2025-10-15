import numpy as np 

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6]) 

print("Add:", np.add(a, b)) 
print("All non-zero (a):", np.all(a)) 
print("Greater (b > a):", np.greater(b, a)) 
print("Greater equal (b >= a):", np.greater_equal(b, a)) 
print("Less (a < b):", np.less(a, b)) 
print("Less equal (a <= b):", np.less_equal(a, b)) 
print("Equal (a == b):", np.equal(a, b)) 
print("All close (a vs [1,2,3]):", np.allclose(a, [1, 2, 3])) 
print("Zeros:", np.zeros(3)) 
print("Ones:", np.ones(3)) 
print("Linspace (0 to 1, 5 points):", np.linspace(0, 1, 5)) 
print("Convert a to list:", a.tolist())
