# Copyright 2019 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Schema-enhanced versions of the operators from `autoai-ts-libs`_ to enable hyperparameter tuning.

.. _`autoai-ts-libs`: https://pypi.org/project/autoai-ts-libs/

Operators
=========

* lale_autoai.autoai_ts_libs. `AutoaiTSPipeline`_
* lale_autoai.autoai_ts_libs. `AutoaiWindowTransformedTargetRegressor`_
* lale_autoai.autoai_ts_libs. `AutoaiWindowedWrappedRegressor`_
* lale_autoai.autoai_ts_libs. `AutoRegression`_
* lale_autoai.autoai_ts_libs. `cubic`_
* lale_autoai.autoai_ts_libs. `DifferenceFlattenAutoEnsembler`_
* lale_autoai.autoai_ts_libs. `EnsembleRegressor`_
* lale_autoai.autoai_ts_libs. `fill`_
* lale_autoai.autoai_ts_libs. `flatten_iterative`_
* lale_autoai.autoai_ts_libs. `FlattenAutoEnsembler`_
* lale_autoai.autoai_ts_libs. `LocalizedFlattenAutoEnsembler`_
* lale_autoai.autoai_ts_libs. `linear`_
* lale_autoai.autoai_ts_libs. `MT2RForecaster`_
* lale_autoai.autoai_ts_libs. `next`_
* lale_autoai.autoai_ts_libs. `previous`_
* lale_autoai.autoai_ts_libs. `SmallDataWindowTargetTransformer`_
* lale_autoai.autoai_ts_libs. `StandardRowMeanCenter`_
* lale_autoai.autoai_ts_libs. `StandardRowMeanCenterMTS`_
* lale_autoai.autoai_ts_libs. `T2RForecaster`_
* lale_autoai.autoai_ts_libs. `TSPipeline`_
* lale_autoai.autoai_ts_libs. `WatForeForecaster`_
* lale_autoai.autoai_ts_libs. `WindowStandardRowMeanCenterMTS`_
* lale_autoai.autoai_ts_libs. `WindowStandardRowMeanCenterUTS`_
* lale_autoai.autoai_ts_libs. `WindowTransformerMTS`_
* lale_autoai.autoai_ts_libs. `TSADPipeline`_
* lale_autoai.autoai_ts_libs. `UnivariateGraphLassoAD`_
* lale_autoai.autoai_ts_libs. `PointwiseBoundedAnomalyDetector`_
* lale_autoai.autoai_ts_libs. `WindowedIsolationForest`_
* lale_autoai.autoai_ts_libs. `Flatten`_
* lale_autoai.autoai_ts_libs. `GeneralizedAnomalyModel`_
* lale_autoai.autoai_ts_libs. `GaussianGraphicalModel`_
* lale_autoai.autoai_ts_libs. `WindowedNN`_
* lale_autoai.autoai_ts_libs. `WindowedPCA`_
* lale_autoai.autoai_ts_libs. `WindowedLOF`_


