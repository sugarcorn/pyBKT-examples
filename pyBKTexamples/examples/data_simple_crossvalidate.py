import sys
sys.path.append('../')
import numpy as np
from pyBKT.generate import synthetic_data, random_model_uni
from pyBKT.fit import EM_fit
from test_utils import crossvalidate
from data_utils import ct_data_helper, check_data
from copy import deepcopy
np.seterr(divide='ignore', invalid='ignore')

num_fit_initializations = 20
skill_name = "Identifying units"

#data!
data = ct_data_helper.ct_data("ct.csv", skill_name)

check_data.check_data(data)
num_learns = len(data["resource_names"])
num_gs = len(data["gs_names"])

crossvalidate.crossvalidate(data, num_gs, num_learns, verbose=True)