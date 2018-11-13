# Support Vector Regression SVR

* Support vector machines support linear and nonlinear regression that we can refer to as SVR.

* Instead of trying to fit the largest possible street between two classes while limiting margin violations, **SVR** tries to fit as many instances as posible on the street while limiting margin violations.

* The width of the street is controlled by a hyper parameter $\epsilon$


## SVR

SVR performs linear regression in a higher dimensional space. We can think of **SVR** as if each data point in the training represents it's own dimension. When you evaluate your kernel between a test point and a point in the training set the resulting value gives you the coordinate of your test point in that dimension.

The vector we get when we evaluate the test point for all points in the training set, $k$ is the representation of the point in the higher dimensional space.

Once you have that vector you the use it to perform a linear regression.