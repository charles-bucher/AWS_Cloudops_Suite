# Set root path of your repo
$RepoPath = "C:\Users\buche\docs\Desktop\REPOS\AWS_Cloudops_Suite"

# Lambda function folder
$LambdaPath = Join-Path $RepoPath "lambdas\my_function"

# Create folders if they don't exist
New-Item -ItemType Directory -Force -Path $LambdaPath

# Create __init__.py (marks it as a Python package)
$InitFile = Join-Path $LambdaPath "__init__.py"
if (!(Test-Path $InitFile)) { New-Item -ItemType File -Force -Path $InitFile }

# Create main.py if it doesn't exist
$MainFile = Join-Path $LambdaPath "main.py"
if (!(Test-Path $MainFile)) {
    @"
def handler(event, context):
    print('Lambda handler called with event:', event)
    return {'statusCode': 200, 'body': 'Hello from Lambda!'}
"@ | Set-Content -Path $MainFile
}

# Create test_main.py if it doesn't exist
$TestFile = Join-Path $LambdaPath "test_main.py"
if (!(Test-Path $TestFile)) {
    @"
from main import handler  # Direct import works inside my_function folder

# Simulate a Lambda event
event = {'test': 'data'}
context = {}

response = handler(event, context)
print('Lambda response:', response)
"@ | Set-Content -Path $TestFile
}

Write-Host "Folder structure and placeholder files created successfully."
