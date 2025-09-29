variable "project" {
  type        = string
  description = "Project name prefix"
}

variable "cidr_block" {
  type        = string
  description = "VPC CIDR"
}

variable "public_subnets" {
  description = "Public subnet definitions"
  type = map(object({
    cidr = string
    az   = string
  }))
}

variable "private_subnets" {
  description = "Private subnet definitions"
  type = map(object({
    cidr = string
    az   = string
  }))
}

variable "tags" {
  type        = map(string)
  default     = {}
  description = "Common resource tags"
}
