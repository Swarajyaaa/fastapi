import boto3
import xml.etree.ElementTree as ET

data='''<library>
  <book>
    <title>Harry Potter and the Philosopher's Stone</title>
    <author>J.K. Rowling</author>
    <year>1997</year>
  </book>
  <book>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
  </book>
  <book>
    <title>To Kill a Mockingbird</title>
    <author>Harper Lee</author>
    <year>1960</year>
  </book>
</library>'''
root=ET.fromstring(data)
response=ET.tostring(root).decode()

s3_client=boto3.client('s3',region_name='ap-south-1', aws_access_key_id='AKIA47NKTFI3LI2FB3NV', aws_secret_access_key='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')
try:
    # response = s3_client.list_objects(Bucket='swarajdemoapi')
    s3_client.put_object(Body=response, Bucket='swarajdemoapi',Key='new_file')
    print("succesfull")
except Exception as e:
    print("Error: ",e)
