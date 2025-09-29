variable "project" {
  type        = string
  description = "Project name"
}

variable "cluster_role_arn" {
  type        = string
  description = "IAM role ARN for EKS cluster"
}

variable "node_role_arn" {
  type        = string
  description = "IAM role ARN for worker nodes"
}

variable "subnet_ids" {
  type        = list(string)
  description = "Subnets for worker nodes"
}

variable "desired_capacity" {
  type    = number
  default = 3
}

variable "max_capacity" {
  type    = number
  default = 6
}

variable "min_capacity" {
  type    = number
  default = 1
}

variable "capacity_type" {
  type    = string
  default = "ON_DEMAND"
}

variable "instance_types" {
  type    = list(string)
  default = ["m6i.large"]
}

variable "tags" {
  type    = map(string)
  default = {}
}
