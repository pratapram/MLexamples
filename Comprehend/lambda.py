import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

def lambda_handler(event, context):    
	text = format(event['review'])    
	jsonstr = comprehend.detect_sentiment(Text=text, LanguageCode='en')
	print (jsonstr)
	return
