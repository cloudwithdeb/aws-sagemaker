
sagemaker-iam-role      = "custom-sagemaker-iam-role"
sagemaker-iam-policy    = "custom-sagemaker-iam-policy"
sagemaker-notebook = {
  name          = "custom-notebook"
  instance-type = "ml.t2.medium"
}

tags = {
  "deployed by" = "Owusu Bright Debrah"
  "role"        = "Cloud Engineer"
  "Email"       = "owusubrightdebrah@gmail.com"
  "purpose"     = "To setup infrastructure for data science and machine learning teams"
}
