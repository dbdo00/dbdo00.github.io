from pyDatalog import pyDatalog 

pyDatalog.create_terms('X, Y, Z, N, M')

print(X==1)

# give me all X, Y and Z so that X and Y are in 0..4, Z is their sum, and Z is below 3
print(X.in_(range(3)) &
           Y.in_(range(5)) &
               (Z==X+Y) &
               (Z<3))