import boto3
import fastapi
from fastapi import FastAPI, Response, Request, Body
import xml.etree.ElementTree as ET

app=FastAPI()

@app.post("/post")
async def root(request: str=Body(media_type="application/xml")):
    try:
        root=ET.fromstring(request)
    except Exception as e:
        return {"Error: ", str(e)}, None
    s3_client=boto3.client('s3')
    response=ET.tostring(root).decode()
    try:
        # to put request in s3
        # s3_client.put_object(Body=request, Bucket='swarajdemoapi')
        # # to put request in s3
        s3_client.put_object(Body=response, Bucket='swarajdemoapi',Key='new_file_1')
    except Exception as e:
        return {"Error": "no response"}
    

    
    


