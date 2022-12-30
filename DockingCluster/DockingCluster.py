from dask_gateway import Gateway
from urllib.parse import urlparse
import asyncio
import random
import string
import os
import shutil
import boto3


class docking_cluster:
    def __init__(self, config):
        self.name=config['name']
        self.maximum_scale=config['maximum_scale']
        self.address=config['address']
        self.partition=config['partition']
        self.worker_instance_type=config['worker_instance_type']
        self.scheduler_instance_type=config['scheduler_instance_type']
        self.client=None
        self.cluster=None
        self.status=None
        self.tmp_folder_name=None
        self.failn=0
        self.gateway=None
    
    async def connect(self):
        try:
            gateway = Gateway(address=self.address,asynchronous=True)
            print("Creating cluster "+self.name)
            cluster = await gateway.new_cluster(worker_instance_type=self.worker_instance_type,scheduler_instance_type=self.scheduler_instance_type)
            await cluster.adapt(minimum=0,maximum=self.maximum_scale)
            client = await cluster.get_client()
            print("DASK cluster is started on "+self.address+" with "+str(self.maximum_scale)+" max workers")
            
            print(client.dashboard_link)
            
            self.cluster=cluster
            self.client=client
            self.status="running"
            self.gateway=gateway

        except Exception as e:
            self.status="failed"
            self.failn=self.failn+1
            #TODO: shutdown cluster
            print("Failed to start DASK cluster on "+self.address)
            print(repr(e))        
            
    async def shutdown(self):
        try:
            await self.client.close()
            await self.cluster.shutdown()
            self.status="stopped"
            self.tmp_folder_name=None
            print("Dask cluster "+ self.name+ " is successfully shut down")
        except Exception as e:
            print("Failed to shut down dask cluster "+ self.name)

    async def get_tasks_count(self):
        def get_number_of_tasks(dask_scheduler=None):
            num=0
            for i in dask_scheduler.tasks:
                if dask_scheduler.tasks[i].state == "processing" or dask_scheduler.tasks[i].state == "no-worker":
                    num=num+1
            return num
        num_tasks=await self.client.run_on_scheduler(get_number_of_tasks)
        return(num_tasks)

    def get_number_of_workers(self):
        try:
            sched_info = self.client.scheduler_info()
            num_workers = len(sched_info['workers'])
            return num_workers
        except:
            return 0