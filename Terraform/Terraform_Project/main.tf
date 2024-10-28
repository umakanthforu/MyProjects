## CREATE AN S3 BUCKET ##

resource "aws_s3_bucket" "myprojects3" {
    bucket = var.bucketname
}

## BUCKET OWNERSHIP ###

resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.myprojects3.id

  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

## BUCKET PUBLIC ACCESS ALLOWING ##

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.myprojects3.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

## BUCKET ACL CONFIGURATION ##

resource "aws_s3_bucket_acl" "example" {
  depends_on = [
    aws_s3_bucket_ownership_controls.example,
    aws_s3_bucket_public_access_block.example,
  ]

  bucket = aws_s3_bucket.myprojects3.id
  acl    = "public-read"
}

## UPLOADING FILES TO S3 BUCKET ##

resource "aws_s3_object" "index" {
    bucket = aws_s3_bucket.myprojects3.id
    key = "index.html"
    source = "index.html"
    acl = "public-read"
}

resource "aws_s3_object" "error" {
    bucket = aws_s3_bucket.myprojects3.id
    key = "error.html"
    source = "error.html"
    acl = "public-read"  
}

## CONFIGURING STATIC WEB SITE ON S3 BUCKET ##

resource "aws_s3_bucket_website_configuration" "website" {
  bucket = aws_s3_bucket.myprojects3.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
  depends_on = [ aws_s3_bucket_acl.example ]
}


