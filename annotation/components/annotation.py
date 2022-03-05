# coding: utf-8

from typing import List
import numpy as np
from scipy.signal import argrelmax, argrelmin
import itertools

class Annotation:
    def __init__(self, source: np.ndarray) -> None:
        self.source = source
        
    def __call__(self) -> np.ndarray:
        return self.obtain_extrema_combinations(self.obtain_maxima_minima())


    def obtain_maxima_minima(self) -> np.ndarray:
        maxima = argrelmax(self.source)
        minima = argrelmin(self.source)
        
        if len(maxima) == 0 or len(minima) == 0:
            raise ValueError('Size of annotation source is too small so that no obvious zero gradient point was found.')

        return np.array(list(set(maxima[0].tolist() + minima[0].tolist())))

    def obtain_extrema_combinations(self, extremas: np.ndarray) -> List[List[int]]:
        extremas_list = extremas.tolist()
        extrema_combinations_list = []
        for i in range(len(extremas_list)):
            for combination in itertools.combinations(extremas_list, i):
                extrema_combinations_list.append(list(combination))

        extrema_combinations_list = [combination for combination in extrema_combinations_list if len(combination) > 2]

        return extrema_combinations_list

    