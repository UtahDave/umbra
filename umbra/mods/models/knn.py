'''
Take dataset X and run it through the knn algorithm
'''

# Import third party libs
from pyod.models.knn import KNN


def __mod_init__(hub):
    hub.models.knn.COMPS = {}


async def run(hub, pipe, data, train):
    '''
    Run the knn algorith on the given dataset
    '''
    if pipe not in hub.models.knn.COMPS:
        hub.models.knn.COMPS[pipe] = {'clf': KNN(contamination=0.01)}
    clf = hub.models.knn.COMPS[pipe]['clf']
    if train:
        clf.fit(train)
    if data:
        clf.fit(data)
        return clf.predict(data)
    return []