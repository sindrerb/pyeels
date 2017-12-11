import numpy as np
import logging
_logger = logging.getLogger(__name__)

class Band:
    
    def __init__(self, k_grid, k_list, energies, waves):
        """ Create instance of Band with a k-grid, energies and waves
        
        :type  k_grid: ndarray
        :param k_grid: A Nx3 array representing N k-points for the energies
        
        :type  energies: ndarray
        :param energies: A vector of N energy-elements corresponding to the k-grid
        
        :type  waves: ndarray
        :param waves: A NxM array containing N wave vectors of length M representing orthogonal wavefunctions
        """
        
        self.k_grid = k_grid
        self.k_list = k_list
        if energies.shape[0] != k_grid.shape[0]:
            _logger.warning("Shape of energy ({}) does not match the length of the k-grid ({})".format(energies.shape,k_grid.shape[0]))
        else:
            self.energies = energies
        if energies.shape[0] != waves.shape[0]:
            _logger.warning("First dimension of waves ({}) does not match the shape of energies ({})".format(waves.shape,energies.shape))
        else:
            self.waves = waves

    def energy_min(self):
        """ Get the minimun energy value of band 
        :returns: minimum energy
        """
        return np.min(self.energies)

    def energy_max(self):
        """ Get the maximun energy value of band 
        :returns: maximum energy
        """
        return np.max(self.energies)
        
    def __repr__(self):
        """ Representing band object """
        return "Band object, E_min: {}, E_max: {}".format(self.energy_min().round(2),self.energy_max().round(2))