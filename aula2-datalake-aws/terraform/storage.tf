resource "aws_s3_bucket" "buckets" {
  count  = length(var.bucket_names)
  bucket = "${var.bucket_names[count.index]}-${var.account}"
  tags = local.common_tags
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {
  count  = length(var.bucket_names)
  bucket = "${var.bucket_names[count.index]}-${var.account}"

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}