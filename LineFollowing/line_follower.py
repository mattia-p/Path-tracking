# -*- coding: utf-8 -*-
"""
@author: mattia
"""
import math
import numpy as np
import matplotlib.pyplot as plt

class LineFollower():
    """
    Simple line following algorithm implementation. Steering control only
    """

    @staticmethod
    def next_state(X,u,dt,L,gamma_max):
        """
        Very simple bicycle kinematic model for vehicle.
        Arguments:
            X: State (x,y,theta)
            u: Input (v, gamma)
            dt: Time step
            L: Vehicle's length
            gamma_max: Maximum steering angle
        Output:
            X_next: Next state
        """
        x, y, theta = X[0], X[1], X[2]
        v, gamma = u[0], u[1]

        if gamma > gamma_max:
            gamma = gamma_max
        if gamma < -gamma_max:
            gamma = -gamma_max

        x_next = x + v * np.cos(theta) * dt
        y_next = y + v * np.sin(theta) * dt
        theta_next = theta + (v / L) * np.tan(gamma) * dt

        X_next = [x_next, y_next, theta_next]
        return X_next


    @staticmethod
    def distance2line(X, line):
        """
        Arguments:
            X: [x1, y1, theta1]
            line: [a, b, c] # Line equation ax + by + c = 0
        Output:
            dist: Normal distance to line from point
        """
        a, b, c = line[0], line[1], line[2]
        x, y = X[0], X[1]

        dist = (a*x + b*y + c) / np.sqrt( (a**2 + b**2 ) )

        return dist


    def move2pose(self, X_0, line, params):
        """
        Arguments:
            X_0: (x_0, y_0, theta_0)
            line: [a, b, c] # Line equation ax + by + c = 0
            params: [dt, L, Kv, Kh, dist_min, gamma_max]
                dt: Time step
                L: Vehicle's length
                Kv: Gain speed controller
                Kh: Gain steering controller
                dist_min: We need to get closer than this to the goal point (Not used here)
                gamma_max: Maximum steering angle
        Output:
            traj_x: List of all x
            traj_y: List of all y
            traj_theta: List of all theta

        """
        dt, L, Kd, Kh, dist_min, gamma_max = params[0], params[1], params[2], params[3], params[4], params[5]
        a, b, c = line[0], line[1], line[2]

        list_X = [X_0]

        d = LineFollower.distance2line(X_0, line)

        # list_gamma = []
        # list_gamma_raw = []
        # list_d = []
        # list_theta_s = []
        # list_alpha_h = []
        # list_alpha_d = []

        for i in range(2000):
            X = list_X[-1]
            x, y, theta = X[0], X[1], X[2]

            # Current distance from line
            d = LineFollower.distance2line(X, line)

            alpha_d =  Kd * d

            theta_s = math.atan2(-a,b)
            alpha_h = Kh * (theta_s - theta)

            # Control law
            v = 1.0 #  Constant speed
            gamma = -alpha_d + alpha_h
            gamma = (gamma + np.pi) % (2 * np.pi ) - np.pi

            # Control input
            u = [v, gamma]

            # Compute next state
            X_next = LineFollower.next_state(X,u,dt,L,gamma_max)
            list_X.append(X_next)

            # list_gamma.append(gamma)
            # list_d.append(d)
            # list_theta_s.append(theta_s)
            # list_alpha_h.append(alpha_h)
            # list_alpha_d.append(alpha_d)

            d = LineFollower.distance2line(list_X[-1], line)

        traj_x = [X[0] for X in list_X]
        traj_y = [X[1] for X in list_X]
        traj_theta = [X[2] for X in list_X]

        # fig,ax =  plt.subplots(2)
        #
        # # ax[0].plot(traj_x, traj_y, label='trajectory')
        # # ax[0].set_xlim([-5,5])
        # # ax[0].set_ylim([-10,10])
        # # ax[0].grid()
        # # ax[0].legend()
        #
        # ax[0].plot(traj_theta, linewidth=1.5, label=r'$\theta$')
        # ax[0].plot(list_theta_s, label = r'$\theta_{goal}$')
        # ax[0].set_xlabel('Iterations')
        # ax[0].set_ylabel('Angle (rad)')
        # ax[0].set_ylim([-3,1])
        # ax[0].grid()
        # ax[0].legend()
        #
        #
        #
        # ax[1].plot(list_d, linewidth=1.5, label='Distance to line')
        # ax[1].set_xlabel('Iterations')
        # ax[1].set_ylabel('Distance (m)')
        # ax[1].legend()
        # ax[1].grid()
        # plt.show()


        return traj_x, traj_y, traj_theta
