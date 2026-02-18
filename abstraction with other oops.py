import logging
import time
from abc import ABC,abstractmethod

logging.basicConfig (
    level =logging.INFO,
    format= "%(asctime)s-%(levelname)s-%(message)s")

class etlerror(Exception):
    pass

class etljob(ABC):
    def __init__(self,job_name,retries=2,delay=2):
        self.job_name=job_name
        self.__status = "created"
        self.retries =retries
        self.delay = delay
        
    def run(self):
        attempt=0
        
        while attempt <=self.retries:
            try:
                self._start()
                
                data = self.extract()
                data = self.transform(data)
                self.load(data)
                
                self._finish()
                return
            
            except Exception as e:
                attempt+=1
                logging.error(f"{self.job_name} failed on attempt {attempt}:{e}")
                if attempt>self.retries:
                    self.__status = "failed"
                    logging.error(f"{self.job_name} permanently failed")
                    raise etlerror(f"{self.job_name} failed after retries") from e
                logging.info(f"retrying {self.job_name} in {self.delay} seconds...")
                time.sleep(self.delay)
                
    def _start(self):
        self.__status = "running"
        logging.info(f"{self.job_name} started")
                
    def _finish(self):
        self.__status = "completed"
        logging.info(f"{self.job_name} completed successfully")
        
    @property
    def status(self):
        return self.__status
        
    @abstractmethod
    def extract(self):
        pass
    
    @abstractmethod
    def transform(self,data):
        pass
    
    @abstractmethod
    def load(self,data):
        pass
        
class salesetl(etljob):

    def extract(self):
        logging.info("extracting sales data")
        return ([100,200,300])
        
    def transform(self,data):
        logging.info("transforming sales data")
        return [x*1.1 for x in data]
        
    def load(self,data):
        logging.info(f"loading sales data: {data}")
        
class inventoryetl(etljob):
    
    def __init__(self,job_name,retries=2,delay=2):
        super().__init__(job_name,retries,delay)
        self.fail_once=True
        
    def extract(self):
        logging.info("extracting the inventory")
        return [10,20]
        
    def transform(self,data):
        logging.info("transform inventory")
        return data
        
    def load(self,data):
        if self.fail_once:
            self.fail_once = False
            raise ValueError("Temporary Db failure")
        logging.info(f"loading data {data}")

if __name__ == "__main__":
    jobs = [salesetl("Salesjob"),inventoryetl("Inventoryjob")]
    for job in jobs:
        try:
            job.run()
        except etlerror as e:
            logging.error(f"Job {job.job_name} failed: {e}")

        print("finalstatus:",job.status)
        print("---"*10)
            
            

            

                    
                    
                    
                    
                    
    