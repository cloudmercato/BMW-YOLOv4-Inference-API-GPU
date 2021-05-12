#!/usr/bin/env python
import sys
from deep_learning_service import DeepLearningService

sys.path.append('./inference')

dl_service = DeepLearningService()
dl_service.load_all_models()
