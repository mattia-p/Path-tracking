
# Path tracking - Line following

Implementation of a line following algorithm proposed in P. I. Corke, "Robotics, Vision & Control", page 104. 


## Context

The goal is to follow a line from a random initial position and orientation. 
Both steering and speed and controlled, using two proportional controllers. 


The vehicle model used is a simple kinematic bicycle model.

![](http://latex.codecogs.com/gif.latex?%5Cgamma%20%3D%20-K_d%20d%20&plus;%20K_h%20%28%5Ctheta%5E%7B*%7D-%5Ctheta%29%20%5C%5C%20%5Ctheta%5E%7B*%7D%20%3D%20tan%5E%7B-1%7D%28%5Cfrac%7B-a%7D%7Bb%7D%29%20d)


## Some results

![](images/traj.png)  ![](images/d_theta.png)

![](images/random.png)

## Usage

```python
cd path_tracking/
python main_line_following.py
```

The ```main_line_following.py``` script is where you can modify the tests launched.



## References
1. P. I. Corke, "Robotics, Vision & Control", Springer 2017, ISBN 978-3-319-54413-7

