
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

def mean_average_precision(annType=None, annFile=None, resFile=None, maxDets=None):

    cocoGt=COCO(annFile)
    cocoDt=cocoGt.loadRes(resFile)
    
    imgIds=sorted(cocoGt.getImgIds())

    cocoEval = COCOeval(cocoGt,cocoDt,annType)
    cocoEval.params.maxDets = [maxDets]
    cocoEval.params.imgIds  = imgIds

    cocoEval.evaluate()
    cocoEval.accumulate()
    print('\nRESULTS:\n')
    cocoEval.summarize_2()



