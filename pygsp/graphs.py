# -*- coding: utf-8 -*-

r"""
Module documentation.
"""

from copy import deepcopy
from scipy import sparse
from scipy import io
import numpy as np


class Graph(object):

    # All the paramters that needs calculation to be set
    # or not needed are set to None
    def __init__(self, W=None, A=None, N=None, d=None, Ne=None,
                 gtype='unknown', directed=None,
                 lap_type='combinatorial', L=None, **kwargs):

        self.gtype = gtype
        self.lap_type = lap_type

        if W:
            self.W = sparse.lil_matrix(W)
        else:
            # TODO check if right
            self.W = sparse.lil_matrix(0)
        if A:
            self.A = A
        else:
            # TODO check if right
            self.A = sparse.lil_matrix(W > 0)
        if N:
            self.N = N
        else:
            # MAT: size(G.W, 1)
            # TODO implement right!
            self.N = 0
            pass
        if d:
            self.d = d
        else:
            self.d = self.W.sum()
        if Ne:
            self.Ne = Ne
        else:
            # MAT: zeros(G.N, L)
            pass
        if directed:
            self.directed = directed
        else:
            # TODO func is_directed(self)
            pass
        if L:
            self.L = L
        else:
            # TODO func create_laplacian(G)
            pass

    def copy_graph_attr(self, gtype, Gn):
        r"""
        TODO write doc
        """
        return deepcopy(self)

    def separate_graph(self):
        r"""
        TODO write func & doc
        """
        raise NotImplementedError("Not implemented yet")

    def subgraph(self, c):
        r"""
        TODO better doc
        This function create a subgraph from G, keeping only the node(s) in c
        """

        sub_G = self
        sub_G.W = [c,c]
        try:
            sub_G.N = len(c)
        except TypeError:
            sub_G.N = 1

        sub_G.gtype = "sub-" + self.gtype

        return sub_G


# Need M
class Grid2d(Graph):

    def __init__(self, M, **kwargs):
        super(Grid2d, self).__init__(**kwargs)
        if M:
            self.M = M
        else:
            self.M = self.N

        self.gtype = '2d-grid'
        self.N = self.N * self.M

        # Create weighted adjacency matrix
        K = 2 * self.N - 1
        J = 2 * self.M - 1
        i_inds = np.zeros((K*self.M + J*self.N, 1), dtype=float)
        j_inds = np.zeros((K*self.M + J*self.N, 1), dtype=float)
        for ii in xrange(1, self.M):
            i_inds[(ii-1) * K + np.arange(0, K)] = (ii - 1) * self.N + np.append(range(0, self.N - 1), range(1, self.N))
            j_inds[(ii-1) * K + np.arange(0, K)] = (ii - 1) * self.N + np.append(range(1, self.N), range(0, self.N - 1))

        for ii in xrange(1, self.M - 1):
            i_inds[(K*self.M) + (ii-1)*2*self.N + np.arange(1, 2*self.N)] = np.append((ii-1)*self.N + np.array(range(1, self.N)), (ii*self.N) + np.array(range(1, self.N)))
            j_inds[(K*self.M) + (ii-1)*2*self.N + np.arange(1, 2*self.N)] = np.append((ii*self.N) + np.array(range(1, self.N)), (ii-1)*self.N + np.array(range(1, self.N)))

        self.W = sparse.csr_matrix((np.ones((K*self.M+J*self.N, 1)), (i_inds, j_inds)), shape=(self.M*self.N, self.M*self.N))


class Torus(Graph):

    def __init__(self, M, **kwargs):
        super(Torus, self).__init__(**kwargs)
        if M:
            self.M = M
        else:
            self.M = self.N


# Need K
class Comet(Graph):

    def __init__(self, k, **kwargs):
        super(Comet, self).__init__(**kwargs)
        if k:
            self.k = k
        else:
            self.k = 12


class LowStretchTree(Graph):

    def __init__(self, k, **kwargs):
        super(LowStretchTree, self).__init__(**kwargs)
        if k:
            self.k = k
        else:
            self.k = 6


class RadomRegular(Graph):

    def __init__(self, k, **kwargs):
        super(RadomRegular, self).__init__(**kwargs)
        if k:
            self.k = k
        else:
            self.k = 6


class Ring(Graph):

    def __init__(self, k, **kwargs):
        super(Ring, self).__init__(**kwargs)
        if k:
            self.k = k
        else:
            self.k = 1


# Need params
class Community(Graph):

    def __init__(self, **kwargs):
        super(Community, self).__init__(**kwargs)
        param = kwargs


class Cube(Graph):

    def __init__(self, **kwargs):
        super(Cube, self).__init__(**kwargs)
        param = kwargs


class Sensor(Graph):

    def __init__(self, **kwargs):
        super(Sensor, self).__init__(**kwargs)
        param = kwargs


class Sphere(Graph):

    def __init__(self, **kwargs):
        super(Sphere, self).__init__(**kwargs)
        param = kwargs


# Need nothing
class Airfoil(Graph):

    def __init__(self):
        super(Airfoil, self).__init__()


class Bunny(Graph):

    def __init__(self):
        super(Bunny, self).__init__()


class DavidSensorNet(Graph):

    def __init__(self):
        super(DavidSensorNet, self).__init__()


class FullConnected(Graph):

    def __init__(self):
        super(FullConnected, self).__init__()


class Logo(Graph):

    def __init__(self):
        super(Logo, self).__init__()

        mat = io.loadmat('misc/logogsp.mat')
        self.W = mat['W']
        self.gtype = 'from MAT-file'
        # TODO implementate plot attribute


class Path(Graph):

    def __init__(self):
        super(Path, self).__init__()


class RandomRing(Graph):

    def __init__(self):
        super(RandomRing, self).__init__()


def dummy(a, b, c):
    r"""
    Short description.

    Long description.

    Parameters
    ----------
    a : int
        Description.
    b : array_like
        Description.
    c : bool
        Description.

    Returns
    -------
    d : ndarray
        Description.

    Examples
    --------
    >>> import pygsp
    >>> pygsp.module1.dummy(0, [1, 2, 3], True)
    array([1, 2, 3])

    """
    return np.array(b)
