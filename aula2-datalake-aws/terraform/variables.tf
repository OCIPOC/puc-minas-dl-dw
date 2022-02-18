variable "aws_region" {
  default = "us-east-2"
}

variable "account" {
  default = 127012818163
}

variable "bucket_names" {
  description = "Create S3 buckets with these names"
  type        = list(string)
  default = [
    "puc-minas-landing-zone",
    "puc-minas-processing-zone",
    "puc-minas-delivery-zone",
    "puc-minas-emr-config"
  ]
}

variable "database_names" {
  description = "Create databases with these names"
  type        = list(string)
  default = [
    #landing-zone
    "puc_minas_dl_landing_zone",
    "puc_minas_dl_processing_zone",
    "puc_minas_dl_delivery_zone"
  ]
}

variable "bucket_paths" {
  description = "Paths to S3 bucket used by the crawler"
  type        = list(string)
  default = [
    "s3://puc-minas-landing-zone-127012818163",
    "s3://puc-minas-processing-zone-127012818163/bank",
    "s3://puc-minas-delivery-zone-127012818163"
  ]
}

variable "prefix" {
  default = "puc-minas"
}

variable "workspace" {
  default = "dev"
}

locals {
  prefix = "${var.prefix}-${var.workspace}"
  common_tags = {
    Project      = "Puc Minas"    
    Environment  = "Desenvolvimento"
  }
}