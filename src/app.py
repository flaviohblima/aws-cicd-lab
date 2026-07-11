import json
import os
from datetime import datetime

VERSION = "1.0.2"

def lambda_handler(event, context):
  method = event.get('httpMethod', 'GET')
  path = event.get('path', '/')
  
  if method == 'GET' and path == '/health':
    return response(200, {
      "status": "healthy",
      "version": VERSION,
      "environment": os.environ.get('ENVIRONMENT', 'unknown'),
      "timestamp": datetime.utcnow().isoformat()
    })
    
  if method == 'GET' and path == '/version':
    return response(200, {
      "version": VERSION,
      "deployed_by": "AWS CodePipeline",
      "message": "Automatically deployed on every git push!"
    })
    
  return response(404, {"error": "Route not found", "path": path})
    
def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, indent=2)
    }