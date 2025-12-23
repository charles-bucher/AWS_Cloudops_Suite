############################################################
# Lambda Function Module
# Path: terraform/lambda/main.tf
############################################################

# IAM Role for Lambda execution
resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = { Service = "lambda.amazonaws.com" }
      }
    ]
  })
}

# Attach basic execution policy to Lambda role
resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Lambda function
resource "aws_lambda_function" "my_function" {
  function_name    = "my_function"
  filename         = "${path.module}/../../lambdas/my_function/my_function.zip"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "main.handler"
  runtime          = "python3.8"

  source_code_hash = filebase64sha256("${path.module}/../../lambdas/my_function/my_function.zip")
}

# Optional outputs
output "lambda_function_name" {
  value = aws_lambda_function.my_function.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.my_function.arn
}
