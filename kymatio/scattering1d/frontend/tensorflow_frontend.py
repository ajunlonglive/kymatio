import tensorflow as tf
import warnings

from ...frontend.tensorflow_frontend import ScatteringTensorFlow
from .base_frontend import ScatteringBase1D


class ScatteringTensorFlow1D(ScatteringTensorFlow, ScatteringBase1D):
    def __init__(self, J, shape, Q=1, T=None, max_order=2, oversampling=0,
            out_type='array', backend='tensorflow', name='Scattering1D'):
        ScatteringTensorFlow.__init__(self, name=name)
        ScatteringBase1D.__init__(self, J, shape, Q, T, max_order,
                oversampling, out_type, backend)
        ScatteringBase1D._instantiate_backend(self, 'kymatio.scattering1d.backend.')
        ScatteringBase1D.build(self)
        ScatteringBase1D.create_filters(self)

ScatteringTensorFlow1D._document()


__all__ = ['ScatteringTensorFlow1D']
