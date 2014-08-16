import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("chidat")

class PullDataError(BaseException):
    pass

class PullData(object):
    """Queries Chicago public data
    """

    def __init__(self):
        self.base_url = "http://data.cityofchicago.org/views"


    def pull(self, url, max_rows=None, return_type='frame'):
        """Pulls a csv of rows from the Chicago data portal based on the url, which can be found by visiting the page of the dataset on the web portal, selecting Export->SODA API

        **Parameters**

        * url <str> - URL to pull from
        * max_rows <int|None>: Maximum number of rows to request. If None, will try to pull as many as possible
        * return_type <str|"frame">: Return type is either a pandas DataFrame ("frame") or a list of dictionaries ("list")
        """

        if return_type not in ["frame", "list"]:
            raise PullDataError("return_type must be either 'frame' or 'list'")
            
        data = []
        offset = 0
        limit = 1000 #That's what the API allows
        while True:
            log.debug("Pulling {} records from offset {}".format(limit, offset))
            req_url = url + "?$limit={}&$offset={}&$order=:id".format(limit, offset)
            r = requests.get(req_url)
            if r.status_code != 200:
                log.info("Request resulted in status code {}, finished pulling".format({r.status_code}))
                break
            data.extend(r.json())
            offset += limit
            if max_rows and offset >= max_rows:
                log.debug("Maximum number of rows ({}) pulled".format(max_rows))
                break
                
        if not data:
            raise PullDataError("Pull failed, got no data")

        log.info("Got {} rows".format(len(data)))
        if return_type == "list":
            return data
        else:
            return pd.DataFrame(data)
        
    
    