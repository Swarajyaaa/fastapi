import boto3
import fastapi
from fastapi import FastAPI, Response, Request, Body
import xml.etree.ElementTree as ET

app = FastAPI()

@app.post("/post")
async def root(request: str = Body(media_type="application/xml")):
    try:
        root = ET.fromstring(request)
    except Exception as e:
        return {"Error": str(e)}

    s3_client = boto3.client('s3')
    request_body = ET.tostring(root).decode()
    response_body = "This is the response"

    try:
        # Upload request to S3
        s3_client.put_object(Body=request_body, Bucket='swarajdemoapi', Key='request_file.xml')
        # Upload response to S3
        s3_client.put_object(Body=response_body, Bucket='swarajdemoapi', Key='response_file.txt')
    except Exception as e:
        return {"Error": str(e)}

    return {"Success": "Request and response uploaded to S3"}
