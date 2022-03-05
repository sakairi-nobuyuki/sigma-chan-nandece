# coding: utf-8


from annotation.components import Annotation, annotation
import numpy as np
import random

class TestAnnotation:
    def test_init(self, mock_one_dim_ndarray: np.ndarray):
        annotation = Annotation(mock_one_dim_ndarray)
        
        assert isinstance(annotation, Annotation)
        assert len(list(annotation.obtain_maxima_minima())) > 0

    def test_peaks(self):
        source = np.array([random.random() for i in range(10)])

        print(source)

        annotation = Annotation(source)

        print(annotation.obtain_maxima_minima())
        print(annotation.obtain_extrema_combinations(annotation.obtain_maxima_minima()))

        
        

