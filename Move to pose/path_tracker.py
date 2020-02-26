# -*- coding: utf-8 -*-
"""
@author: mattia
"""
import math
import numpy as np



class PathTracker():
    """
    Simple path tracking algorithm implementation with speed and steering control
    """


    @staticmethod
    def next_state(X,u,dt,L):
        """
        Very simple bicycle kinematic model for vehicle.
        Arguments:
            X: State (x,y,theta)
            u: Input (v, gamma)
            dt: Time step
            L: Vehicle's length
        Output:
            X_next: Next state
        """
        x, y, theta = X[0], X[1], X[2]
        v, gamma = u[0], u[1]

        x_next = x + v * np.cos(theta) * dt
        y_next = y + v * np.sin(theta) * dt
        theta_next = theta + (v / L) * np.tan(gamma) * dt

        X_next = [x_next, y_next, theta_next]
        return X_next


    @staticmethod
    def distance(X1, X2):
        """
        Arguments:
            X1: (x1, y1, theta1)
            X2: (x2, y2, theta2)
        Output:
            Euclidean distance between the two points
        """
        return np.sqrt((X1[0] - X2[0])**2 + (X1[1] - X2[1])**2)


    def move2pose(self, X_0, X_goal, params):
        """
        Arguments:
            X_0: (x_0, y_0, theta_0)
            X_goal: (x_goal, y_goal, theta_goal)
            params: [dt, L, Kv, Kh, dist_min]
                dt: Time step
                L: Vehicle's length
                Kv: Gain speed controller
                Kh: Gain steering controller
                dist_min: We need to get closer than this to the goal point
        Output:
            traj_x: List of all x
            traj_y: List of all y
            traj_theta: List of all theta

        """
        dt, L, Kv, Kh, dist_min = params[0], params[1], params[2], params[3], params[4]

        x_0, y_0, theta_0 = X_0[0], X_0[1], X_0[2]
        x_goal, y_goal = X_goal[0], X_goal[1]

        list_X = [X_0]

        dist = np.sqrt((x_goal - x_0)**2 + (y_goal - y_0)**2)

        while dist > dist_min:
            X = list_X[-1]
            x, y, theta = X[0], X[1], X[2]

            # speed
            v = Kv * PathTracker.distance(X, X_goal)

            # steering wheel angle
            theta_s = math.atan2(y_goal - y, x_goal - x)
            gamma = Kh * (theta_s - theta)
            gamma = (gamma + np.pi) % (2 * np.pi ) - np.pi

            u = [v, gamma]
            X_next = PathTracker.next_state(X,u,dt,L)

            list_X.append(X_next)
            dist = PathTracker.distance(list_X[-1], X_goal)

        traj_x = [X[0] for X in list_X]
        traj_y = [X[1] for X in list_X]
        traj_theta = [X[2] for X in list_X]

        return traj_x, traj_y, traj_theta
