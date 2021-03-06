# coding: utf-8


from annotation.components import ExtremaAnnotation
import numpy as np
import random

class TestAnnotation:
    def test_init(self, mock_one_dim_ndarray: np.ndarray):
        #annotation = ExtremaAnnotation(mock_one_dim_ndarray)
        annotation = ExtremaAnnotation()
        
        assert isinstance(annotation, ExtremaAnnotation)
        assert len(list(annotation.obtain_maxima_minima(mock_one_dim_ndarray))) > 0

    def test_peaks(self):
        source = np.array([random.random() for i in range(10)])

        print(source)

        annotation = ExtremaAnnotation()

        print(annotation.obtain_maxima_minima(source))
        print(annotation.obtain_extrema_combinations(annotation.obtain_maxima_minima(source)))

        
        