.. _`AutoaiTSPipeline`: lale_autoai.autoai_ts_libs.autoai_ts_pipeline.html
.. _`AutoaiWindowTransformedTargetRegressor`: lale_autoai.autoai_ts_libs.autoai_window_transformed_target_regressor.html
.. _`AutoaiWindowedWrappedRegressor`: lale_autoai.autoai_ts_libs.autoai_windowed_wrapped_regressor.html
.. _`AutoRegression`: lale_autoai.autoai_ts_libs.auto_regression.html
.. _`cubic`: lale_autoai.autoai_ts_libs.cubic.html
.. _`DifferenceFlattenAutoEnsembler`: lale_autoai.autoai_ts_libs.difference_flatten_auto_ensembler.html
.. _`EnsembleRegressor`: lale_autoai.autoai_ts_libs.ensemble_regressor.html
.. _`fill`: lale_autoai.autoai_ts_libs.fill.html
.. _`flatten_iterative`: lale_autoai.autoai_ts_libs.flatten_iterative.html
.. _`FlattenAutoEnsembler`: lale_autoai.autoai_ts_libs.flatten_auto_ensembler.html
.. _`LocalizedFlattenAutoEnsembler`: lale_autoai.autoai_ts_libs.localized_flatten_auto_ensembler.html
.. _`linear`: lale_autoai.autoai_ts_libs.linear.html
.. _`MT2RForecaster`: lale_autoai.autoai_ts_libs.mt2r_forecaster.html
.. _`next`: lale_autoai.autoai_ts_libs.next.html
.. _`previous`: lale_autoai.autoai_ts_libs.previous.html
.. _`SmallDataWindowTargetTransformer`: lale_autoai.autoai_ts_libs.small_data_window_target_transformer.html
.. _`StandardRowMeanCenter`: lale_autoai.autoai_ts_libs.standard_row_mean_center.html
.. _`StandardRowMeanCenterMTS`: lale_autoai.autoai_ts_libs.standard_row_mean_center_mts.html
.. _`T2RForecaster`: lale_autoai.autoai_ts_libs.t2r_forecaster.html
.. _`TSPipeline`: lale_autoai.autoai_ts_libs.ts_pipeline.html
.. _`WatForeForecaster`: lale_autoai.autoai_ts_libs.watfore_forecaster.html
.. _`WindowStandardRowMeanCenterMTS`: lale_autoai.autoai_ts_libs.window_standard_row_mean_center_mts.html
.. _`WindowStandardRowMeanCenterUTS`: lale_autoai.autoai_ts_libs.window_standard_row_mean_center_uts.html
.. _`WindowTransformerMTS`: lale_autoai.autoai_ts_libs.window_transformer_mts.html
.. _`TSADPipeline`: lale_autoai.autoai_ts_libs.ts_ad_pipeline.html
.. _`UnivariateGraphLassoAD`: lale_autoai.autoai_ts_libs.graph_lasso_ad.html
.. _`PointwiseBoundedAnomalyDetector`: lale_autoai.autoai_ts_libs.pointwise_bounded_ad.html
.. _`WindowedIsolationForest`: lale_autoai.autoai_ts_libs.windowed_isolation_forest.html
.. _`Flatten`: lale_autoai.autoai_ts_libs.flatten.html
.. _`GeneralizedAnomalyModel`: lale_autoai.autoai_ts_libs.generalized_anomaly_model.html
.. _`GaussianGraphicalModel`: lale_autoai.autoai_ts_libs.gaussian_graphical_anomaly_model.html
.. _`WindowedNN`: lale_autoai.autoai_ts_libs.windowed_nn.html
.. _`WindowedPCA`: lale_autoai.autoai_ts_libs.windowed_pca.html
.. _`WindowedLOF`: lale_autoai.autoai_ts_libs.windowed_lof.html
"""
from sklearn.experimental import enable_iterative_imputer  # noqa

from .auto_regression import AutoRegression
from .autoai_ts_pipeline import AutoaiTSPipeline
from .autoai_window_transformed_target_regressor import (
    AutoaiWindowTransformedTargetRegressor,
)
from .autoai_windowed_wrapped_regressor import AutoaiWindowedWrappedRegressor
from .cubic import cubic
from .difference_flatten_auto_ensembler import DifferenceFlattenAutoEnsembler
from .ensemble_regressor import EnsembleRegressor
from .fill import fill
from .flatten_auto_ensembler import FlattenAutoEnsembler
from .flatten_iterative import flatten_iterative
from .linear import linear
from .localized_flatten_auto_ensembler import LocalizedFlattenAutoEnsembler
from .mt2r_forecaster import MT2RForecaster
from .next import next
from .previous import previous
from .small_data_window_target_transformer import SmallDataWindowTargetTransformer
from .small_data_window_transformer import SmallDataWindowTransformer
from .standard_row_mean_center import StandardRowMeanCenter
from .standard_row_mean_center_mts import StandardRowMeanCenterMTS
from .t2r_forecaster import T2RForecaster
from .ts_pipeline import TSPipeline
from .watfore_forecaster import WatForeForecaster
from .window_standard_row_mean_center_mts import WindowStandardRowMeanCenterMTS
from .window_standard_row_mean_center_uts import WindowStandardRowMeanCenterUTS
from .window_transformer_mts import WindowTransformerMTS
from .ts_ad_pipeline import TSADPipeline
from .graph_lasso_ad import UnivariateGraphLassoAD
from .pointwise_bounded_ad import PointwiseBoundedAnomalyDetector
from .windowed_isolation_forest import WindowedIsolationForest
from .flatten import Flatten
from .generalized_anomaly_model import GeneralizedAnomalyModel
from .gaussian_graphical_anomaly_model import GaussianGraphicalModel
from .windowed_nn import WindowedNN
from .windowed_pca import WindowedPCA
from .windowed_lof import WindowedLOF

