import json

lst=[
  '{"name": "FCO", "path": "/1", "nbrofChildren": 0, "base": "FCO"}',
  '{"name": "Connection", "path": "/D/y", "nbrofChildren": 0, "base": "Connection"}',
  '{"name": "Language", "path": "/D", "nbrofChildren": 17, "base": "Language"}',
  '{"name": "Car_Repo", "path": "/D/P", "nbrofChildren": 0, "base": "Car_Repo"}',
  '{"name": "Car", "path": "/D/T", "nbrofChildren": 0, "base": "Car"}',
  '{"name": "Suspension", "path": "/D/h", "nbrofChildren": 0, "base": "Suspension"}',
  '{"name": "Brake", "path": "/D/3", "nbrofChildren": 0, "base": "Brake"}',
  '{"name": "Tyre", "path": "/D/V", "nbrofChildren": 0, "base": "Tyre"}',
  '{"name": "Wheels", "path": "/D/r", "nbrofChildren": 0, "base": "Wheels"}',
  '{"name": "Engine", "path": "/D/X", "nbrofChildren": 0, "base": "Engine"}',
  '{"name": "Controls", "path": "/D/c", "nbrofChildren": 0, "base": "Controls"}',
  '{"name": "ICE", "path": "/D/m", "nbrofChildren": 0, "base": "ICE"}',
  '{"name": "Electric", "path": "/D/2", "nbrofChildren": 0, "base": "Electric"}',
  '{"name": "DriveTrain", "path": "/D/Z", "nbrofChildren": 0, "base": "DriveTrain"}',
  '{"name": "Frontdrive", "path": "/D/N", "nbrofChildren": 0, "base": "Frontdrive"}',
  '{"name": "AllDrive", "path": "/D/Y", "nbrofChildren": 0, "base": "AllDrive"}',
  '{"name": "Multi-link", "path": "/D/R", "nbrofChildren": 0, "base": "Multi-link"}',
  '{"name": "Swing axle", "path": "/D/Q", "nbrofChildren": 0, "base": "Swing axle"}',
  '{"name": "Semi-trail arm", "path": "/D/L", "nbrofChildren": 0, "base": "Semi-trail arm"}'
]
lst='[%s]' % ', '.join(map(str, lst))
#print('[%s]' % ', '.join(map(str, lst)))
print(lst)