import numpy as np


def prepare_laplacian(A: np.matrix) -> np.matrix:
    """Given an adjacency matrix, computes the laplacian matrix"""
    return A - np.diag(A.sum(axis=0))


def get_features(L: np.matrix, k: int) -> np.matrix:
    """Given a Laplacian matrix, return the feature vector based on eigenvalues"""
    eigval, eigvect = np.linalg.eig(L)
    k_largest_eigvals_indices = np.argsort(-np.real(eigval))[:k]
    return eigvect[:, k_largest_eigvals_indices]
