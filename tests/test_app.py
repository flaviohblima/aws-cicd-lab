import json
import sys
import os

# Make src importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from app import lambda_handler

def make_event(method='GET', path='/'):
  return { 'httpMethod': method, 'path': path}

def test_health_returns_200():
  result = lambda_handler(make_event('GET', '/health'), {})
  assert result['statusCode'] == 200
  body = json.loads(result['body'])
  assert body['status'] == 'healthy'
  print(f"✅ test_health_returns_200 passed")

def test_version_returns_200():
  result = lambda_handler(make_event('GET', '/version'), {})
  assert result['statusCode'] == 200
  body = json.loads(result['body'])
  assert body['version'] == '1.0.0'
  print(f"✅ test_version_returns_200 passed")
  
def test_unknown_route_returns_404():
  result = lambda_handler(make_event('GET', '/unknown'), {})
  assert result['statusCode'] == 404
  print(f"✅ test_unknown_route_returns_404 passed")

if __name__ == "__main__":
  test_health_returns_200()
  test_version_returns_200()
  test_unknown_route_returns_404()
  print("\n✅ All tests passed!")