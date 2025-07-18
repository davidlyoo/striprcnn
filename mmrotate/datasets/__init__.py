# Copyright (c) OpenMMLab. All rights reserved.
from .builder import build_dataset  # noqa: F401, F403
from .dota import DOTADataset #,DOTAv15Dataset, DOTAv2Dataset  # noqa: F401, F403
from .hrsc import HRSCDataset  # noqa: F401, F403
from .pipelines import *  # noqa: F401, F403
from .sar import SARDataset  # noqa: F401, F403
from .fair import FairDataset
from .dota_1_5 import DOTADataset15
from .dior import DIORDataset
from .aihub import AIHUBDataset
from .v5 import V5Dataset
from .v6 import V6Dataset
__all__ = ['SARDataset','DIORDataset', 'DOTADataset', 'build_dataset', 'HRSCDataset', 
           'FairDataset', 'DOTADataset15', 'AIHUBDataset', 'V5Dataset', 'V6Dataset']
